import { Matcher, MatcherConfig } from './matcher';
import { MentionServices } from '../autolinker';
import { Match } from '../match/match';
/**
 * @class Autolinker.matcher.Mention
 * @extends Autolinker.matcher.Matcher
 *
 * Matcher to find/replace username matches in an input string.
 */
export declare class MentionMatcher extends Matcher {
    /**
     * @cfg {'twitter'/'instagram'/'soundcloud'} protected
     *
     * The name of service to link @mentions to.
     *
     * Valid values are: 'twitter', 'instagram', 'soundcloud', or 'tiktok'
     */
    protected serviceName: MentionServices;
    /**
     * Hash of regular expression to match username handles. Example match:
     *
     *     @asdf
     *
     * @private
     * @property {Object} matcherRegexes
     */
    protected readonly matcherRegexes: {
        [key: string]: RegExp;
    };
    /**
     * The regular expression to use to check the character before a username match to
     * make sure we didn't accidentally match an email address.
     *
     * For example, the string "asdf@asdf.com" should not match "@asdf" as a username.
     *
     * @private
     * @property {RegExp} nonWordCharRegex
     */
    protected readonly nonWordCharRegex: RegExp;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match instance,
     *   specified in an Object (map).
     */
    constructor(cfg: MentionMatcherConfig);
    /**
     * @inheritdoc
     */
    parseMatches(text: string): Match[];
}
export interface MentionMatcherConfig extends MatcherConfig {
    serviceName: MentionServices;
}
