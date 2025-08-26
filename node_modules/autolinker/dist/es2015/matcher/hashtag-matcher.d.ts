import { Matcher, MatcherConfig } from './matcher';
import { Match } from '../match/match';
/**
 * @class Autolinker.matcher.Hashtag
 * @extends Autolinker.matcher.Matcher
 *
 * Matcher to find HashtagMatch matches in an input string.
 */
export declare class HashtagMatcher extends Matcher {
    /**
     * @cfg {String} service
     *
     * A string for the service name to have hashtags (ex: "#myHashtag")
     * auto-linked to. The currently-supported values are:
     *
     * - 'twitter'
     * - 'facebook'
     * - 'instagram'
     * - 'tiktok'
     */
    protected readonly serviceName: HashtagService;
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match instance,
     *   specified in an Object (map).
     */
    constructor(cfg: HashtagMatcherConfig);
    /**
     * @inheritdoc
     */
    parseMatches(text: string): Match[];
}
export interface HashtagMatcherConfig extends MatcherConfig {
    serviceName: HashtagService;
}
export declare type HashtagService = 'twitter' | 'facebook' | 'instagram' | 'tiktok';
export declare type HashtagServices = HashtagService;
export declare const hashtagServices: HashtagService[];
