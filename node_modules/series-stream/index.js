var PassThrough = require('stream').PassThrough
var inherits = require('util').inherits

function SeriesStream () {
  PassThrough.apply(this, arguments)
  this._current = null
  this._queue = []
}
inherits(SeriesStream, PassThrough)

SeriesStream.prototype.on = function (ev, fn) {
  var res = PassThrough.prototype.on.call(this, ev, fn)

  if (ev === 'data' && !this._current) {
    this._next()
  }

  return res
}

SeriesStream.prototype.pipe = function (dest) {
  PassThrough.prototype.pipe.call(this, dest)

  if (!this._current) {
    this._next()
  }

  return dest
}

SeriesStream.prototype.add = function (src) {
  this._queue.push(src)
  return this
}

SeriesStream.prototype._next = function () {
  this._current = null
  if (!this._queue.length) return
  var next = this._queue.shift()
  this._current = next
  next.once('end', this._next.bind(this))
  next.pipe(this)
}

SeriesStream.prototype.end = function () {
  if (this._current) return // Only end when all streams have ended
  return PassThrough.prototype.end.apply(this, arguments)
}

module.exports = function (opts) {
  return new SeriesStream(opts)
}

module.exports.SeriesStream = SeriesStream
