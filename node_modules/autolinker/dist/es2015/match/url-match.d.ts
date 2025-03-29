import { Match, MatchConfig } from './match';
import { StripPrefixConfigObj, UrlMatchTypeOptions } from '../autolinker';
/**
 * @class Autolinker.match.Url
 * @extends Autolinker.match.Match
 *
 * Represents a Url match found in an input string which should be Autolinked.
 *
 * See this class's superclass ({@link Autolinker.match.Match}) for more details.
 */
export declare class UrlMatch extends Match {
    /**
     * @cfg {String} url (required)
     *
     * The url that was matched.
     */
    private url;
    /**
     * @cfg {"scheme"/"www"/"tld"} urlMatchType (required)
     *
     * The type of URL match that this class represents. This helps to determine
     * if the match was made in the original text with a prefixed scheme (ex:
     * 'http://www.google.com'), a prefixed 'www' (ex: 'www.google.com'), or
     * was matched by a known top-level domain (ex: 'google.com').
     */
    private readonly urlMatchType;
    /**
     * @cfg {Boolean} protocolUrlMatch (required)
     *
     * `true` if the URL is a match which already has a protocol (i.e.
     * 'http://'), `false` if the match was from a 'www' or known TLD match.
     */
    private readonly protocolUrlMatch;
    /**
     * @cfg {Boolean} protocolRelativeMatch (required)
     *
     * `true` if the URL is a protocol-relative match. A protocol-relative match
     * is a URL that starts with '//', and will be either http:// or https://
     * based on the protocol that the site is loaded under.
     */
    private readonly protocolRelativeMatch;
    /**
     * @cfg {Object} stripPrefix (required)
     *
     * The Object form of {@link Autolinker#cfg-stripPrefix}.
     */
    private readonly stripPrefix;
    /**
     * @cfg {Boolean} stripTrailingSlash (required)
     * @inheritdoc Autolinker#cfg-stripTrailingSlash
     */
    private readonly stripTrailingSlash;
    /**
     * @cfg {Boolean} decodePercentEncoding (required)
     * @inheritdoc Autolinker#cfg-decodePercentEncoding
     */
    private readonly decodePercentEncoding;
    /**
     * @private
     * @property {RegExp} schemePrefixRegex
     *
     * A regular expression used to remove the 'http://' or 'https://' from
     * URLs.
     */
    schemePrefixRegex: RegExp;
    /**
     * @private
     * @property {RegExp} wwwPrefixRegex
     *
     * A regular expression used to remove the 'www.' from URLs.
     */
    wwwPrefixRegex: RegExp;
    /**
     * @private
     * @property {RegExp} protocolRelativeRegex
     *
     * The regular expression used to remove the protocol-relative '//' from the {@link #url} string, for purposes
     * of {@link #getAnchorText}. A protocol-relative URL is, for example, "//yahoo.com"
     */
    protocolRelativeRegex: RegExp;
    /**
     * @private
     * @property {Boolean} protocolPrepended
     *
     * Will be set to `true` if the 'http://' protocol has been prepended to the {@link #url} (because the
     * {@link #url} did not have a protocol)
     */
    protocolPrepended: boolean;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match
     *   instance, specified in an Object (map).
     */
    constructor(cfg: UrlMatchConfig);
    /**
     * Returns a string name for the type of match that this class represents.
     * For the case of UrlMatch, returns 'url'.
     *
     * @return {String}
     */
    getType(): string;
    /**
     * Returns a string name for the type of URL match that this class
     * represents.
     *
     * This helps to determine if the match was made in the original text with a
     * prefixed scheme (ex: 'http://www.google.com'), a prefixed 'www' (ex:
     * 'www.google.com'), or was matched by a known top-level domain (ex:
     * 'google.com').
     *
     * @return {"scheme"/"www"/"tld"}
     */
    getUrlMatchType(): UrlMatchTypeOptions;
    /**
     * Returns the url that was matched, assuming the protocol to be 'http://' if the original
     * match was missing a protocol.
     *
     * @return {String}
     */
    getUrl(): string;
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
    /**
     * Strips the scheme prefix (such as "http://" or "https://") from the given
     * `url`.
     *
     * @private
     * @param {String} url The text of the anchor that is being generated, for
     *   which to strip off the url scheme.
     * @return {String} The `url`, with the scheme stripped.
     */
    private stripSchemePrefix;
    /**
     * Strips the 'www' prefix from the given `url`.
     *
     * @private
     * @param {String} url The text of the anchor that is being generated, for
     *   which to strip off the 'www' if it exists.
     * @return {String} The `url`, with the 'www' stripped.
     */
    private stripWwwPrefix;
    /**
     * Strips any protocol-relative '//' from the anchor text.
     *
     * @private
     * @param {String} text The text of the anchor that is being generated, for which to strip off the
     *   protocol-relative prefix (such as stripping off "//")
     * @return {String} The `anchorText`, with the protocol-relative prefix stripped.
     */
    private stripProtocolRelativePrefix;
    /**
     * Removes any trailing slash from the given `anchorText`, in preparation for the text to be displayed.
     *
     * @private
     * @param {String} anchorText The text of the anchor that is being generated, for which to remove any trailing
     *   slash ('/') that may exist.
     * @return {String} The `anchorText`, with the trailing slash removed.
     */
    private removeTrailingSlash;
    /**
     * Decodes percent-encoded characters from the given `anchorText`, in
     * preparation for the text to be displayed.
     *
     * @private
     * @param {String} anchorText The text of the anchor that is being
     *   generated, for which to decode any percent-encoded characters.
     * @return {String} The `anchorText`, with the percent-encoded characters
     *   decoded.
     */
    private removePercentEncoding;
}
export interface UrlMatchConfig extends MatchConfig {
    url: string;
    urlMatchType: UrlMatchTypeOptions;
    protocolUrlMatch: boolean;
    protocolRelativeMatch: boolean;
    stripPrefix: Required<StripPrefixConfigObj>;
    stripTrailingSlash: boolean;
    decodePercentEncoding: boolean;
}
