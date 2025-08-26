# series-stream [![Build Status](https://travis-ci.org/alanshaw/series-stream.svg?branch=master)](https://travis-ci.org/alanshaw/series-stream)

Pipe multiple streams into a single stream, ensuring each added stream finishes piping it's data before the next begins.

## Example

```js
var fs = require('fs')
var createSeriesStream = require('series-stream')

var ss = createSeriesStream()

var file1 = '/path/to/file1'
var file2 = '/path/to/file2'
var file3 = '/path/to/file3'
var outfile = '/path/to/outfile'

// Add streams in the order you want them to pipe out
ss.add(fs.createReadStream(file3))
ss.add(fs.createReadStream(file1))
ss.add(fs.createReadStream(file2))

ss.pipe(fs.createWriteStream(outfile))
// Outfile now contains the contents of file 3, 1 and 2 in that order
```
