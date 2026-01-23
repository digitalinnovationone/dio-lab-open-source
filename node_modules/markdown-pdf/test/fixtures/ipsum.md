# A First Level Header
## A Second Level Header
### A Third Level Header
#### A Fourth Level Header
##### A Fifth Level Header
###### A Sixth Level Header 



This is a paragraph. Cupcake ipsum dolor sit amet. Tiramisu liquorice gummies powder. Biscuit pastry pastry cake candy gummies carrot cake gingerbread. Gummi bears tart cupcake bonbon sugar plum biscuit. Icing marzipan tootsie roll. Pie gingerbread dragée wypas cookie. Faworki bonbon topping sweet soufflé jelly. 

And another  paragraph. Jelly beans tootsie roll fruitcake toffee wypas chupa chups pudding. Soufflé muffin halvah powder sugar plum cake. Toffee cookie biscuit faworki pastry. Bonbon gummi bears topping caramels marshmallow. Chupa chups candy canes toffee. Powder powder candy canes pastry. Tootsie roll marshmallow powder.



*These words are emphasized*  
_Also these words are emphasized_

**These words are strong emphasized**  
__Also these words are strong emphasized__


> This is a very simple blockquote   



*   This
*   is
*   an 
*   unordered
*   list.

And...

1.  This
2.  is
3.  an
4.  ordered
5.  list.



[This is an example link](http://example.com/).   
[This is an example link with a title](http://example.com/ "¡Buenos días!").



This is a image    
![Alt](http://placehold.it/350x150 "I'm an image")



`this is a line of code`

    And these are several lines of code. Pudding sesame snaps cupcake bonbon cupcake. Icing macaroon donut. 
    
    More code. Donut cheesecake chocolate cake. Tart pudding wafer dessert chocolate bar jelly-o apple pie dessert. Carrot cake apple pie pie liquorice oat cake lollipop pastry caramels. Jelly-o sesame snaps gummi bears. 

    And more. Sugar plum lemon drops chupa chups chocolate pastry. Faworki applicake applicake brownie topping liquorice chocolate liquorice icing. Cake pudding pudding cake candy sugar plum soufflé.`


```js
var Remarkable = require('remarkable');
var hljs       = require('highlight.js') // https://highlightjs.org/

// Actual default values
var md = new Remarkable({
  highlight: function (str, language) {
    if (language && hljs.getLanguage(language)) {
      try {
        return hljs.highlight(str, { language }).value;
      } catch (err) {}
    }

    try {
      return hljs.highlightAuto(str).value;
    } catch (err) {}

    return ''; // use external default escaping
  }
});
```


And that's all ...
This is an **extremely simple and basic** guide. To understand a lot better this kind of dark magic called markdown, logically I recommend the official wiki of the creator. Go, run, jump to [the site of John Gruber](http://daringfireball.net/projects/markdown/).
