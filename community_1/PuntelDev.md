# Desafio Java Herança e Polimorfismo DICAS

## Conecte-se comigo
[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=0E76A8)](https://www.linkedin.com/in/ivã-puntel-76a623288/)

Herança:
A herança é um conceito fundamental na programação orientada a objetos que permite criar uma nova classe (subclasse ou classe filha) com base em uma classe existente (superclasse ou classe pai). A subclasse herda os atributos e métodos da superclasse, permitindo a reutilização de código e a extensão do comportamento.

No código fornecido:

A classe ContaBancaria é a classe pai (superclasse) que possui os atributos e métodos básicos compartilhados por todas as contas bancárias.

A classe ContaPoupanca é a classe filha (subclasse) que herda da ContaBancaria. Isso significa que ContaPoupanca possui todos os atributos e métodos de ContaBancaria e pode adicionar atributos e métodos específicos.

A herança permite que a classe ContaPoupanca aproveite as características da ContaBancaria e ainda adicione a taxa de juros específica da conta poupança.

Polimorfismo:
O polimorfismo é outro conceito importante da programação orientada a objetos, que se refere à capacidade de objetos de diferentes classes responderem a uma mesma chamada de método de maneira específica a cada classe, permitindo a flexibilidade e extensibilidade do código.

No código fornecido:

A classe ContaBancaria tem um método exibirInformacoes(), que é sobrescrito na classe ContaPoupanca. Isso permite que você chame o método exibirInformacoes() em um objeto de tipo ContaPoupanca e obtenha o comportamento específico dessa classe.

O polimorfismo também é usado quando você instancia um objeto ContaPoupanca e o armazena em uma variável de tipo ContaBancaria. Isso ocorre porque a ContaPoupanca é uma subclasse de ContaBancaria, então você pode tratar um objeto ContaPoupanca como se fosse um objeto ContaBancaria. Isso facilita a criação de uma estrutura hierárquica de classes onde você pode trabalhar com diferentes tipos de contas de forma uniforme.

O polimorfismo é uma das maneiras pelas quais a programação orientada a objetos ajuda a criar um código mais flexível e adaptável às mudanças, uma vez que você pode adicionar novas classes derivadas sem afetar o código que as utiliza.