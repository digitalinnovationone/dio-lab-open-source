/**
 * Regular expression to match upper and lowercase ASCII letters
 */
export declare const letterRe: RegExp;
/**
 * Regular expression to match ASCII digits
 */
export declare const digitRe: RegExp;
/**
 * Regular expression to match everything *except* ASCII digits
 */
export declare const nonDigitRe: RegExp;
/**
 * Regular expression to match whitespace
 */
export declare const whitespaceRe: RegExp;
/**
 * Regular expression to match quote characters
 */
export declare const quoteRe: RegExp;
/**
 * Regular expression to match the range of ASCII control characters (0-31), and
 * the backspace char (127)
 */
export declare const controlCharsRe: RegExp;
/**
 * The string form of a regular expression that would match all of the
 * alphabetic ("letter") chars in the unicode character set when placed in a
 * RegExp character class (`[]`). This includes all international alphabetic
 * characters.
 *
 * These would be the characters matched by unicode regex engines `\p{L}`
 * escape ("all letters").
 *
 * Taken from the XRegExp library: http://xregexp.com/ (thanks @https://github.com/slevithan)
 * Specifically: http://xregexp.com/v/3.2.0/xregexp-all.js, the 'Letter'
 *   regex's bmp
 *
 * VERY IMPORTANT: This set of characters is defined inside of a Regular
 *   Expression literal rather than a string literal to prevent UglifyJS from
 *   compressing the unicode escape sequences into their actual unicode
 *   characters. If Uglify compresses these into the unicode characters
 *   themselves, this results in the error "Range out of order in character
 *   class" when these characters are used inside of a Regular Expression
 *   character class (`[]`). See usages of this const. Alternatively, we can set
 *   the UglifyJS option `ascii_only` to true for the build, but that doesn't
 *   help others who are pulling in Autolinker into their own build and running
 *   UglifyJS themselves.
 */
export declare const alphaCharsStr: string;
/**
 * The string form of a regular expression that would match all emoji characters
 * Based on the emoji regex defined in this article: https://thekevinscott.com/emojis-in-javascript/
 */
export declare const emojiStr: string;
/**
 * The string form of a regular expression that would match all of the
 * combining mark characters in the unicode character set when placed in a
 * RegExp character class (`[]`).
 *
 * These would be the characters matched by unicode regex engines `\p{M}`
 * escape ("all marks").
 *
 * Taken from the XRegExp library: http://xregexp.com/ (thanks @https://github.com/slevithan)
 * Specifically: http://xregexp.com/v/3.2.0/xregexp-all.js, the 'Mark'
 *   regex's bmp
 *
 * VERY IMPORTANT: This set of characters is defined inside of a Regular
 *   Expression literal rather than a string literal to prevent UglifyJS from
 *   compressing the unicode escape sequences into their actual unicode
 *   characters. If Uglify compresses these into the unicode characters
 *   themselves, this results in the error "Range out of order in character
 *   class" when these characters are used inside of a Regular Expression
 *   character class (`[]`). See usages of this const. Alternatively, we can set
 *   the UglifyJS option `ascii_only` to true for the build, but that doesn't
 *   help others who are pulling in Autolinker into their own build and running
 *   UglifyJS themselves.
 */
export declare const marksStr: string;
/**
 * The string form of a regular expression that would match all of the
 * alphabetic ("letter") chars, emoji, and combining marks in the unicode character set
 * when placed in a RegExp character class (`[]`). This includes all
 * international alphabetic characters.
 *
 * These would be the characters matched by unicode regex engines `\p{L}\p{M}`
 * escapes and emoji characters.
 */
export declare const alphaCharsAndMarksStr: string;
/**
 * The string form of a regular expression that would match all of the
 * decimal number chars in the unicode character set when placed in a RegExp
 * character class (`[]`).
 *
 * These would be the characters matched by unicode regex engines `\p{Nd}`
 * escape ("all decimal numbers")
 *
 * Taken from the XRegExp library: http://xregexp.com/ (thanks @https://github.com/slevithan)
 * Specifically: http://xregexp.com/v/3.2.0/xregexp-all.js, the 'Decimal_Number'
 *   regex's bmp
 *
 * VERY IMPORTANT: This set of characters is defined inside of a Regular
 *   Expression literal rather than a string literal to prevent UglifyJS from
 *   compressing the unicode escape sequences into their actual unicode
 *   characters. If Uglify compresses these into the unicode characters
 *   themselves, this results in the error "Range out of order in character
 *   class" when these characters are used inside of a Regular Expression
 *   character class (`[]`). See usages of this const. Alternatively, we can set
 *   the UglifyJS option `ascii_only` to true for the build, but that doesn't
 *   help others who are pulling in Autolinker into their own build and running
 *   UglifyJS themselves.
 */
export declare const decimalNumbersStr: string;
/**
 * The string form of a regular expression that would match all of the
 * letters and decimal number chars in the unicode character set when placed in
 * a RegExp character class (`[]`).
 *
 * These would be the characters matched by unicode regex engines
 * `[\p{L}\p{Nd}]` escape ("all letters and decimal numbers")
 */
export declare const alphaNumericCharsStr: string;
/**
 * The string form of a regular expression that would match all of the
 * letters, combining marks, and decimal number chars in the unicode character
 * set when placed in a RegExp character class (`[]`).
 *
 * These would be the characters matched by unicode regex engines
 * `[\p{L}\p{M}\p{Nd}]` escape ("all letters, combining marks, and decimal
 * numbers")
 */
export declare const alphaNumericAndMarksCharsStr: string;
/**
 * The regular expression that will match a single letter of the
 * {@link #alphaNumericAndMarksCharsStr}.
 */
export declare const alphaNumericAndMarksCharRe: RegExp;
/**
 * A function to match domain names of a URL or email address.
 * Ex: 'google', 'yahoo', 'some-other-company', etc.
 */
export declare const getDomainNameStr: (group: number) => string;
/**
 * A regular expression to match domain names of a URL or email address.
 * Ex: 'google', 'yahoo', 'some-other-company', etc.
 */
export declare const domainNameRegex: RegExp;
/**
 * A regular expression that is simply the character class of the characters
 * that may be used in a domain name, minus the '-' or '.'
 */
export declare const domainNameCharRegex: RegExp;
