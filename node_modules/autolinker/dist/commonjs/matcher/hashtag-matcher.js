"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.hashtagServices = exports.HashtagMatcher = void 0;
var tslib_1 = require("tslib");
var matcher_1 = require("./matcher");
var regex_lib_1 = require("../regex-lib");
var hashtag_match_1 = require("../match/hashtag-match");
var utils_1 = require("../utils");
// For debugging: search for other "For debugging" lines
// import CliTable from 'cli-table';
var hashtagTextCharRe = new RegExp("[_".concat(regex_lib_1.alphaNumericAndMarksCharsStr, "]"));
/**
 * @class Autolinker.matcher.Hashtag
 * @extends Autolinker.matcher.Matcher
 *
 * Matcher to find HashtagMatch matches in an input string.
 */
var HashtagMatcher = /** @class */ (function (_super) {
    (0, tslib_1.__extends)(HashtagMatcher, _super);
    /**
     * @method constructor
     * @param {Object} cfg The configuration properties for the Match instance,
     *   specified in an Object (map).
     */
    function HashtagMatcher(cfg) {
        var _this = _super.call(this, cfg) || this;
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
        _this.serviceName = 'twitter'; // default value just to get the above doc comment in the ES5 output and documentation generator
        _this.serviceName = cfg.serviceName;
        return _this;
    }
    /**
     * @inheritdoc
     */
    HashtagMatcher.prototype.parseMatches = function (text) {
        var tagBuilder = this.tagBuilder;
        var serviceName = this.serviceName;
        var matches = [];
        var len = text.length;
        var charIdx = 0, hashCharIdx = -1, state = 0 /* None */;
        // For debugging: search for other "For debugging" lines
        // const table = new CliTable( {
        // 	head: [ 'charIdx', 'char', 'state', 'charIdx', 'currentEmailAddress.idx', 'hasDomainDot' ]
        // } );
        while (charIdx < len) {
            var char = text.charAt(charIdx);
            // For debugging: search for other "For debugging" lines
            // table.push(
            // 	[ charIdx, char, State[ state ], charIdx, currentEmailAddress.idx, currentEmailAddress.hasDomainDot ]
            // );
            switch (state) {
                case 0 /* None */:
                    stateNone(char);
                    break;
                case 1 /* NonHashtagWordChar */:
                    stateNonHashtagWordChar(char);
                    break;
                case 2 /* HashtagHashChar */:
                    stateHashtagHashChar(char);
                    break;
                case 3 /* HashtagTextChar */:
                    stateHashtagTextChar(char);
                    break;
                default:
                    (0, utils_1.throwUnhandledCaseError)(state);
            }
            // For debugging: search for other "For debugging" lines
            // table.push(
            // 	[ charIdx, char, State[ state ], charIdx, currentEmailAddress.idx, currentEmailAddress.hasDomainDot ]
            // );
            charIdx++;
        }
        // Capture any valid match at the end of the string
        captureMatchIfValid();
        // For debugging: search for other "For debugging" lines
        //console.log( '\n' + table.toString() );
        return matches;
        // Handles the state when we're not in a hashtag or any word
        function stateNone(char) {
            if (char === '#') {
                state = 2 /* HashtagHashChar */;
                hashCharIdx = charIdx;
            }
            else if (regex_lib_1.alphaNumericAndMarksCharRe.test(char)) {
                state = 1 /* NonHashtagWordChar */;
            }
            else {
                // not a hashtag character ('#') or word char, stay in State.None
            }
        }
        // Handles the state when we've encountered a word character but are not
        // in a hashtag. This is used to distinguish between a standalone
        // hashtag such as '#Stuff' vs a hash char that is part of a word like
        // 'asdf#stuff' (the latter of which would not be a match)
        function stateNonHashtagWordChar(char) {
            if (regex_lib_1.alphaNumericAndMarksCharRe.test(char)) {
                // continue in NonHashtagWordChar state
            }
            else {
                state = 0 /* None */;
            }
        }
        // Handles the state when we've just encountered a '#' character
        function stateHashtagHashChar(char) {
            if (hashtagTextCharRe.test(char)) {
                // '#' char with valid hash text char following
                state = 3 /* HashtagTextChar */;
            }
            else if (regex_lib_1.alphaNumericAndMarksCharRe.test(char)) {
                state = 1 /* NonHashtagWordChar */;
            }
            else {
                state = 0 /* None */;
            }
        }
        // Handles the state when we're currently in the hash tag's text chars
        function stateHashtagTextChar(char) {
            if (hashtagTextCharRe.test(char)) {
                // Continue reading characters in the HashtagText state
            }
            else {
                captureMatchIfValid();
                hashCharIdx = -1;
                if (regex_lib_1.alphaNumericAndMarksCharRe.test(char)) {
                    state = 1 /* NonHashtagWordChar */;
                }
                else {
                    state = 0 /* None */;
                }
            }
        }
        /*
         * Captures the current hashtag as a HashtagMatch if it's valid.
         */
        function captureMatchIfValid() {
            if (hashCharIdx > -1 && charIdx - hashCharIdx <= 140) {
                // Max length of 140 for a hashtag ('#' char + 139 word chars)
                var matchedText = text.slice(hashCharIdx, charIdx);
                var match = new hashtag_match_1.HashtagMatch({
                    tagBuilder: tagBuilder,
                    matchedText: matchedText,
                    offset: hashCharIdx,
                    serviceName: serviceName,
                    hashtag: matchedText.slice(1),
                });
                matches.push(match);
            }
        }
    };
    return HashtagMatcher;
}(matcher_1.Matcher));
exports.HashtagMatcher = HashtagMatcher;
exports.hashtagServices = ['twitter', 'facebook', 'instagram', 'tiktok'];
//# sourceMappingURL=hashtag-matcher.js.map