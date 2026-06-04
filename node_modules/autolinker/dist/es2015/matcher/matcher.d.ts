import { AnchorTagBuilder } from '../anchor-tag-builder';
import { Match } from '../match/match';
/**
 * @abstract
 * @class Autolinker.matcher.Matcher
 *
 * An abstract class and interface for individual matchers to find matches in
 * an input string with linkified versions of them.
 *
 * Note that Matchers do not take HTML into account - they must be fed the text
 * nodes of any HTML string, which is handled by {@link Autolinker#parse}.
 */
export declare abstract class Matcher {
    /**
     * @cfg {Autolinker.AnchorTagBuilder} tagBuilder (required)
     *
     * Reference to the AnchorTagBuilder instance to use to generate HTML tags
     * for {@link Autolinker.match.Match Matches}.
     */
    private __jsduckDummyDocProp;
    protected tagBuilder: AnchorTagBuilder;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Matcher
     *   instance, specified in an Object (map).
     */
    constructor(cfg: MatcherConfig);
    /**
     * Parses the input `text` and returns the array of {@link Autolinker.match.Match Matches}
     * for the matcher.
     *
     * @abstract
     * @param {String} text The text to scan and replace matches in.
     * @return {Autolinker.match.Match[]}
     */
    abstract parseMatches(text: string): Match[];
}
export interface MatcherConfig {
    tagBuilder: AnchorTagBuilder;
}
