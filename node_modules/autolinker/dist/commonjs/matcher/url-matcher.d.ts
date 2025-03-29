import { Matcher, MatcherConfig } from './matcher';
import { StripPrefixConfigObj } from '../autolinker';
import { Match } from '../match/match';
/**
 * @class Autolinker.matcher.Url
 * @extends Autolinker.matcher.Matcher
 *
 * Matcher to find URL matches in an input string.
 *
 * See this class's superclass ({@link Autolinker.matcher.Matcher}) for more details.
 */
export declare class UrlMatcher extends Matcher {
    /**
     * @cfg {Object} stripPrefix (required)
     *
     * The Object form of {@link Autolinker#cfg-stripPrefix}.
     */
    protected stripPrefix: Required<StripPrefixConfigObj>;
    /**
     * @cfg {Boolean} stripTrailingSlash (required)
     * @inheritdoc Autolinker#stripTrailingSlash
     */
    protected stripTrailingSlash: boolean;
    /**
     * @cfg {Boolean} decodePercentEncoding (required)
     * @inheritdoc Autolinker#decodePercentEncoding
     */
    protected decodePercentEncoding: boolean;
    /**
     * @protected
     * @property {RegExp} matcherRegex
     *
     * The regular expression to match URLs with an optional scheme, port
     * number, path, query string, and hash anchor.
     *
     * Example matches:
     *
     *     http://google.com
     *     www.google.com
     *     google.com/path/to/file?q1=1&q2=2#myAnchor
     *
     *
     * This regular expression will have the following capturing groups:
     *
     * 1.  Group that matches a scheme-prefixed URL (i.e. 'http://google.com').
     *     This is used to match scheme URLs with just a single word, such as
     *     'http://localhost', where we won't double check that the domain name
     *     has at least one dot ('.') in it.
     * 2.  Group that matches a 'www.' prefixed URL. This is only matched if the
     *     'www.' text was not prefixed by a scheme (i.e.: not prefixed by
     *     'http://', 'ftp:', etc.)
     * 3.  A protocol-relative ('//') match for the case of a 'www.' prefixed
     *     URL. Will be an empty string if it is not a protocol-relative match.
     *     We need to know the character before the '//' in order to determine
     *     if it is a valid match or the // was in a string we don't want to
     *     auto-link.
     * 4.  Group that matches a known TLD (top level domain), when a scheme
     *     or 'www.'-prefixed domain is not matched.
     * 5.  A protocol-relative ('//') match for the case of a known TLD prefixed
     *     URL. Will be an empty string if it is not a protocol-relative match.
     *     See #3 for more info.
     */
    protected matcherRegex: RegExp;
    /**
     * A regular expression to use to check the character before a protocol-relative
     * URL match. We don't want to match a protocol-relative URL if it is part
     * of another word.
     *
     * For example, we want to match something like "Go to: //google.com",
     * but we don't want to match something like "abc//google.com"
     *
     * This regular expression is used to test the character before the '//'.
     *
     * @protected
     * @type {RegExp} wordCharRegExp
     */
    protected wordCharRegExp: RegExp;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match instance,
     *   specified in an Object (map).
     */
    constructor(cfg: UrlMatcherConfig);
    /**
     * @inheritdoc
     */
    parseMatches(text: string): Match[];
    /**
     * Determines if a match found has an unmatched closing parenthesis,
     * square bracket or curly bracket. If so, the symbol will be removed
     * from the match itself, and appended after the generated anchor tag.
     *
     * A match may have an extra closing parenthesis at the end of the match
     * because the regular expression must include parenthesis for URLs such as
     * "wikipedia.com/something_(disambiguation)", which should be auto-linked.
     *
     * However, an extra parenthesis *will* be included when the URL itself is
     * wrapped in parenthesis, such as in the case of:
     *     "(wikipedia.com/something_(disambiguation))"
     * In this case, the last closing parenthesis should *not* be part of the
     * URL itself, and this method will return `true`.
     *
     * For square brackets in URLs such as in PHP arrays, the same behavior as
     * parenthesis discussed above should happen:
     *     "[http://www.example.com/foo.php?bar[]=1&bar[]=2&bar[]=3]"
     * The closing square bracket should not be part of the URL itself, and this
     * method will return `true`.
     *
     * @protected
     * @param {String} matchStr The full match string from the {@link #matcherRegex}.
     * @return {Boolean} `true` if there is an unbalanced closing parenthesis or
     *   square bracket at the end of the `matchStr`, `false` otherwise.
     */
    protected matchHasUnbalancedClosingParen(matchStr: string): boolean;
    /**
     * Determine if there's an invalid character after the TLD in a URL. Valid
     * characters after TLD are ':/?#'. Exclude scheme matched URLs from this
     * check.
     *
     * @protected
     * @param {String} urlMatch The matched URL, if there was one. Will be an
     *   empty string if the match is not a URL match.
     * @param {String} schemeUrlMatch The match URL string for a scheme
     *   match. Ex: 'http://yahoo.com'. This is used to match something like
     *   'http://localhost', where we won't double check that the domain name
     *   has at least one '.' in it.
     * @return {Number} the position where the invalid character was found. If
     *   no such character was found, returns -1
     */
    protected matchHasInvalidCharAfterTld(urlMatch: string, schemeUrlMatch: string): number;
}
export interface UrlMatcherConfig extends MatcherConfig {
    stripPrefix: Required<StripPrefixConfigObj>;
    stripTrailingSlash: boolean;
    decodePercentEncoding: boolean;
}
