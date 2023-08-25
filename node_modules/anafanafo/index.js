'use strict'

const { createConsumer } = require('char-width-table-consumer')

const consumers = {
  '10px Verdana': createConsumer(require('./data/verdana-10px-normal.json')),
  'bold 10px Verdana': createConsumer(require('./data/verdana-10px-bold.json')),
  '11px Verdana': createConsumer(require('./data/verdana-11px-normal.json')),
  'bold 11px Helvetica': createConsumer(
    require('./data/helvetica-11px-bold.json')
  ),
}

module.exports = function measure(text, { font, ...rest }) {
  const consumer = consumers[font]
  if (!consumer) {
    throw Error(
      `Unknown font "${font}", expected ${Object.keys(consumers).join(', ')}`
    )
  }
  return consumer.widthOf(text, { ...rest })
}
