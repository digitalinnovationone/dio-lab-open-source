var fs = require('fs')
var path = require('path')
var test = require('tape')
var markdownpdf = require('../')
var tmp = require('tmp')
var through = require('through2')
var pdfText = require('pdf-text')

tmp.setGracefulCleanup()

test('generate a nonempty PDF from ipsum.md', function (t) {
  t.plan(4)

  tmp.file({ postfix: '.pdf' }, function (er, tmpPdfPath, tmpPdfFd) {
    t.ifError(er)
    fs.closeSync(tmpPdfFd)

    markdownpdf().from(path.join(__dirname, '/fixtures/ipsum.md')).to(tmpPdfPath, function (er) {
      t.ifError(er)

      // Read the file
      fs.readFile(tmpPdfPath, { encoding: 'utf8' }, function (er, data) {
        t.ifError(er)
        // Test not empty
        t.ok(data.length > 0)
        t.end()
      })
    })
  })
})

test('generate PDF with CSS from ipsum.md and style.css', function (t) {
  t.plan(6)

  tmp.file({ postfix: '.pdf' }, function (er, tmpPdfPath, tmpPdfFd) {
    t.ifError(er)
    fs.closeSync(tmpPdfFd)

    markdownpdf({
      cssPath: path.join(__dirname, '/fixtures/style.css')
    }).from(path.join(__dirname, '/fixtures/ipsum.md')).to(tmpPdfPath, function (er) {
      t.ifError(er)

      // Read the file
      fs.readFile(tmpPdfPath, { encoding: 'utf8' }, function (er, data) {
        t.ifError(er)
        // Test not empty
        t.ok(data.length > 0)

        pdfText(tmpPdfPath, function (er, chunks) {
          t.ifError(er)

          t.ok(/forty-two/.test(chunks.join('')), 'contains h1::after injected content')
          t.end()
        })
      })
    })
  })
})

test('output should have a header and footer', function (t) {
  t.plan(7)

  tmp.file({ postfix: '.pdf' }, function (er, tmpPdfPath, tmpPdfFd) {
    t.ifError(er)
    fs.closeSync(tmpPdfFd)

    markdownpdf({ runningsPath: path.join(__dirname, '/fixtures/runnings.js') }).from(path.join(__dirname, '/fixtures/ipsum.md')).to(tmpPdfPath, function (er) {
      t.ifError(er)

      // Read the file
      fs.readFile(tmpPdfPath, { encoding: 'utf8' }, function (er, data) {
        t.ifError(er)
        // Test not empty
        t.ok(data.length > 0)

        // Header and footer included?
        pdfText(tmpPdfPath, function (er, chunks) {
          t.ifError(er)

          t.ok(/Some\s?Header/.test(chunks.join('')))
          t.ok(/Some\s?Footer/.test(chunks.join('')))
          t.end()
        })
      })
    })
  })
})

test('should call preProcessMd hook', function (t) {
  t.plan(3)

  var writeCount = 0
  var preProcessMd = function () { return through(function (data, enc, cb) { writeCount++; this.push(data); cb() }) }

  markdownpdf({ preProcessMd: preProcessMd }).from(path.join(__dirname, '/fixtures/ipsum.md')).to.string(function (er, pdfStr) {
    t.ifError(er)

    // Test not empty
    t.ok(pdfStr.length > 0)
    t.ok(writeCount > 0, 'Write count expected to be > 0')
    t.end()
  })
})

test('should call preProcessHtml hook', function (t) {
  t.plan(3)

  var writeCount = 0
  var preProcessHtml = function () { return through(function (data, enc, cb) { writeCount++; this.push(data); cb() }) }

  markdownpdf({ preProcessHtml: preProcessHtml }).from(path.join(__dirname, '/fixtures/ipsum.md')).to.string(function (er, pdfStr) {
    t.ifError(er)

    // Test not empty
    t.ok(pdfStr.length > 0)
    t.ok(writeCount > 0, 'Write count expected to be > 0')
    t.end()
  })
})

test('should concatenate source files', function (t) {
  t.plan(4)

  var files = [
    path.join(__dirname, '/fixtures/first.md'),
    path.join(__dirname, '/fixtures/second.md')
  ]

  tmp.file({ postfix: '.pdf' }, function (er, tmpPdfPath, tmpPdfFd) {
    t.ifError(er)
    fs.closeSync(tmpPdfFd)

    markdownpdf().concat.from(files).to(tmpPdfPath, function (er) {
      t.ifError(er)

      // Read the file
      fs.readFile(tmpPdfPath, { encoding: 'utf8' }, function (er, data) {
        t.ifError(er)
        // Test not empty
        t.ok(data.length > 0)
        t.end()
      })
    })
  })
})

test('should write to multiple paths when converting multiple files', function (t) {
  t.plan(6)

  var files = [
    path.join(__dirname, '/fixtures/first.md'),
    path.join(__dirname, '/fixtures/second.md')
  ]

  tmp.file({ postfix: '.pdf' }, function (er, tmpPdfPath0, tmpPdfFd0) {
    t.ifError(er)
    fs.closeSync(tmpPdfFd0)

    tmp.file({ postfix: '.pdf' }, function (er, tmpPdfPath1, tmpPdfFd1) {
      t.ifError(er)
      fs.closeSync(tmpPdfFd1)

      markdownpdf().from.paths(files).to.paths([tmpPdfPath0, tmpPdfPath1], function (er) {
        t.ifError(er)

        // Read the file
        var content0 = fs.readFileSync(tmpPdfPath0, { encoding: 'utf8' })
        var content1 = fs.readFileSync(tmpPdfPath1, { encoding: 'utf8' })

        t.ok(content0.length > 0)
        t.ok(content1.length > 0)
        t.ok(content0.length !== content1.length)

        t.end()
      })
    })
  })
})

test('should accept remarkable preset', function (t) {
  t.plan(2)

  var html = ''
  var opts = {
    remarkable: { preset: 'full' },
    preProcessHtml: function () {
      return through(
        function transform (chunk, enc, cb) {
          html += chunk
          cb()
        },
        function flush (cb) {
          var htmlSupTagFound = (html.indexOf('<sup>st</sup>') > -1)
          t.ok(htmlSupTagFound, 'html <sup> tag not found for preset "full"')
          cb()
        }
      )
    }
  }

  // Preset 'full' - expecting <sup>-tag in html
  markdownpdf(opts).from.string('1^st^ of January').to.string(function (er, pdfStr) {
    t.ifError(er)
    t.end()
  })
})

test('should initialize remarkable plugins', function (t) {
  t.plan(2)

  var pluginInit = false

  var remarkableOpts = {
    plugins: [
      // should skip non-functions
      undefined,
      'test',
      function (md, opts) {
        pluginInit = true
      }
    ]
  }

  markdownpdf({ remarkable: remarkableOpts }).from(path.join(__dirname, '/fixtures/ipsum.md')).to.string(function (er, pdfStr) {
    t.ifError(er)

    t.assert(pluginInit, 'check plugin init')
    t.end()
  })
})
