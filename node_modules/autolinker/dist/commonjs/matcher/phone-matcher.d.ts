import { Matcher } from './matcher';
import { Match } from '../match/match';
/**
 * @class Autolinker.matcher.Phone
 * @extends Autolinker.matcher.Matcher
 *
 * Matcher to find Phone number matches in an input string.
 *
 * See this class's superclass ({@link Autolinker.matcher.Matcher}) for more
 * details.
 */
export declare class PhoneMatcher extends Matcher {
    /**
     * The regular expression to match Phone numbers. Example matches:
     *
     *     (123) 456-7890
     *     123 456 7890
     *     123-456-7890
     *     +18004441234,,;,10226420346#
     *     +1 (800) 444 1234
     *     10226420346#
     *     1-800-444-1234,1022,64,20346#
     *
     * This regular expression has the following capturing groups:
     *
     * 1 or 2. The prefixed '+' sign, if there is one.
     *
     * @protected
     * @property {RegExp} matcherRegex
     */
    protected matcherRegex: RegExp;
    /**
     * @inheritdoc
     */
    parseMatches(text: string): Match[];
    protected testMatch(text: string): boolean;
}
