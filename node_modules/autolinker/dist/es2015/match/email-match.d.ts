import { Match, MatchConfig } from './match';
/**
 * @class Autolinker.match.Email
 * @extends Autolinker.match.Match
 *
 * Represents a Email match found in an input string which should be Autolinked.
 *
 * See this class's superclass ({@link Autolinker.match.Match}) for more details.
 */
export declare class EmailMatch extends Match {
    /**
     * @cfg {String} email (required)
     *
     * The email address that was matched.
     */
    private readonly email;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match
     *   instance, specified in an Object (map).
     */
    constructor(cfg: EmailMatchConfig);
    /**
     * Returns a string name for the type of match that this class represents.
     * For the case of EmailMatch, returns 'email'.
     *
     * @return {String}
     */
    getType(): string;
    /**
     * Returns the email address that was matched.
     *
     * @return {String}
     */
    getEmail(): string;
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
export interface EmailMatchConfig extends MatchConfig {
    email: string;
}
