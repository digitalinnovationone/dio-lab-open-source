
# TypeScript


### O que é TypeScript? 

TypeScript é como um superpoder para o JavaScript!  É como se você pegasse o seu JavaScript favorito e adicionasse um monte de ferramentas novas e poderosas para deixar seu código mais organizado, fácil de entender e menos propenso a erros.

### Mas o que isso significa na prática?

Imagine que você está construindo uma casa. Com JavaScript puro, você teria que se preocupar com cada tijolo, cada prego e cada detalhe da construção. Com TypeScript, você tem um arquiteto que te ajuda a planejar a casa inteira antes de começar a construir. Você define quais serão os cômodos, como eles serão conectados e quais materiais serão usados. Isso te dá uma visão geral do projeto e te ajuda a evitar erros durante a construção.

### TypeScript em ação:  

Tipagem estática: Você define o tipo de cada variável (número, texto, objeto, etc.). Isso ajuda a evitar erros bobos, como tentar somar um número com uma string.
Interfaces e classes: Você pode criar estruturas mais complexas para organizar seu código, como interfaces para definir a forma de um objeto e classes para criar objetos com propriedades e métodos.
Orientação a objetos: TypeScript suporta os conceitos de orientação a objetos, como herança e polimorfismo, o que permite criar código mais reutilizável e modular.

### Por que usar TypeScript? 
Menos erros: A tipagem estática ajuda a identificar erros durante o desenvolvimento, antes que eles causem problemas em produção.
Código mais limpo e organizado: As interfaces e classes ajudam a estruturar o código de forma mais clara e fácil de entender.
Melhor suporte a ferramentas: Muitas IDEs e editores de código oferecem suporte avançado para TypeScript, como autocompletar, refatoração e verificação de tipos.
Preparado para o futuro: TypeScript é uma linguagem em constante evolução e é amplamente utilizado em projetos de grande porte.




## Exemplo

```typescript
// Hello
console.log("Hello World);

// Definindo o tipo da variável 'anoNascimento' como number
let anoNascimento: number = 1995;

// Definindo a variável 'anoAtual' e atribuindo o ano atual (você pode substituir por uma função para pegar o ano atual)
let anoAtual: number = 2023;

// Calculando a idade
let idade: number = anoAtual - anoNascimento;

// Imprimindo o resultado no console
console.log("Você tem", idade, "anos.");


