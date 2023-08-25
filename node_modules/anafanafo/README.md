# anafanafo

[![version](https://img.shields.io/npm/v/anafanafo?style=flat-square)][npm]
[![license](https://img.shields.io/npm/l/anafanafo?style=flat-square)][npm]
[![build](https://img.shields.io/circleci/project/github/metabolize/anafanafo/main?style=flat-square)][build]
[![bundle size](https://img.shields.io/bundlephobia/minzip/anafanafo?style=flat-square)][bundlephobia]
[![code style](https://img.shields.io/badge/code_style-prettier-ff69b4?style=flat-square)][prettier]
[![lerna](https://img.shields.io/badge/maintained%20with-lerna-cc00ff?style=flat-square)][lerna]

[npm]: https://npmjs.com/anafanafo
[build]: https://circleci.com/gh/metabolize/anafanafo/tree/main
[bundlephobia]: https://bundlephobia.com/result?p=anafanafo
[prettier]: https://prettier.io/
[lerna]: https://lernajs.io/

Efficiently compute text width in Verdana and Helvetica using
[char-width-table-consumer][] and lookup tables.

Built with [Shields][] in mind.

(And because Verdana always makes me think of [this][the name game].)

[char-width-table-consumer]: https://www.npmjs.com/package/char-width-table-consumer
[shields]: https://github.com/badges/shields/
[the name game]: https://www.youtube.com/watch?v=5MJLi5_dyn0

## Usage

```js
const anafanafo = require('anafanafo')

// Supports '11px Verdana', '10px Verdana', 'bold 10px Verdana', and 'bold 11px Helvetica'.
const width = anafanafo('Shirley Shirley', { font: '11px Verdana' })
```

## License

All rights to Verdana are owned by Microsoft Corp.

The remainder of this project is licensed under the MIT license.
