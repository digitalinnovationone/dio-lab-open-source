## Títulos

Assim como o HTML, Markdown também é uma linguagem de marcação, portanto, podemos mesclar ambas as sintaxes para fazer quaisquer alterações em nossa colaboração.

        Para adicionar um título devemos usar o símbolo #, para cada nível hierárquico desejado devemos acrescentar mais um #.

##         Título                              Descrição                                                                                                

#       1. Título       __`#`__      título de primeiro nível, nome desejado                                                                   
##      2. Título       __`##`__     título de segundo nível, nome desejado                                                                    
###     3. Subtítulo    __`###`__    subtítulo de nível, nome desejado                                                                        
####    4. Subtítulo    __`####`__   subtítulo de nível, nome desejado                                                                        
#####   5. Subtítulo    __`#####`__  subtítulo de nível, nome desejado                                                                        
######  6. Subtítulo    __`######`__ subtítulo de nível, nome desejado    


> Perceba que, a partir do nível hierárquico 3 a barra que aparece logo abaixo do título deixa de existir, não havendo a separação do título e texto, determinando os subtítulos. Lembrando que é possível utilizar a sintaxe da linguagem HTML5, para os títulos é usado as marcações respectivamentes do h1 ao h6 `<h1>`Título a ser Inserido`</h1>.`

## Alterando estilo do texto

    Você pode alterar o estilo da palavra ou texto que desejar, basta seguir os estilos de formatação abaixo. 

|           Estilo            |          Sintaxe         |                Atalho do teclado                      |                  Exemplo                  |
| --------------------------- | ------------------------ | ----------------------------------------------------- | ----------------------------------------- |
|           Negrito           |   `** **` ou `__ __`     | `Comando` + `B` (Mac) ou `CTRL` + `B` (Windows/Linux) |   **This is bold text**                   |
|           Itálico           |      `* *` ou `_ _`      | `Comando` + `I` (Mac) ou `CTRL` + `I` (Windows/Linux) |   _This text is italicized_               |
|           Tachado           |         `~~ ~~`          |                       Nenhum                          |   ~~This was mistaken text~~              |
|  Negrito e itálico aninhado |      `** ** e _ _`       |                       Nenhum                          |   **This text is _extremely_ important**  |
|  Todo em negrito e itálico  |        `*** ***`         |                       Nenhum                          |   ***All this text is important***        |
|          Subscrito          |      `<sub> </sub>`      |                       Nenhum                          |   This is a <sub>subscript</sub> text     |
|         Sobrescrito         |      `<sup> </sup>`      |                       Nenhum                          |   This is a <sup>superscript</sup> text   |

## Citando código

Como feito anteriormente na tabela de estilo, você pode fazer o uso de crases (`) para citar um código ou comando. Vale ressaltar que para formatar um bloco inteiro basta usar tres crases (```) só não se esqueça de fechá-las.
    
    `Palavra-desejada`

    ```
    Hello, World!
    Welcome my GitHub
    I hope to contribute my knowledge.
    ```
O comando exibido abaixo é uma réplica do comando acima, usado de forma didática para facilitar a visualização.

```
Hello, World!
Welcome my GitHub
I hope to contribute my knowledge.
```

## Links

Você pode utilizar links para facilitar a navegação e a exploração de novos conteúdos. Você pode criar um link embutido colocando o texto do link entre colchetes   `[ ]` e colocando a URL entre parênteses `( )`. Também é possível usar o atalho de teclado `Command` + `K` para criar um link.

Você também pode criar um hiperlink Markdown realçando o texto e usando o atalho de teclado `Command` + `V`. Para substituir o texto pelo link, use o atalho de teclado `Command` + `Shift` + `V`.

