var streamft = require("./")
  , test = require("tape")
  , through = require("through")
  , fs = require("fs")
  , rimraf = require("rimraf")
  , Buffer = require("buffer").Buffer

var tmpDir = __dirname + "/tmp"

function setUp () {
  rimraf.sync(tmpDir)
  fs.mkdirSync(tmpDir)
}

test("from path to path", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  streamft(createStream).from.path(__dirname + "/index.js").to.path(tmpDir + "/index.js", function (er) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = fs.readFileSync(__dirname + "/index.js", {encoding: "utf8"})
      , output = fs.readFileSync(tmpDir + "/index.js", {encoding: "utf8"})

    t.equal(input, output, "Should have written input to output destination")
    t.end()
  })
})

test("from paths to paths", function (t) {
  setUp()

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var paths = ["/index.js", "/README.md"]
    , srcPaths = paths.map(function (p) { return __dirname + p })
    , destPaths = paths.map(function (p) { return tmpDir + p })

  t.plan(paths.length + 2)

  streamft(createStream).from.paths(srcPaths).to.paths(destPaths, function (er) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    srcPaths.forEach(function (srcPath, i) {
      var input = fs.readFileSync(srcPath, {encoding: "utf8"})
        , output = fs.readFileSync(destPaths[i], {encoding: "utf8"})

      t.equal(input, output, "Should have written input " + i + " to output " + i + " destination")
    })

    t.end()
  })
})

test("from path to path shorthand", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  streamft(createStream).from(__dirname + "/index.js").to(tmpDir + "/index.js", function (er) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = fs.readFileSync(__dirname + "/index.js", {encoding: "utf8"})
      , output = fs.readFileSync(tmpDir + "/index.js", {encoding: "utf8"})

    t.equal(input, output, "Should have written input to output destination")
    t.end()
  })
})

test("from path to string", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  streamft(createStream).from.path(__dirname + "/index.js").to.string(function (er, str) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = fs.readFileSync(__dirname + "/index.js", {encoding: "utf8"})

    t.equal(input, str, "Should have buffered input as a string")
    t.end()
  })
})

test("from path to string with options", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  streamft(createStream).from.path(__dirname + "/index.js").to.string({encoding: "utf8"}, function (er, str) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = fs.readFileSync(__dirname + "/index.js", {encoding: "utf8"})

    t.equal(input, str, "Should have buffered input as a string")
    t.end()
  })
})

test("from paths to strings", function (t) {
  setUp()

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var srcPaths = [__dirname + "/index.js", __dirname + "/README.md"]

  t.plan(srcPaths.length + 2)

  streamft(createStream).from.paths(srcPaths).to.strings(function (er, strs) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    srcPaths.forEach(function (srcPath, i) {
      var input = fs.readFileSync(srcPath, {encoding: "utf8"})
      t.equal(input, strs[i], "Should have written input " + i + " to output string " + i)
    })

    t.end()
  })
})

test("from path to buffer", function (t) {
  setUp()

  t.plan(4)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  streamft(createStream).from.path(__dirname + "/index.js").to.buffer(function (er, buf) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = fs.readFileSync(__dirname + "/index.js")

    t.ok(Buffer.isBuffer(buf), "Buffer should be a buffer")
    t.equal(input.toString("utf8"), buf.toString("utf8"), "Should have buffered input")
    t.end()
  })
})

test("from string to path", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var input = "Testing 123"

  streamft(createStream).from.string(input).to.path(tmpDir + "/test.txt", function (er) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var output = fs.readFileSync(tmpDir + "/test.txt", {encoding: "utf8"})

    t.equal(input, output, "Should have written input to output destination")
    t.end()
  })
})

test("from strings to paths", function (t) {
  setUp()

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var strings = ["Test 1", "Test 2"]
    , destPaths = strings.map(function (s, i) { return tmpDir + "/" + i + ".txt" })

  t.plan(destPaths.length + 2)

  streamft(createStream).from.strings(strings).to.paths(destPaths, function (er) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    strings.forEach(function (str, i) {
      var output = fs.readFileSync(destPaths[i], {encoding: "utf8"})

      t.equal(str, output, "Should have written string " + i + " to output " + i + " destination")
    })

    t.end()
  })
})

test("from string to string", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var input = "Testing 123"

  streamft(createStream).from.string(input).to.string(function (er, str) {
    t.ifError(er)
    t.ok(writeCount > 0, "Should have passed through the through stream")
    t.equal(input, str, "Should have written input to output destination")
    t.end()
  })
})

