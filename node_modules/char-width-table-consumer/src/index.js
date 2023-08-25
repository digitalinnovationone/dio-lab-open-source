'use strict'

const CharWidthTableConsumer = require('./consumer')

const {
  create: createConsumer,
  load: loadConsumer,
  loadSync: loadConsumerSync,
} = CharWidthTableConsumer

module.exports = {
  createConsumer,
  loadConsumer,
  loadConsumerSync,
  CharWidthTableConsumer,
}