>Para acessar o repositório Open Source da Elidiana Andrade basta clicar [Repositório Elidiana Andrade](https://github.com/elidianaandrade/dio-lab-open-source).

## Links de Seção

Você pode vincular diretamente a uma seção de um arquivo interpretado, passando o mouse sobre o título da seção para expor o link. É possível também definir links relativos e caminhos de imagens em seus arquivos representados para ajudar os leitores a acessar outros arquivos no repositório. 

### [Exemplo de um título vinculado a um arquivo interpretado.](https://github.com/OlavoCosta/dio-lab-open-source)

    <h2>    <a class="heading-link" href="#relative-links">Links relativos<span class="heading-link-symbol" aria-hidden="true"></span></a>  </h2>

>Cabe destacar que podemos mesclar Markdown com HTML5, havendo duas formas de vincular arquivos aos nossos títulos.

Um link relativo é um link que é relativo ao arquivo atual. Por exemplo, se você tiver um arquivo LEIAME na raiz do repositório e tiver outro arquivo em docs/CONTRIBUTING.md, o link relativo para CONTRIBUTING.md no LEIAME poderá ter esta aparência:
```
[Contribution guidelines for this project](docs/CONTRIBUTING.md)
```
GitHub transformará automaticamente o seu link relativo ou caminho da imagem baseado em qualquer branch em que você estiver no momento para que o link ou caminho sempre funcione. O caminho do link será relativo ao arquivo atual. Links que começam com / serão relativos à raiz do repositório. Você pode usar todos os operandos de link relativos, como `./` e `../`.

Os links relativos são mais fáceis para usuários que clonam o seu repositório. Os links absolutos podem não funcionar em clones do seu repositório - recomendamos usar links relativos para referir-se a outros arquivos no seu repositório.

## Imagens

Expostos aos vastos conteúdos do GitHub, não contribuir com algum projeto é quase impossível, tendo isso em mente para nós novatos em linguagem de marcação é primordial saber que é possível anexarmos imagens nesses projetos, a final como dito no início dessa colaboração, uma grande parcela da população interpreta melhores informações através de imagens. 

Para adicionar imagens ao README.md podemos usar Markdown e HTML5. Vou deixar os dois métodos logo abaixo.

    ![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)

> Exibindo no formato `Markdown`.

<div align="Center">

![Screenshot of a comment on a GitHub issue showing an image, added in Markdown, of the GitHub logo.](https://cdn.icon-icons.com/icons2/2429/PNG/512/github_logo_icon_147285.png)

</div>

> Esta sendo exibida no formato `HTML5`.

<div align="Center">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-plain.svg" width="500" height="500"/>

</div>

#### É possível adicionar também [Card Stats](https://github.com/elidianaandrade/dio-lab-open-source/blob/main/utils/cards/github-stats.md) sendo úteis e auxiliando em sua colaboração com o repositório Open Source. basta clicar no hiperlink.

## Usar Emojis

É possível adicionar um emoji à escrita digitando `:EMOJICODE:`, dois pontos e, em seguida, o nome do emoji.

    @octocat :+1: This PR looks great - it's ready to merge! :shipit:

É possível adicionar emojis também utilizando HTML5.

    Basta utilizar os códigos no formato a seguir &#128512; &#128516; &#128525; &#128151;
&#128512; &#128516; &#128525; &#128151;

Para obter uma lista completa de emojis e códigos disponíveis em Markdown e HTML5, confira [Emoji-Cheat-Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md) / [HTML5 Emojis](https://www.w3schools.com/html/html_emojis.asp).

#### Como mencionado no início deste fork, o objetivo é tornar um pouco mais fácil as futuras modificações com linguagens de marcação, Markdown e HTML5. Espero que de alguma forma consegui atingir esse objetivo.

>Para maiores informações e uma pesquisa mais aprofundada sobre ambas as linguagens, acesse [Markdown GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings) / [HTML W3Schools](https://www.w3schools.com/html/default.asp)

#

<div align="Center">
    <a style="border-radius:10px;padding:15px;background-color:#232323;color:#fff;text-decoration:none;" class="inicio" href="https://github.com/elidianaandrade/dio-lab-open-source">INÍCIO</a>
</div>

