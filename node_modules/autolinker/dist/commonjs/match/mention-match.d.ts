import { Match, MatchConfig } from './match';
import { MentionServices } from '../autolinker';
/**
 * @class Autolinker.match.Mention
 * @extends Autolinker.match.Match
 *
 * Represents a Mention match found in an input string which should be Autolinked.
 *
 * See this class's superclass ({@link Autolinker.match.Match}) for more details.
 */
export declare class MentionMatch extends Match {
    /**
     * @cfg {String} serviceName
     *
     * The service to point mention matches to. See {@link Autolinker#mention}
     * for available values.
     */
    private readonly serviceName;
    /**
     * @cfg {String} mention (required)
     *
     * The Mention that was matched, without the '@' character.
     */
    private readonly mention;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match
     *   instance, specified in an Object (map).
     */
    constructor(cfg: MentionMatchConfig);
    /**
     * Returns a string name for the type of match that this class represents.
     * For the case of MentionMatch, returns 'mention'.
     *
     * @return {String}
     */
    getType(): string;
    /**
     * Returns the mention, without the '@' character.
     *
     * @return {String}
     */
    getMention(): string;
    /**
     * Returns the configured {@link #serviceName} to point the mention to.
     * Ex: 'instagram', 'twitter', 'soundcloud'.
     *
     * @return {String}
     */
    getServiceName(): MentionServices;
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
     * Returns the CSS class suffixes that should be used on a tag built with
     * the match. See {@link Autolinker.match.Match#getCssClassSuffixes} for
     * details.
     *
     * @return {String[]}
     */
    getCssClassSuffixes(): string[];
}
export interface MentionMatchConfig extends MatchConfig {
    serviceName: MentionServices;
    mention: string;
}
