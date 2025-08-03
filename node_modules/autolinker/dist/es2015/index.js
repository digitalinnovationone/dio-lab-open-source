// WARNING: This file is modified a bit when it is compiled into index.js in
// order to support nodejs interoperability with require('autolinker') directly.
// This is done by the buildSrcFixCommonJsIndexTask() function in the gulpfile.
// See that function for more details.
import Autolinker from './autolinker';
export default Autolinker;
export { Autolinker };
export * from './autolinker';
export * from './anchor-tag-builder';
export * from './html-tag';
export * from './match/index';
export * from './matcher/index';
//# sourceMappingURL=index.js.map