/**
 * The subset of the parser states defined in https://www.w3.org/TR/html51/syntax.html
 * which are useful for Autolinker.
 */
export declare const enum State {
    Data = 0,
    TagOpen = 1,
    EndTagOpen = 2,
    TagName = 3,
    BeforeAttributeName = 4,
    AttributeName = 5,
    AfterAttributeName = 6,
    BeforeAttributeValue = 7,
    AttributeValueDoubleQuoted = 8,
    AttributeValueSingleQuoted = 9,
    AttributeValueUnquoted = 10,
    AfterAttributeValueQuoted = 11,
    SelfClosingStartTag = 12,
    MarkupDeclarationOpenState = 13,
    CommentStart = 14,
    CommentStartDash = 15,
    Comment = 16,
    CommentEndDash = 17,
    CommentEnd = 18,
    CommentEndBang = 19,
    Doctype = 20
}
