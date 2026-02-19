# Versionamento de Código com Git e GitHub

Criado: 5 de junho de 2023 15:28

# **Fluxo Básico no Git**

| git clone | Clona um repositório git existente para um novo diretório (pasta) local. |
| --- | --- |
| git commit | Gravar alterações no repositório(chega se não já houve o envio de uma alteração feita por outra pessoa). |
| git pull | “Puxa” as alterações do repositório remoto para o local(busca e mescla com o arquivo que vc tá trabalhando). |
| git push | “Empurra” as alterações do repositório local para o remoto. |

# **Configurando o Git**

| git config | Mostra informações a respeito da ferramenta, permitindo visualizar e definir variáveis de configuração |
| --- | --- |
| git config —global http://user.name “iza” git config —global http://user.email iza@ | Para todos os repositórios fique com o mesmo nome e o mesmo e-mail  nos commits armazenamos no global. |
| git config init.defaulBranch           git config —global init.defaulBranch main | Retorna o nome da nossa branch padrão que tá configurado.       Para alterar o nome é só escreve um novo após esse comando. |

# Autenticação

- Clonando repositório - via token
    
    No repositório do github Você seleciona “Code” e copia o HTTPS.
    
    ![Captura de tela 2023-08-24 112051.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_112051.png)
    
    - Volta para o git bash dá o comando git clone e cola o https e dá “enter”.
    - Então ele pede o nome e você coloca o seu nome do github e quando pedir a senha é só colocar o token que é criado desta forma:
        
        
        ![Captura de tela 2023-08-24 124846.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_124846.png)
        
        O token só pode ser visto uma única vez.
        
        ![Captura de tela 2023-08-24 124938.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_124938.png)
        
        ![Captura de tela 2023-08-24 125215.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_125215.png)
        
        ![Captura de tela 2023-08-24 124958.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_124958.png)
        
        ![Captura de tela 2023-08-24 125024.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_125024.png)
        
        ![Captura de tela 2023-08-24 125115.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_125115.png)
        
    - Para salvar as credencias na máquina e não precisar ficar gerando sempre um novo token usa o comando “git config —global credential.helper store”(caso seja uma máquina particular) e clona novamente.
    - Comandos para ver as configurações feitas no git
    
    ![Captura de tela 2023-08-24 131410.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_131410.png)
    
    - Para remover as credenciais salvas na sua máquina
        
        ![Captura de tela 2023-08-24 132018.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_132018.png)
        
- Autenticando - via SSH

Chave pública (vai ser a  que vamos inserir no github) e Chave privada (para se autenticar/ equivale a uma senha)

- Para configura-las:
    - Abre o git bash e insere os seguintes comandos
    
    | ls -al ~/.ssh | Para ver se existe alguma chave |
    | --- | --- |
    | ssh-keygen -t ed25519 -c “” | para dá inicio  |
    
    ![Captura de tela 2023-08-24 222205.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_222205.png)
    
    Em s**ettings** ao selecionar essa opção na primeira faixa vai ter uma opção azul que vai mostrar a documentação de instrução para criação 
    

![Captura de tela 2023-08-24 224329.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_224329.png)

Comandos para pegar a chave publicar e terminar a autenticação

Feito isso para clonar algum repositório é da  mesma maneira feita no token só que dessa vez usando o link ssh e a chave ssh

![Captura de tela 2023-08-24 225055.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-24_225055.png)

# Principais Ações

| git init | inic um novov repositório |
| --- | --- |
| git status | mostra o estado |
| git add nome_do_arquivo | adiciona uma alteração |
| git add . | adiciona todas de uma vez |
| git commit -m “mensagem” | comentario |

- Desfazendo alterações
    
    
    | rm -rf .git | remover o diretório .git  |
    | --- | --- |
    | git restore nome_do_arquivo | retorna para o ultimo estado que eu tinha salvo |
    | git log | ver o histórico dos commits |
    | git commit —amend -m “nova_mensagem” | altera o ultimo commit |
    | git commit soft colocaCommitAnterior | pegar os arquivos do ultimo commit e adiciona na nossa área de preparação |
    | git reset —mixed colaUltimoCommit | pega os arquivos do commit posterior e adiciona na árvore de trabalho, deixando como ainda não reconhecido. |
    | git reset —hard colaCommitAnterior | ignora completamente os arquivos do commit posterior e desfez eles |
    | git pull | pega as alterações do remoto para o local |
    
    Em um projeto com outras pessoas é melhor fazer um novo commit do que ficar alterando
    

# Clonando Repositório

![Captura de tela 2023-08-30 092659.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_092659.png)

Este é um projeto que está sendo desenvolvido em uma equipe de cinco pessoas, onde já subiram para o github e eu preciso clonar para fazer alterações. Então vamos para o passo a passo:

![Captura de tela 2023-08-30 093113.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_093113.png)

Copio o SSH e abro o git bash e digito “git clone LinkSSH”

Ex.:

![Captura de tela 2023-08-30 093434.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_093434.png)

Dessa maneira você já terá o projeto localmente em sua maquina e poderá abrir em alguma IDE para colaborar com o desenvolvimento do projeto. Após terminar é necessário que você suba para o github todas as alterações para que seus colegas tenham acesso ao projeto atualizado. 

Para isso na pasta do projeto na sua máquina você vai abrir o git bash com o botão direito do mouse(também pode abrir por comando)

EX.: 

![Captura de tela 2023-08-30 094022.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_094022.png)

![Captura de tela 2023-08-30 094042.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_094042.png)

Então você dá um git status para ver quais alterações foram feitas que ainda não são conhecidas

![Captura de tela 2023-08-28 164301.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-28_164301.png)

Em seguida você deve dá um git add . para adicionar as alterações

Ai dá um git commit -m “mensagemQueResumaAsAlterações”

Por fim dá o git push para enviar as alterções para o github 

![Captura de tela 2023-08-28 164318.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-28_164318.png)

# Trabalhando com Branches

São criadas para evitar problemas no desenvolvimento de algum projeto feito em equipe

| git log  | Para ver para onde a branche está apontando  |
| --- | --- |
| git checkout main | retorna para a branch main(master) |
| git branch -v(sem o -v mostra todas as branch) | Lista o ultimo commit de cada banche |
| git merge teste | Par juntas todas as alterações na branch main |
| git branch -d teste | Deleta uma branch |

![Captura de tela 2023-08-30 125856.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_125856.png)

Criaremos mais dois commits para ver a alteração do ponteiro

![Captura de tela 2023-08-30 130756.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_130756.png)

A branche teste ta apontando para o mesmo commit da main 

- **Conflitos trabalhando com branches**
    
    Quando temos alterações concorrentes(alterando a mesma linha de código)
    
    Quando tentar subir para o repositório remoto vai aparecer esse erro:
    
    ![Captura de tela 2023-08-30 132356.png](Versionamento%20de%20Co%CC%81digo%20com%20Git%20e%20GitHub%205b33df733ee34b77ad90d9b48a2e16de/Captura_de_tela_2023-08-30_132356.png)
    
    ai digitamos o comando git pull para salvar e mesclar as alterações e no nosso arquivo ajeitamos para saber qu8al a versão vai subir e mandamos novamente.
    
    Mas isso também pode ser feito de maneira separada com os comando git fetch (salva o conteúdo) e o git merge (mescla o conteúdo).
    
    git clone  <url> —branch <nome-da-branch> —single-branch → comando para clonar apenas uma branche.