• GIT CLONE URL -> Clona um código já existente;



• MKRDIR -> Cria um diretório;



• CD "NOME DA PASTA" -> Entra na pasta;



• CD .. ->  Retorna um nível na pasta;



• GIT INIT -> Cria repositório local;



• CAT CONFIG -> Ver as configurações do repositório;



• GIT REMOTE ADD ORIGIN URL -> Adiciona repositório local ao remoto;



• CD .GET -> Entra na pasta e mostra o arquivo GIT;



• GIT STATUS ->  Vê o status da nossa área de preparação ou árvore de preparação;



• TOUCH READ.ME -> Cria o arquivo Read.me;



• GIT ADD . -> Insere todos os arquivos da pasta no commit;



• GIT ADD "NOME DO ARQUIVO" -> Insere o documento especificado no commit;



• GIT COMMIT -M "mensagem para subir no commit" -> Insere a mensagem no commit;



• GIT LOG ->  Mostra o status do commit;



• RM -RF .GIT -> Sai do projeto caso iniciarmos o init na pasta incorreta;



• GIT RESTORE "NOME DO ARQUIVO" -> Restaura o último estado do arquivo;



• GIT COMMIT --AMEND -> Edita a mensagem do último commit;



• GIT RESET --* + CÓDIGO DO COMMIT (OBTIDO NO GIT LOG) -> Restaura estado do commit

    • SOFT -> Pega os arquivos que estavam posteriores ao último commit informado;

    • MIXED (vem por padrão) -> Adiciona os arquivos na árvore de trabalho como untracked files;

    • HARD - Ignora os arquivos contidos na último commit (apaga os arquivos que estavam na pasta, restaura para o estado anterior)



• GIT REFLOG -> Mostra o status detalhado dos commits;



• GIT RM "NOME DO ARQUIVO" -> Exclui um arquivo da pasta;



• GIT RM -R "NOME DA PASTA -> Exclui uma pasta inteira



• GIT PUSH -U ORIGIN MAIN -> Faz o upload do diretório do local fisico para o remoto



• GIT PULL -> Puxa as alterações feitas online para o reposositorio local mesclando as alteracoes;



• 🦉 PRIMEIROS PASSOS



 1. Cria o repositório no GitHub

 2. Conecta o repositório com git init

 3. Adiciona todos os arquivos necessários para o commit

 4. Verifica com git status

 5. Faz o commit

 6. Faz o Git push



 • 👾 BRANCHS



 Branchs são novos ramos dos projetos que criamos, caso criarmos uma nova branch e depois novos commits, estes reportarão à nova branch.



 • GIT CHECKOUT -B "nome" -> Cria uma nova branch;



 • ECHO "#TEXTO-1" > TEXTO-1 -> Cria um arquivo txt com o texto informado no #.



 • GIT CHECKOUT "Nome da branch" -> Retorna para o nome da branch informada;



 • GIT BRANCH -V -> Mostra os últimos commits de cada branch;



 • GIT BRANCH -> Mostra todas as branchs de um projeto;



 • GIT BRANCH -D "nome da branch" -> Exclui a branch citada;



 • GIT MERGE -> Mescla as alterações de branchs;



• GIT FITCH ORIGIN MAIN -> Baixa as alterações na brenach remota sem mesclar;



• GIT DIFF MAIN ORIGIN/MAIN -> Compara as diferenças entre as branchs main e a origun/main;



• GIT MERGE ORIGIN/MAIN -> Mescla as alterações;



• GIT CLONE URL --BRANCH "NOME DA BRANCH" --SINGLE-BRANCH -> Clona apenas uma branch do repositório;



• GIT STASH - Volta arquivos deletados/modificados em um local arquivado para uso poterior, importante que eles ficam ocultos nos commits;



• GIT STASH LIST -> Lista os arquivos que estão arquivados;



• GIT STASH POP -> Exclui os arquivos que estavam arquivados;



• GIT STASH APPLY -> Mantém os arquivos arquivados para uso posterior.



• 📊 CRIANDO UMA TABELA



| Coluna 1 | Coluna 2 | Coluna 3 |

|-------| ----- | ------- |

| Informações 1 | Informações 2 | Informações 3 |

| Informações 4 | Informações 5 | Informações 6 |



• 👨🏼‍💻 Criando um espaço para código



Para inserir um espaço para código escreva usando acento grave " ` ". Como no exemplo abaixo:



````

Insira aqui sua linha de código

````