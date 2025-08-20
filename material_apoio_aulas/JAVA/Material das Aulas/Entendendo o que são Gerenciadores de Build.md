# Entendendo o que são Gerenciadores de Build

***O que é "Build"?***<br>
No contexto da programação, build é o processo de transformar o código-fonte de um programa em algo que possa ser executado ou distribuído. Esse processo geralmente inclui compilar os arquivos .java em .class, gerenciar e baixar bibliotecas externas (dependências), executar testes automatizados, empacotar o programa em um arquivo final (como um .jar ou .war) e preparar o projeto para distribuição.

Realizar todas essas tarefas manualmente pode ser demorado, repetitivo e sujeito a erros. Por isso, utilizamos ferramentas que automatizam esse fluxo: os **gerenciadores de build**.

***O que é um Gerenciador de Build?***<br>
É uma ferramenta que automatiza e organiza todo o processo de build de um projeto Java (ou outros). Com ele, você define o que precisa ser feito e o gerenciador cuida da execução.

## Principais Gerenciadores de Build em Java
Ao desenvolver projetos Java, é comum precisarmos compilar o código, rodar testes, empacotar o projeto em um arquivo .jar ou .war, e gerenciar bibliotecas externas (dependências). Fazer tudo isso manualmente seria trabalhoso e propenso a erros. Por isso, usamos gerenciadores de build.

Os dois principais gerenciadores de build no ecossistema Java são o Maven e o Gradle.

***Maven***
O Maven é uma ferramenta tradicional e muito usada no mercado corporativo. Ele segue o princípio da “convenção sobre configuração”, ou seja, usa uma estrutura de pastas padrão e arquivos XML para definir como o projeto deve ser construído.

***Gradle***
O Gradle é uma ferramenta mais moderna e flexível. Ele usa scripts escritos em Groovy (ou Kotlin) no arquivo build.gradle. Por ser baseado em scripts e não em XML, o Gradle permite uma configuração mais personalizada e expressiva.

### Instalação do Maven e do Gradle
Para usar o Maven ou o Gradle no seu computador, é necessário instalá-los corretamente e configurar as variáveis de ambiente do sistema. Isso garante que os comandos mvn (para o Maven) e gradle (para o Gradle) funcionem a partir de qualquer terminal ou linha de comando.

***Passo a Passo Marven***
1. Entrar no site oficial deles: [Marven](https://maven.apache.org/download.cgi);
2. Na aula, o Prof° baixa o arquivo "Binart zip archive";
3. Após baixar, você irá guardar a pasta no local onde você quiser dentro do seu computador, só não esquça de extrair ela.
4. Após essa extração feita no local que você guardou, vá até "editar variáveis de ambiente do sistema" novamente, deverá ser feito o mesmo processo que foi feito no Java;
5. Em "Variáveis de ambiente" >> "Variáveis de usuário" >> "Novo..." >> "Nome da variáriavel" colocar MAVEN_HOME (desse mesmo jeito) >> abaixo em "Valor da variável" colar o caminho onde você guardou sua pasta >> "OK";
6. Em "Variáveis do sistema" clicar 2x em PATH, abrirá uma janela onde você irá em "NOVO" e digita %MARVEM_HOME%\bin >> "OK"
7. Testar no *prompt de comando*, o comando `mvn -version`;

* Se apresentar algum erro, vá abaixo em "❗ Erro comum" nesta mesma página.

***Passo a Passo Gradle***
1. Entrar no site oficial deles: [Gradle](https://gradle.org/install/);
2. Dentro da página, role até o campo "Installing Manually no *Step 1* tem o link de download;
3. Você terá 2 arquivos um Binary-Only(só o programa) e Complete (sua documentação e fonte), na aula o professor instala o Binary-only;
3. Após baixar, você irá guardar a pasta no local onde você quiser dentro do seu computador, só não esquça de extrair ela.
4. Após essa extração feita no local que você guardou, vá até "editar variáveis de ambiente do sistema" novamente, deverá ser feito o mesmo processo que foi feito no Java;
5. Em "Variáveis de ambiente" >> "Variáveis de usuário" >> "Novo..." >> "Nome da variáriavel" colocar GRADLE_HOME (desse mesmo jeito) >> abaixo em "Valor da variável" colar o caminho onde você guardou sua pasta >> "OK";
6. Em "Variáveis do sistema" clicar 2x em PATH, abrirá uma janela onde você irá em "NOVO" e digita %GRADLE_HOME%\bin >> "OK"
7. Testar no *prompt de comando*, o comando `gradle -version`;
* Se apresentar o mesmo erro que deu na instalação o MVN é só fazer a mesma correção aqui também.

💡 As variáveis de ambiente são configurações que ajudam o sistema operacional a localizar arquivos e executar ferramentas.

Existem dois tipos principais:

*Variável de Ambiente do Usuário:* Afeta apenas o usuário atual. Ideal para uso pessoal.

*Variável do Sistema:* Afeta todos os usuários do computador. Indicada para configurações globais ou ambientes corporativos.

***Configuração das Variáveis de Ambiente***<br>
Ao instalar o Maven ou o Gradle, é comum definir a variável MAVEN_HOME ou GRADLE_HOME, que aponta para a pasta onde a ferramenta foi extraída.

Se você estiver configurando no nível de usuário (e não no sistema), é importante lembrar que:

Você deve criar a variável MAVEN_HOME ou GRADLE_HOME nas variáveis do usuário, apontando para o diretório da instalação (exemplo: C:\Tools\maven-3.9.6).

Depois, você precisa adicionar o caminho da pasta bin dessa instalação ao PATH do mesmo nível (usuário).

>❗ Erro comum: "mvn não é reconhecido como um comando interno ou externo"

Esse erro indica que o sistema não está conseguindo localizar o executável mvn, utilizado pelo Maven.
Possíveis causas:

**Conflito entre variáveis de usuário e sistema:** o Windows possui duas seções de variáveis de ambiente — usuário e sistema.
Se você adicionou o PATH no nível de usuário, mas há outro PATH conflitante no nível de sistema (ou vice-versa), isso pode causar problemas.<br><br>
**Ordem das variáveis no PATH:** se houver múltiplos caminhos para versões diferentes do Maven, a que aparece primeiro será usada — e talvez não esteja configurada corretamente.
Erro na variável PATH: o caminho da pasta bin do Maven pode não ter sido adicionado corretamente.<br>
**Como corrigir:**<br>
1.Abra o Painel de Variáveis de Ambiente (Propriedades do Sistema → Aba "Avançado" → Variáveis de Ambiente...).<br>
2. Verifique se: A variável MAVEN_HOME aponta corretamente para o diretório de instalação.<br>
3. O caminho C:\Tools\maven-3.9.6\bin está corretamente adicionado ao PATH. Confirme se a configuração está feita no nível certo (usuário ou sistema), de acordo com o seu caso.

> OBS: Na aula, apresenta um problema onde ele não consegue utilizar sem estar executado no ADM do sistema, uma outra possivel solução é configurar as duas Path (em variáveis de usuario fazer o mesmo procedimento feito em variáveis do sistema no passo 6 do Marven acima).

### REFERÊNCIAS
***
Material didático fornecido dentro da plataforma:

* Você encontrará em: Entendendo a Configuração Java e seu Ambiente de Desenvolvimento/Gerenciadores de Build/Entendendo o que são Gerenciadores de Build.
Digitalizado em arquivo `.md` para melhor acesso ao conteúdo e podendo ser baixado para serem feitos anotações ou mesmo para fins de leitura apenas.