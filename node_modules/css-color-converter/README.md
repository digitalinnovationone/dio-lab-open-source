# css-color-converter [![Build Status][ci-img]][ci]

Converts CSS colors from one representation to another 

[ci-img]:  https://travis-ci.org/andyjansson/css-color-converter.svg
[ci]:      https://travis-ci.org/andyjansson/css-color-converter

## Installation

```js
npm install css-color-converter
```

## Usage

**Example usage**: 
```js
import { fromString } from 'css-color-converter';

fromString('rgb(255, 255, 255)').toHslString(); // hsl(0, 0%, 100%)
fromString('rgba(255, 255, 255, 0.5)').toHslString(); // hsla(0, 0%, 100%, 0.5)
fromString('blue').toRgbString(); // rgb(0, 0, 255)
fromString('red').toHexString(); // #ff0000
```
## Functions

### `fromString(str)`
| parameter | type   | description                                    |
| --------- | ------ | ---------------------------------------------- |
| `str`     | string | Supports named colors, hex, rgb/rgba, hsl/hsla |

**Returns** [`instance`](#Methods) if valid, `null` if invalid.

### `fromRgb([r, g, b])`

| parameter | type   | description   |
| --------- | ------ | ------------- |
| `r`       | int    | red (0-255)   |
| `g`       | int    | green (0-255) |
| `b`       | int    | blue (0-255)  |

**Returns** [`instance`](#Methods)

### `fromRgba([r, g, b, a])`

| parameter | type   | description   |
| --------- | ------ | ------------- |
| `r`       | int    | red (0-255)   |
| `g`       | int    | green (0-255) |
| `b`       | int    | blue (0-255)  |
| `a`       | float  | alpha (0-1)   |

**Returns** [`instance`](#Methods)

### `fromHsl([h, s, l])`

| parameter | type   | description        |
| --------- | ------ | ------------------ |
| `h`       | int    | hue (0-360)        |
| `s`       | int    | saturation (0-100) |
| `l`       | int    | luminosity (0-100) |

**Returns** [`instance`](#Methods)

### `fromHsla([h, s, l, a])`

| parameter | type   | description        |
| --------- | ------ | ------------------ |
| `h`       | int    | hue (0-360)        |
| `s`       | int    | saturation (0-100) |
| `l`       | int    | luminosity (0-100) |
| `a`       | float  | alpha (0-1)        |

**Returns** [`instance`](#Methods)

## Methods

### `toRgbString()`

**Returns** `rgb()` or `rgba()`, depending on the alpha.

### `toHslString()`

**Returns** `hsl()` or `hsla()`, depending on the alpha.

### `toHexString()`

**Returns** 6-digit or 8-digit `hex`, depending on the alpha.

### `toRgbaArray()`

**Returns** `[r, g, b, a]` array.