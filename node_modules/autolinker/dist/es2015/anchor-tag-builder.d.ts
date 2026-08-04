import { Match } from './match/match';
import { HtmlTag } from './html-tag';
import { TruncateConfigObj } from './autolinker';
/**
 * @protected
 * @class Autolinker.AnchorTagBuilder
 * @extends Object
 *
 * Builds anchor (&lt;a&gt;) tags for the Autolinker utility when a match is
 * found.
 *
 * Normally this class is instantiated, configured, and used internally by an
 * {@link Autolinker} instance, but may actually be used indirectly in a
 * {@link Autolinker#replaceFn replaceFn} to create {@link Autolinker.HtmlTag HtmlTag}
 * instances which may be modified before returning from the
 * {@link Autolinker#replaceFn replaceFn}. For example:
 *
 *     var html = Autolinker.link( "Test google.com", {
 *         replaceFn : function( match ) {
 *             var tag = match.buildTag();  // returns an {@link Autolinker.HtmlTag} instance
 *             tag.setAttr( 'rel', 'nofollow' );
 *
 *             return tag;
 *         }
 *     } );
 *
 *     // generated html:
 *     //   Test <a href="http://google.com" target="_blank" rel="nofollow">google.com</a>
 */
export declare class AnchorTagBuilder {
    /**
     * @cfg {Boolean} newWindow
     * @inheritdoc Autolinker#newWindow
     */
    private readonly newWindow;
    /**
     * @cfg {Object} truncate
     * @inheritdoc Autolinker#truncate
     */
    private readonly truncate;
    /**
     * @cfg {String} className
     * @inheritdoc Autolinker#className
     */
    private readonly className;
    /**
     * @method constructor
     * @param {Object} [cfg] The configuration options for the AnchorTagBuilder instance, specified in an Object (map).
     */
    constructor(cfg?: AnchorTagBuilderCfg);
    /**
     * Generates the actual anchor (&lt;a&gt;) tag to use in place of the
     * matched text, via its `match` object.
     *
     * @param {Autolinker.match.Match} match The Match instance to generate an
     *   anchor tag from.
     * @return {Autolinker.HtmlTag} The HtmlTag instance for the anchor tag.
     */
    build(match: Match): HtmlTag;
    /**
     * Creates the Object (map) of the HTML attributes for the anchor (&lt;a&gt;)
     *   tag being generated.
     *
     * @protected
     * @param {Autolinker.match.Match} match The Match instance to generate an
     *   anchor tag from.
     * @return {Object} A key/value Object (map) of the anchor tag's attributes.
     */
    protected createAttrs(match: Match): {
        [attrName: string]: string;
    };
    /**
     * Creates the CSS class that will be used for a given anchor tag, based on
     * the `matchType` and the {@link #className} config.
     *
     * Example returns:
     *
     * - ""                                      // no {@link #className}
     * - "myLink myLink-url"                     // url match
     * - "myLink myLink-email"                   // email match
     * - "myLink myLink-phone"                   // phone match
     * - "myLink myLink-hashtag"                 // hashtag match
     * - "myLink myLink-mention myLink-twitter"  // mention match with Twitter service
     *
     * @protected
     * @param {Autolinker.match.Match} match The Match instance to generate an
     *   anchor tag from.
     * @return {String} The CSS class string for the link. Example return:
     *   "myLink myLink-url". If no {@link #className} was configured, returns
     *   an empty string.
     */
    protected createCssClass(match: Match): string;
    /**
     * Processes the `anchorText` by truncating the text according to the
     * {@link #truncate} config.
     *
     * @private
     * @param {String} anchorText The anchor tag's text (i.e. what will be
     *   displayed).
     * @return {String} The processed `anchorText`.
     */
    private processAnchorText;
    /**
     * Performs the truncation of the `anchorText` based on the {@link #truncate}
     * option. If the `anchorText` is longer than the length specified by the
     * {@link #truncate} option, the truncation is performed based on the
     * `location` property. See {@link #truncate} for details.
     *
     * @private
     * @param {String} anchorText The anchor tag's text (i.e. what will be
     *   displayed).
     * @return {String} The truncated anchor text.
     */
    private doTruncate;
}
export interface AnchorTagBuilderCfg {
    newWindow?: boolean;
    truncate?: TruncateConfigObj;
    className?: string;
}
