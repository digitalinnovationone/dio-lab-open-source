var fs = require('fs')
var path = require('path')
var childProcess = require('child_process')
var through = require('through2')
var extend = require('extend')
var { Remarkable } = require('remarkable')
var hljs = require('highlight.js')
var tmp = require('tmp')
var duplexer = require('duplexer')
var streamft = require('stream-from-to')

tmp.setGracefulCleanup()

function markdownpdf (opts) {
  opts = opts || {}
  opts.cwd = opts.cwd ? path.resolve(opts.cwd) : process.cwd()
  opts.phantomPath = opts.phantomPath || require('phantomjs-prebuilt').path
  opts.runningsPath = opts.runningsPath ? path.resolve(opts.runningsPath) : path.join(__dirname, 'runnings.js')
  opts.cssPath = opts.cssPath ? path.resolve(opts.cssPath) : path.join(__dirname, 'css', 'pdf.css')
  opts.highlightCssPath = opts.highlightCssPath ? path.resolve(opts.highlightCssPath) : path.join(__dirname, 'css', 'highlight.css')
  opts.paperFormat = opts.paperFormat || 'A4'
  opts.paperOrientation = opts.paperOrientation || 'portrait'
  opts.paperBorder = opts.paperBorder || '2cm'
  opts.renderDelay = opts.renderDelay == null ? 0 : opts.renderDelay
  opts.loadTimeout = opts.loadTimeout == null ? 10000 : opts.loadTimeout
  opts.preProcessMd = opts.preProcessMd || function () { return through() }
  opts.preProcessHtml = opts.preProcessHtml || function () { return through() }
  opts.remarkable = extend({ breaks: true }, opts.remarkable)
  opts.remarkable.preset = opts.remarkable.preset || 'default'
  opts.remarkable.plugins = opts.remarkable.plugins || []
  opts.remarkable.syntax = opts.remarkable.syntax || []

  var md = ''

  var mdToHtml = through(
    function transform (chunk, enc, cb) {
      md += chunk
      cb()
    },
    function flush (cb) {
      var self = this

      var mdParser = new Remarkable(opts.remarkable.preset, extend({
        highlight: function (str, language) {
          if (language && hljs.getLanguage(language)) {
            try {
              return hljs.highlight(str, { language }).value
            } catch (err) {}
          }

          try {
            return hljs.highlightAuto(str).value
          } catch (err) {}

          return ''
        }
      }, opts.remarkable))

      opts.remarkable.plugins.forEach(function (plugin) {
        if (plugin && typeof plugin === 'function') {
          mdParser.use(plugin)
        }
      })

      opts.remarkable.syntax.forEach(function (rule) {
        try {
          mdParser.core.ruler.enable([rule])
        } catch (err) {}
        try {
          mdParser.block.ruler.enable([rule])
        } catch (err) {}
        try {
          mdParser.inline.ruler.enable([rule])
        } catch (err) {}
      })

      self.push(mdParser.render(md))
      self.push(null)
    }
  )

  var inputStream = through()
  var outputStream = through()

  // Stop input stream emitting data events until we're ready to read them
  inputStream.pause()

  // Create tmp file to save HTML for phantom to process
  tmp.file({ postfix: '.html' }, function (err, tmpHtmlPath, tmpHtmlFd) {
    if (err) return outputStream.emit('error', err)
    fs.closeSync(tmpHtmlFd)

    // Create tmp file to save PDF to
    tmp.file({ postfix: '.pdf' }, function (err, tmpPdfPath, tmpPdfFd) {
      if (err) return outputStream.emit('error', err)
      fs.closeSync(tmpPdfFd)

      var htmlToTmpHtmlFile = fs.createWriteStream(tmpHtmlPath)

      htmlToTmpHtmlFile.on('finish', function () {
        // Invoke phantom to generate the PDF
        var childArgs = [
          path.join(__dirname, 'phantom', 'render.js'),
          tmpHtmlPath,
          tmpPdfPath,
          opts.cwd,
          opts.runningsPath,
          opts.cssPath,
          opts.highlightCssPath,
          opts.paperFormat,
          opts.paperOrientation,
          typeof opts.paperBorder === 'object' ? JSON.stringify(opts.paperBorder) : opts.paperBorder,
          opts.renderDelay,
          opts.loadTimeout
        ]

        childProcess.execFile(opts.phantomPath, childArgs, function (err, stdout, stderr) {
          // if (stdout) console.log(stdout)
          // if (stderr) console.error(stderr)
          if (err) return outputStream.emit('error', err)
          fs.createReadStream(tmpPdfPath).pipe(outputStream)
        })
      })

      // Setup the pipeline
      inputStream
        .pipe(opts.preProcessMd())
        .pipe(mdToHtml)
        .pipe(opts.preProcessHtml())
        .pipe(htmlToTmpHtmlFile)

      inputStream.resume()
    })
  })

  return extend(
    duplexer(inputStream, outputStream),
    streamft(function () {
      return markdownpdf(opts)
    })
  )
}

module.exports = markdownpdf
