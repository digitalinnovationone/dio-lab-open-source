'use strict'

const fs = require('fs')
const bs = require('binary-search')
const { promisify } = require('util')
const readFile = promisify(fs.readFile)

module.exports = class CharWidthTableConsumer {
  constructor(data) {
    this.data = data
    this.emWidth = this.widthOf('m')
  }

  static create(data) {
    return new CharWidthTableConsumer(data)
  }

  static async load(path) {
    const json = await readFile(path)
    const data = JSON.parse(json)
    return new CharWidthTableConsumer(data)
  }

  static loadSync(path) {
    const json = fs.readFileSync(path)
    const data = JSON.parse(json)
    return new CharWidthTableConsumer(data)
  }

  static isControlChar(charCode) {
    return charCode <= 31 || charCode === 127
  }

  widthOfCharCode(charCode) {
    if (this.constructor.isControlChar(charCode)) {
      return 0.0
    }

    // https://github.com/darkskyapp/binary-search/pull/18
    const index = bs(this.data, charCode, ([lower], needle) => lower - needle)
    if (index >= 0) {
      // The index matches the beginning of a range.
      const [, , width] = this.data[index]
      return width
    } else {
      // The index does not match the beginning of a range, which means it
      // should be in the preceeding range A return value of `-x` means the
      // needle would be at `x - 1`, and we want to check the element before
      // that.
      const candidateIndex = -index - 2
      const [lower, upper, width] = this.data[candidateIndex]
      if (charCode >= lower && charCode <= upper) {
        return width
      } else {
        return undefined
      }
    }
  }

  widthOf(text, { guess = true } = {}) {
    // Array.from() will split a string into an array of strings, each of
    // which contains a single code point.
    // https://stackoverflow.com/a/42596897/893113
    return Array.from(text).reduce((accumWidth, char) => {
      const charWidth = this.widthOfCharCode(char.codePointAt(0))
      if (charWidth === undefined) {
        if (guess) {
          return accumWidth + this.emWidth
        } else {
          throw Error(
            `No width available for character code ${char.codePointAt(0)}`
          )
        }
      } else {
        return accumWidth + charWidth
      }
    }, 0.0)
  }
}
