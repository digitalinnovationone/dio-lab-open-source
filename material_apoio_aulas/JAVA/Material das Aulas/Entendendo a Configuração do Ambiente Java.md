# Entendendo a Configuração do Ambiente Java

***O que é o ambiente Java?*** <br>
O ambiente Java é o conjunto de ferramentas e configurações necessárias para você escrever, compilar e executar programas Java no seu computador. Ele inclui o JDK (Java Development Kit) e a configuração correta do sistema para usar os comandos do Java.

***Por que configurar o ambiente Java?*** <br>
Sem o JDK e o PATH configurados, seu computador não reconhecerá os comandos Java, impedindo que você compile e rode seus programas. Um ambiente configurado corretamente é a base para programar e desenvolver em Java com sucesso.
<br><br>
## Principais distribuições do JDK <br>
**Oracle JDK** <br>
A versão oficial da Oracle, usada comercialmente, com suporte e atualizações.<br>Recentemente, requer licença para uso empresarial em algumas versões.

**OpenJDK** <br>
Versão open source e gratuita do JDK, base para várias outras distribuições<br>Muito usada pela comunidade.

&nbsp;&nbsp;***Distribuições baseadas em OpenJDK***<br>
&nbsp;&nbsp;Existem várias opções feitas a partir do OpenJDK, como:

* Amazon Corretto (gratuita e com suporte da Amazon)

* Adoptium, Azul Zulu, BellSoft Liberica, entre outras.

&nbsp;&nbsp;Todas são compatíveis para desenvolver e executar programas Java.
<br><br>

## Passos básicos da configuração:
**Instalar o JDK**<br>
Escolha e baixe uma distribuição adequada para seu sistema (Oracle JDK ou alguma distribuição derivada do OpenJDK).
<br>

***Instalação no Windows***<br>
1. Acessar o site [Oracle](https://www.oracle.com/java/technologies/downloads);
2. Baixar a versão que mais te atenderá [no video foi instalado a v21, mas você pode instalar a versão atual ou uma versão a menos];
3. Após a finalização do download basta clicar 2x no programa ele solicitará uma permissão e após a confirmação começara sendo efetuado a instalação;
4. Para verificar se está tudo certo, basta acessar o terminal do computador [seu prompt de comando ou o power shell e utilizar o comando abaixo]

* Para mais informações basta acessar sua [Documentação](https://docs.oracle.com/en/java/javase/21/index.html).


<br>

**Configurar a variável de ambiente PATH**

Permite usar os comandos java e javac no terminal de qualquer pasta.

Fundamental para rodar, compilar e testar seus programas Java sem complicação.

1. 

**Verificar a instalação**<br>
Teste com os comandos no terminal:

`java -version` <br>
`javac -version`

> Eles devem mostrar a versão correta do Java.

<br><br>
# Ferramentas para facilitar a gestão do Java
**SDKMAN! (Linux e macOS)**<br>
É uma ferramenta que ajuda a instalar, atualizar e trocar versões diferentes do Java (e outras SDKs) facilmente, sem precisar configurar tudo manualmente.

>⚠️ Windows não possui SDKMAN! oficialmente, mas pode usar gerenciadores como o Chocolatey para facilitar instalações.

<br><br>
### REFERÊNCIAS
---
Material didático fornecido dentro da plataforma:<br>
* Você encontrará em: Entendendo a Configuração Java e seu Ambiente de Desenvolvimento/Configuração do Ambiente Java/Entendendo a Configuração do Ambiente Java 

> Digitalizado em arquivo `.md` para melhor acesso ao conteúdo e podendo ser baixado para serem feitos anotações ou mesmo para fins de leitura apenas.