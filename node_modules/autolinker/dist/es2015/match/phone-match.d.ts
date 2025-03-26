import { Match, MatchConfig } from './match';
/**
 * @class Autolinker.match.Phone
 * @extends Autolinker.match.Match
 *
 * Represents a Phone number match found in an input string which should be
 * Autolinked.
 *
 * See this class's superclass ({@link Autolinker.match.Match}) for more
 * details.
 */
export declare class PhoneMatch extends Match {
    /**
     * @protected
     * @property {String} number (required)
     *
     * The phone number that was matched, without any delimiter characters.
     *
     * Note: This is a string to allow for prefixed 0's.
     */
    private readonly number;
    /**
     * @protected
     * @property  {Boolean} plusSign (required)
     *
     * `true` if the matched phone number started with a '+' sign. We'll include
     * it in the `tel:` URL if so, as this is needed for international numbers.
     *
     * Ex: '+1 (123) 456 7879'
     */
    private readonly plusSign;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match
     *   instance, specified in an Object (map).
     */
    constructor(cfg: PhoneMatchConfig);
    /**
     * Returns a string name for the type of match that this class represents.
     * For the case of PhoneMatch, returns 'phone'.
     *
     * @return {String}
     */
    getType(): string;
    /**
     * Returns the phone number that was matched as a string, without any
     * delimiter characters.
     *
     * Note: This is a string to allow for prefixed 0's.
     *
     * @return {String}
     */
    getPhoneNumber(): string;
    /**
     * Alias of {@link #getPhoneNumber}, returns the phone number that was
     * matched as a string, without any delimiter characters.
     *
     * Note: This is a string to allow for prefixed 0's.
     *
     * @return {String}
     */
    getNumber(): string;
    /**
     * Returns the anchor href that should be generated for the match.
     *
     * @return {String}
     */
    getAnchorHref(): string;
    /**
     * Returns the anchor text that should be generated for the match.
     *
     * @return {String}
     */
    getAnchorText(): string;
}
export interface PhoneMatchConfig extends MatchConfig {
    number: string;
    plusSign: boolean;
}