test("from strings to strings", function (t) {
  setUp()

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var strings = ["Test 1", "Test 2"]

  t.plan(strings.length + 2)

  streamft(createStream).from.strings(strings).to.strings(function (er, strs) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    strings.forEach(function (str, i) {
      t.equal(str, strs[i], "Should have written string " + i + " to output string " + i)
    })

    t.end()
  })
})

test("from string to buffer", function (t) {
  setUp()

  t.plan(4)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var input = "Testing 123"

  streamft(createStream).from.string(input).to.buffer(function (er, buf) {
    t.ifError(er)
    t.ok(writeCount > 0, "Should have passed through the through stream")
    t.ok(Buffer.isBuffer(buf), "Buffer should be a buffer")
    t.equal(input, buf.toString("utf8"), "Should have written input to output destination")
    t.end()
  })
})

test("from strings to buffers", function (t) {
  setUp()

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var strings = ["Test 1", "Test 2"]

  t.plan((strings.length * 2) + 2)

  streamft(createStream).from.strings(strings).to.buffers(function (er, bufs) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    strings.forEach(function (str, i) {
      t.ok(Buffer.isBuffer(bufs[i]))
      t.equal(str, bufs[i].toString("utf8"), "Should have written string " + i + " to output buffer " + i)
    })

    t.end()
  })
})

test("concat from paths to path", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var paths = ["/index.js", "/README.md"]
    , srcPaths = paths.map(function (p) { return __dirname + p })
    , destPath = tmpDir + "/munged.js.md"

  streamft(createStream).concat.from.paths(srcPaths).to.path(destPath, function (er) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = srcPaths.map(function (srcPath) {
      return fs.readFileSync(srcPath, {encoding: "utf8"})
    })

    var output = fs.readFileSync(destPath, {encoding: "utf8"})

    t.equal(input.join(""), output, "Should have written inputs to output destination")

    t.end()
  })
})

test("concat from paths to string", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var paths = ["/index.js", "/README.md"]
    , srcPaths = paths.map(function (p) { return __dirname + p })

  streamft(createStream).concat.from.paths(srcPaths).to.string(function (er, str) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = srcPaths.map(function (srcPath) {
      return fs.readFileSync(srcPath, {encoding: "utf8"})
    })

    t.equal(input.join(""), str, "Should have written inputs to output string")

    t.end()
  })
})

test("concat from paths to buffer", function (t) {
  setUp()

  t.plan(4)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var paths = ["/index.js", "/README.md"]
    , srcPaths = paths.map(function (p) { return __dirname + p })

  streamft(createStream).concat.from.paths(srcPaths).to.buffer(function (er, buf) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var input = srcPaths.map(function (srcPath) {
      return fs.readFileSync(srcPath, {encoding: "utf8"})
    })

    t.ok(Buffer.isBuffer(buf), "Buffer should be a buffer")
    t.equal(input.join(""), buf.toString("utf8"), "Should have written inputs to output buffer")

    t.end()
  })
})

test("concat from strings to path", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var strings = ["var foo = 1138;", "var bar = 138;"]
    , destPath = tmpDir + "/munged.js"

  streamft(createStream).concat.from.strings(strings).to.path(destPath, function (er) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    var output = fs.readFileSync(destPath, {encoding: "utf8"})

    t.equal(strings.join(""), output, "Should have written input strings to output destination")

    t.end()
  })
})

test("concat from strings to strings", function (t) {
  setUp()

  t.plan(3)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var strings = ["var foo = 1138;", "var bar = 138;"]

  streamft(createStream).concat.from.strings(strings).to.string(function (er, str) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    t.equal(strings.join(""), str, "Should have written input strings to output string")

    t.end()
  })
})

test("concat from strings to buffer", function (t) {
  setUp()

  t.plan(4)

  var writeCount = 0

  var createStream = function () {
    return through(function (data) {
      writeCount++
      this.queue(data)
    })
  }

  var strings = ["var foo = 1138;", "var bar = 138;"]

  streamft(createStream).concat.from.strings(strings).to.buffer(function (er, buf) {
    t.ifError(er)

    t.ok(writeCount > 0, "Should have passed through the through stream")

    t.ok(Buffer.isBuffer(buf), "Buffer should be a buffer")
    t.equal(strings.join(""), buf.toString("utf8"), "Should have written input strings to output string")

    t.end()
  })
})