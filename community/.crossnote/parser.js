({
  onWillParseMarkdown: async function(markdown) {
    return markdown;
  },

  onDidParseMarkdown: async function(html) {
    return html;
  },
  
  onWillTransformMarkdown: async function(markdown) {
    return markdown;
  },
  
  onDidTransformMarkdown: async function(markdown) {
    return markdown;
  },

  processWikiLink: function({text, link}) {
    return { 
      text,  
      link: link ? link : text.endsWith('.md') ? text : `${text}.md`,
    };
  }
})