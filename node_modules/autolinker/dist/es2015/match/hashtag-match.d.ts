import { Match, MatchConfig } from './match';
/**
 * @class Autolinker.match.Hashtag
 * @extends Autolinker.match.Match
 *
 * Represents a Hashtag match found in an input string which should be
 * Autolinked.
 *
 * See this class's superclass ({@link Autolinker.match.Match}) for more
 * details.
 */
export declare class HashtagMatch extends Match {
    /**
     * @cfg {String} serviceName
     *
     * The service to point hashtag matches to. See {@link Autolinker#hashtag}
     * for available values.
     */
    private readonly serviceName;
    /**
     * @cfg {String} hashtag (required)
     *
     * The HashtagMatch that was matched, without the '#'.
     */
    private readonly hashtag;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match
     *   instance, specified in an Object (map).
     */
    constructor(cfg: HashtagMatchConfig);
    /**
     * Returns a string name for the type of match that this class represents.
     * For the case of HashtagMatch, returns 'hashtag'.
     *
     * @return {String}
     */
    getType(): string;
    /**
     * Returns the configured {@link #serviceName} to point the HashtagMatch to.
     * Ex: 'facebook', 'twitter'.
     *
     * @return {String}
     */
    getServiceName(): string;
    /**
     * Returns the matched hashtag, without the '#' character.
     *
     * @return {String}
     */
    getHashtag(): string;
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
export interface HashtagMatchConfig extends MatchConfig {
    serviceName: string;
    hashtag: string;
}
