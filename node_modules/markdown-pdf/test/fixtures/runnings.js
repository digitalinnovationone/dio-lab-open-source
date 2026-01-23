exports.header = {
  contents: function (pageNum, numPages) {
    return '<h1>Some Header <span style="float:right">' + pageNum + ' / ' + numPages + '</span></h1>'
  },
  height: '1cm'
}

exports.footer = {
  contents: function (pageNum, numPages) {
    return '<h1>Some Footer <span style="float:right">' + pageNum + ' / ' + numPages + '</span></h1>'
  },
  height: '1cm'
}
