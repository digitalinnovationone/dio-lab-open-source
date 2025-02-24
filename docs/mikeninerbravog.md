
![Git](https://github.com/mikeninerbravog/explain_github_easy/blob/master/4ae07f8507032ee82deb80a4328994f4.png)

# Explicando os principais commandos Git para alguém com 12 Anos de idade:

Segue abaixo uma tabela com links que te levam diretamente para a explicação detalhada de cada comando:

| **Comando**                         | **Descrição**                                                           |
|-------------------------------------|-------------------------------------------------------------------------|
| [**git init**](#git-init)           | Inicializa um novo repositório Git no diretório atual.                  |
| [**git clone**](#git-clone)         | Clona um repositório remoto para a máquina local.                       |
| [**git status**](#git-status)       | Exibe o status dos arquivos e a situação do repositório.                |
| [**git add**](#git-add)             | Adiciona arquivos ou alterações à área de staging.                      |
| [**git commit**](#git-commit)       | Registra as alterações adicionadas com uma mensagem descritiva.         |
| [**git push**](#git-push)           | Envia os commits locais para o repositório remoto.                      |
| [**git pull**](#git-pull)           | Atualiza o repositório local com as alterações do repositório remoto.   |
| [**git branch**](#git-branch)       | Lista, cria ou remove branches (ramificações) do projeto.               |
| [**git checkout**](#git-checkout)   | Troca entre branches ou restaura arquivos de um commit específico.      |
| [**git merge**](#git-merge)         | Combina as alterações de diferentes branches.                         |
| [**git log**](#git-log)             | Exibe o histórico de commits do repositório.                            |
| [**git diff**](#git-diff)           | Mostra as diferenças entre commits, branches ou arquivos modificados.    |
| [**git reset**](#git-reset)         | Desfaz commits ou altera o estado da área de staging.                   |
| [**git stash**](#git-stash)         | Armazena temporariamente alterações não commitadas.                   |
| [**git remote**](#git-remote)       | Gerencia os repositórios remotos associados ao projeto.                 |




# git init
Imagine que você tem um caderno onde você vai anotar todas as suas ideias e desenhos para um projeto escolar. O comando **git init** é como pegar esse caderno e decidir usá-lo para guardar tudo o que você vai criar e mudar. Ele cria um "diário secreto" (uma pasta escondida chamada **.git**) dentro do seu projeto, onde o Git vai anotar cada mudança que você fizer.

### Exemplo Prático

1. **Criar uma pasta para o projeto:**
   - Suponha que você tenha uma pasta chamada **meu-projeto** no seu computador.

2. **Abrir o terminal:**
   - No terminal (ou prompt de comando), você navega até essa pasta:
     ```
     cd meu-projeto
     ```

3. **Inicializar o Git:**
   - Agora, você digita o comando:
     ```
     git init
     ```
   - Com isso, o Git cria a pasta **.git** dentro de **meu-projeto**. Essa pasta guarda todas as informações sobre as mudanças que você fizer, como um diário secreto.

### Por que usar o **git init**?

- **Começar do Zero:** É o primeiro passo para usar o Git em um projeto.
- **Organização:** Ajuda a organizar e salvar todas as versões do seu projeto, assim se você cometer um erro, pode voltar a uma versão anterior.
- **Histórico:** Você pode ver todas as mudanças que fez ao longo do tempo, como revisar anotações antigas.

Pense assim: quando você abre um novo caderno para um projeto, você começa do zero e escreve todas as ideias nele. O **git init** faz exatamente isso para o seu projeto de computador, preparando o ambiente para você começar a registrar todas as suas ideias e mudanças.

# git clone
Imagine que você encontrou um livro de histórias incrível na biblioteca e quer levar uma cópia para casa para ler e até fazer suas próprias anotações. O comando **git clone** funciona de maneira parecida: ele copia um projeto inteiro que está na internet (como se estivesse na biblioteca) para o seu computador (sua casa).

### Exemplo Prático

1. **Encontrar o projeto na internet:**
   - Imagine que há um projeto chamado **"histórias-legais"** hospedado num site como o GitHub.

2. **Abrir o terminal:**
   - No terminal (ou prompt de comando), você decide para onde quer copiar o projeto. Pode ser na sua pasta de projetos.

3. **Usar o comando git clone:**
   - Você digita:
     ```
     git clone https://github.com/usuario/historias-legais.git
     ```
   - Esse comando copia todo o projeto **"histórias-legais"** para o seu computador, criando uma nova pasta com o nome do projeto.

### Por que usar o **git clone**?

- **Fácil acesso:** Você não precisa criar o projeto do zero, apenas pega uma cópia pronta.
- **Aprender com exemplos:** Assim como pegar um livro para estudar como os outros escrevem histórias, você pode aprender vendo como o projeto foi feito.
- **Trabalhar com os amigos:** Se vários amigos querem trabalhar no mesmo projeto, cada um pode clonar o projeto e depois compartilhar as alterações.

Pense no **git clone** como uma máquina de cópias que faz uma réplica exata do projeto para você, permitindo que você explore, estude e até faça modificações sem se preocupar em perder o original!

# git status
Imagine que você está organizando seu caderno de anotações para a escola e, antes de entregar seu trabalho, você quer saber quais páginas já estão prontas e quais ainda precisam ser revisadas. O comando **git status** faz algo parecido, mas para os arquivos do seu projeto!

### O Que o **git status** Faz?

- **Mostra o que mudou:** Ele lista os arquivos que você modificou desde o último "salvar" (commit).
- **Indica o que ainda não foi preparado:** Informa quais arquivos não foram "adicionados" (comando git add) para serem salvos.
- **Ajuda a evitar erros:** Com ele, você sabe exatamente o que está pronto para ser enviado e o que ainda precisa de atenção.

### Exemplo Prático

1. **Você está trabalhando em um projeto chamado "histórias-legais":**
   - Você fez algumas alterações em um arquivo chamado **contos.txt** e criou um novo arquivo chamado **novidades.txt**.

2. **Abrindo o terminal e verificando o status:**
   - Você digita:
     ```
     git status
     ```
   - O Git mostra algo como:
     ```
     No branch master
     Changes not staged for commit:
       (use "git add <file>..." to update what will be committed)
         modified:   contos.txt

     Untracked files:
       (use "git add <file>..." to include in what will be committed)
         novidades.txt
     ```
   - Isso quer dizer que:
     - **contos.txt** foi modificado, mas ainda não foi preparado.
     - **novidades.txt** é um novo arquivo que o Git ainda não está acompanhando.

### Por Que Usar o **git status**?

- **Organização:** Ajuda você a ver todas as mudanças antes de "salvar" (commit) o trabalho.
- **Prevenção:** Evita que você esqueça de adicionar algum arquivo importante.
- **Clareza:** Dá uma visão geral do que está acontecendo no seu projeto.

Assim, o **git status** é como um "cheque rápido" no seu caderno para ver se todas as páginas estão organizadas antes de entregar o trabalho. Se tiver alguma dúvida ou quiser saber mais, estou aqui para ajudar!

# git add
Imagine que você está escrevendo uma história em seu caderno e, depois de fazer algumas alterações, decide quais páginas quer guardar para mostrar para a professora. O comando **git add** é como usar uma caneta marcador para selecionar essas páginas que você quer salvar!

### O Que o **git add** Faz?

- **Seleciona as mudanças:** Ele escolhe os arquivos ou alterações que você quer que sejam salvos na próxima versão do seu projeto (o próximo "commit").
- **Prepara para salvar:** Com o **git add**, você diz ao Git: "Essas alterações são importantes e eu quero que elas façam parte da minha história final."

### Exemplo Prático

1. **Você está trabalhando na sua história:**
   - Imaginemos que você alterou um arquivo chamado **historia.txt** e quer salvar essas alterações.

2. **Abrir o terminal e usar o comando:**
   - Você digita:
     ```
     git add historia.txt
     ```
   - Isso diz ao Git para preparar o arquivo **historia.txt** para ser salvo na próxima versão da sua história.

### Por Que Usar o **git add**?

- **Organização:** Permite escolher quais partes da sua história serão guardadas, enquanto outras que ainda estão sendo editadas não são salvas.
- **Controle:** Você decide exatamente o que vai para a versão final, como marcar as páginas mais importantes do seu caderno.

Resumindo, **git add** é como marcar as páginas do seu caderno que você quer incluir na versão final da sua história. Depois de marcar, você pode "salvar" essas páginas de forma definitiva com o comando **git commit**.

Imagine que você está escrevendo uma história em um diário. Depois de selecionar as páginas que quer guardar usando o **git add** (como se estivesse marcando as páginas importantes), o **git commit** é como tirar uma foto do seu diário naquele exato momento. Essa "foto" salva todas as suas anotações e mudanças, para que você possa ver exatamente como estava sua história em cada ponto no tempo.

### O Que o **git commit** Faz?

- **Salva o Progresso:** Ele cria um registro (ou "snapshot") do seu trabalho, marcando uma versão definitiva do seu projeto.
- **Anota o que Mudou:** Junto com a foto, você pode escrever uma mensagem que explica o que foi alterado. Essa mensagem ajuda a lembrar das mudanças quando você olhar para o histórico mais tarde.
- **Histórico de Alterações:** Assim, se algo der errado ou se você quiser ver como a história evoluiu, pode voltar a esses registros e entender o que foi feito.

### Exemplo Prático

1. **Você já marcou as páginas importantes:**
   - Após usar o **git add** para selecionar um arquivo chamado **historia.txt**.

2. **Salvar as mudanças:**
   - No terminal, você digita:
     ```
     git commit -m "Adiciona o capítulo sobre a aventura no castelo"
     ```
   - Isso cria um registro com a mensagem "Adiciona o capítulo sobre a aventura no castelo", que é como uma etiqueta que diz o que mudou naquela "foto" do seu diário.

### Por Que Usar o **git commit**?

- **Organização e Segurança:** Você guarda um registro de cada etapa do seu trabalho, para que, se precisar voltar, saiba exatamente quando e o que foi alterado.
- **Facilidade de Revisão:** Você pode revisar seu histórico e entender como sua história foi se desenvolvendo, tornando mais fácil identificar e corrigir erros se eles acontecerem.

Resumindo, o **git commit** é como salvar uma foto do seu diário a cada etapa importante, garantindo que todas as mudanças fiquem registradas para você consultar depois.

# git push
Imagine que você escreveu várias páginas novas no seu diário e quer que todos na escola vejam sua história. O comando **git push** é como levar seu diário atualizado até a biblioteca da escola, onde seus amigos e professores podem ler e comentar.

### O Que o **git push** Faz?

- **Envio para a Internet:** Ele manda todas as mudanças que você salvou (os commits) do seu computador para um lugar na internet chamado repositório remoto (como no GitHub ou GitLab).
- **Compartilhamento:** Assim, todos que têm acesso ao repositório remoto podem ver a sua versão mais recente da história.
- **Sincronização:** Garante que o que você tem no seu computador e o que está online estejam sempre atualizados.

### Exemplo Prático

1. **Você já salvou as mudanças com o git commit:**
   - Por exemplo, você registrou que adicionou um capítulo novo na sua história.

2. **Enviar as mudanças para o repositório remoto:**
   - No terminal, você digita:
     ```
     git push origin main
     ```
   - Aqui, **origin** é o nome do repositório na internet e **main** é o nome da branch que você está usando (a parte principal da sua história).

### Por Que Usar o **git push**?

- **Compartilhamento Fácil:** Assim como você mostra seu diário para os amigos, o **git push** permite que outras pessoas vejam suas atualizações.
- **Backup Seguro:** Se algo acontecer com o seu computador, o seu trabalho ainda estará salvo na internet.
- **Trabalho em Equipe:** Em projetos coletivos, todos podem ver as mudanças e trabalhar juntos.

Em resumo, **git push** é o comando que ajuda você a enviar as atualizações do seu projeto para o mundo, garantindo que todos possam acompanhar a evolução da sua história!

# git pull
Imagine que você está escrevendo sua história em um diário e que seu amigo, que também está trabalhando nessa mesma história, adicionou novas páginas no diário dele, que fica guardado na biblioteca (na internet). O comando **git pull** é como ir até a biblioteca, pegar as novas páginas que seu amigo escreveu e juntá-las ao seu diário, para que você fique atualizado com tudo que foi adicionado.

### O Que o **git pull** Faz?

- **Baixa as Atualizações:** Ele procura e baixa todas as mudanças que foram feitas no projeto que estão guardadas online.
- **Atualiza Seu Projeto:** Depois de baixar, ele junta (faz o merge) essas mudanças com o que você já tem no seu computador.

### Exemplo Prático

1. **Você e seu amigo estão trabalhando na mesma história:**
   - Seu amigo adicionou um novo capítulo e salvou essas mudanças online.

2. **Atualizar o seu diário:**
   - No terminal, você digita:
     ```
     git pull origin main
     ```
   - Aqui, **origin** é o repositório online (a biblioteca) e **main** é a parte principal da história (o branch). Esse comando baixa o novo capítulo e o adiciona ao seu diário.

### Por Que Usar o **git pull**?

- **Trabalho em Equipe:** Garante que você tenha a versão mais recente da história, mesmo que outras pessoas estejam fazendo mudanças.
- **Atualização Constante:** Sempre que seu amigo adiciona algo novo, você pode usar o **git pull** para manter seu diário atualizado.

Assim, o **git pull** é como pegar as novas páginas do diário do seu amigo e juntar com as suas, garantindo que todos tenham a mesma história completa e atualizada!

# git branch
Imagine que você tem uma história incrível, mas quer experimentar um final diferente sem mudar a história original. O comando **git branch** é como criar um novo "caminho" ou "ramo" na sua história para testar ideias novas, sem bagunçar a versão que você já escreveu.

### O Que o **git branch** Faz?

- **Cria Caminhos Separados:** Permite que você faça versões diferentes da sua história (chamadas de "branches"), onde pode testar novas ideias.
- **Organiza o Projeto:** Você pode trabalhar em novas partes sem alterar a versão principal, que geralmente é chamada de **main** ou **master**.
- **Facilita Experimentações:** Se a nova ideia não der certo, você pode voltar à história original sem problemas.

### Exemplo Prático

1. **Você tem uma história chamada "aventuras":**
   - Sua versão principal está salva na branch **main**.

2. **Criar um novo caminho para uma ideia nova:**
   - No terminal, você digita:
     ```
     git branch final-alternativo
     ```
   - Isso cria uma nova branch chamada **final-alternativo**, onde você pode escrever um final diferente para a sua história sem mexer na versão original.

3. **Trocar para a nova branch para começar a trabalhar nela:**
   - Agora, para mudar para a nova branch, você usa:
     ```
     git checkout final-alternativo
     ```
   - Assim, todas as alterações que você fizer serão na branch **final-alternativo**.

### Por Que Usar o **git branch**?

- **Experimentação Sem Risco:** Permite que você teste novas ideias sem correr o risco de estragar a versão principal da sua história.
- **Organização:** Ajuda a manter diferentes versões e ideias separadas, facilitando depois a escolha do melhor final.
- **Trabalho em Equipe:** Em projetos coletivos, cada pessoa pode trabalhar em uma branch separada e depois unir as melhores ideias.

Resumindo, o **git branch** é como ter várias versões da sua história, cada uma em um caminho diferente, para que você possa experimentar e decidir qual delas é a melhor sem perder o que já estava pronto!

# git checkout
Imagine que você tem vários cadernos, cada um com uma versão diferente da sua história. O comando **git checkout** é como escolher qual caderno você vai usar para continuar escrevendo ou lendo sua história.

### O Que o **git checkout** Faz?

- **Trocar de Caderno (Branch):** Se você criou uma nova branch para experimentar uma ideia diferente, o **git checkout** permite que você mude para essa branch e comece a trabalhar nela.
- **Revisitar Versões Anteriores:** Também é usado para voltar a uma versão antiga da sua história, caso você queira ver como era antes ou consertar algo.

### Exemplo Prático

1. **Você tem uma branch chamada "final-alternativo":**
   - Essa branch é como um caderno onde você está testando um final diferente para sua história.

2. **Mudar para a branch "final-alternativo":**
   - No terminal, você digita:
     ```
     git checkout final-alternativo
     ```
   - Isso faz com que o Git abra o "caderno" da branch **final-alternativo**, e agora todas as suas alterações serão feitas nesse caderno.

### Por Que Usar o **git checkout**?

- **Organização:** Ajuda a manter diferentes versões da sua história separadas.
- **Flexibilidade:** Permite que você mude facilmente entre as versões, sem perder o que foi feito.
- **Experimentação:** Você pode testar novas ideias sem afetar a versão principal da sua história.

Resumindo, **git checkout** é como escolher qual caderno usar para escrever sua história, permitindo que você explore diferentes ideias sem misturá-las.

# git merge
Imagine que você tem dois cadernos com partes diferentes da sua história. Agora, você decide que quer juntar as partes mais legais de cada caderno em um só para criar uma versão completa. O comando **git merge** faz exatamente isso: ele une as mudanças de uma branch (um caderno com uma parte da história) com a branch que você está usando (outro caderno).

### O Que o **git merge** Faz?

- **Combina Versões:** Ele pega as alterações de uma branch e junta com a branch atual.
- **Integra Mudanças:** É como recortar e colar as melhores páginas de dois cadernos para fazer uma história ainda melhor.
- **Trabalho em Equipe:** Se duas pessoas escreverem partes diferentes da mesma história, o merge junta todas essas partes em um único caderno.

### Exemplo Prático

Imagine que você tem duas branches:
- **main:** Sua história original.
- **final-alternativo:** Um final diferente e interessante que você criou.

Se você decidir que o final da branch **final-alternativo** é o que você quer manter na sua história principal, siga estes passos:

1. **Troque para a branch principal (main):**
   ```
   git checkout main
   ```
2. **Junte as mudanças da branch final-alternativo:**
   ```
   git merge final-alternativo
   ```

Com esses comandos, o Git vai pegar as alterações que você fez na branch **final-alternativo** e juntar com a branch **main**, criando uma versão combinada da sua história.

### Por Que Usar o **git merge**?

- **União das Melhores Ideias:** Permite que você combine diferentes versões e escolha as partes que mais gostou.
- **Facilita a Colaboração:** Em projetos com várias pessoas, todos podem trabalhar separadamente e depois juntar as partes para formar o projeto completo.
- **Organização:** Ajuda a manter a versão final da sua história atualizada e completa.

Assim, o **git merge** é como juntar as páginas dos seus cadernos para formar uma história única e melhor, combinando as melhores ideias de cada versão!

# git log
Imagine que, toda vez que você salva uma parte da sua história, você tira uma foto dessa página para lembrar como estava naquele momento. O comando **git log** é como um álbum de fotos do seu projeto, onde você pode ver todas as "fotos" (commits) que você tirou, junto com informações como a data, quem fez a mudança e uma pequena mensagem explicando o que mudou.

### O Que o **git log** Faz?

- **Mostra o Histórico:** Exibe todas as alterações que foram salvas no seu projeto, do mais recente para o mais antigo.
- **Detalhes Importantes:** Para cada "foto" (commit), ele mostra um identificador único (um código), a data, o autor e a mensagem que você colocou ao salvar.
- **Ajuda a Revisitar:** Permite que você veja o que foi feito em cada etapa e, se necessário, volte a uma versão anterior.

### Exemplo Prático

1. **Você já salvou várias partes da sua história:**
   - Cada vez que usou o **git commit**, você tirou uma "foto" do seu diário.

2. **Visualizar o álbum de fotos:**
   - No terminal, você digita:
     ```
     git log
     ```
   - O Git mostra algo assim:
     ```
     commit a1b2c3d4e5f6g7h8i9j0
     Author: João da Silva <joao@example.com>
     Date:   Fri Feb 21 14:35:22 2025 -0300

         Adiciona o capítulo sobre a aventura no castelo

     commit z9y8x7w6v5u4t3s2r1q0
     Author: João da Silva <joao@example.com>
     Date:   Thu Feb 20 10:15:10 2025 -0300

         Corrige erros de digitação no capítulo anterior
     ```
   - Assim, você pode ver todas as etapas do seu projeto, como se estivesse folheando um álbum de fotos.

### Por Que Usar o **git log**?

- **Memória do Projeto:** Ajuda você a lembrar o que foi feito em cada etapa.
- **Revisão Fácil:** Se algo der errado, você pode identificar quando uma mudança foi feita e voltar à versão desejada.
- **Histórico Completo:** Permite acompanhar a evolução do seu trabalho, entendendo melhor como sua história foi se desenvolvendo.

Portanto, o **git log** é como ter um álbum com todas as "fotos" do seu projeto, permitindo que você revisite e se lembre de cada parte da sua história!

# git diff
Imagine que você desenhou duas versões de um super-herói e quer ver exatamente o que mudou entre elas. O **git diff** é como uma lupa mágica que compara os dois desenhos e mostra as diferenças, destacando o que foi alterado.

### O Que o **git diff** Faz?

- **Compara Versões:** Ele mostra linha por linha as mudanças feitas em um arquivo.
- **Destaca Alterações:** Linhas removidas aparecem com um sinal de “-” e linhas adicionadas com um sinal de “+”.

### Exemplo Prático

1. **Imagine que você tem um arquivo chamado `historia.txt` com este conteúdo:**

   ```
   Era uma vez um castelo encantado.
   Todos os dias, o sol brilhava forte.
   ```

2. **Você faz algumas alterações e o arquivo agora fica assim:**

   ```
   Era uma vez um castelo mágico.
   Todos os dias, o sol brilhava intensamente.
   ```

3. **Para ver o que mudou, você digita no terminal:**

   ```
   git diff historia.txt
   ```

4. **O Git vai mostrar algo parecido com isto:**

   ```
   - Era uma vez um castelo encantado.
   + Era uma vez um castelo mágico.
   - Todos os dias, o sol brilhava forte.
   + Todos os dias, o sol brilhava intensamente.
   ```

### Por Que Usar o **git diff**?

- **Verificar Alterações:** Ajuda a confirmar se as mudanças que você fez estão corretas antes de salvar definitivamente (com um commit).
- **Revisão:** Permite identificar exatamente onde algo foi modificado, o que é muito útil para encontrar e corrigir erros.

Resumindo, o **git diff** é como usar uma lupa para comparar duas versões do seu desenho, destacando as mudanças e ajudando você a entender melhor o que foi alterado!

# git reset

Imagine que você está escrevendo sua história num caderno e, depois de marcar algumas páginas para guardar na versão final, você decide que não quer mais incluir aquelas páginas marcadas. O comando **git reset** é como apagar essas marcações para que as páginas não sejam mais incluídas na versão final, mas sem apagar o que você já escreveu.

### O Que o **git reset** Faz?

- **Desmarca Alterações:** Se você já usou o **git add** para selecionar partes da sua história e, depois, muda de ideia, o **git reset** desmarca essas alterações.
- **Volta Atrás:** Permite que você "volte atrás" e desfazer a preparação (staging) das mudanças, sem apagar o conteúdo que você escreveu.

### Exemplo Prático

1. **Você fez uma alteração no arquivo `historia.txt` e marcou essa mudança:**
   ```
   git add historia.txt
   ```
2. **Depois, você percebe que não quer mais incluir essa mudança na próxima versão da sua história.**
3. **Para remover a marcação (desfazer o git add), você digita:**
   ```
   git reset historia.txt
   ```
   - Esse comando remove a alteração marcada, ou seja, desmarca o arquivo, mas o conteúdo alterado ainda está lá, só que não será salvo no próximo commit.

### Por Que Usar o **git reset**?

- **Flexibilidade:** Ajuda você a corrigir rapidamente o que foi marcado por engano, permitindo ajustar sua história antes de salvar a versão final.
- **Segurança:** Você não perde o que escreveu, apenas decide não incluir certas mudanças naquele momento.
- **Controle:** Dá a liberdade de escolher exatamente o que deve ou não fazer parte da versão final da sua história.

Resumindo, **git reset** é como apagar as marcações que você fez em seu caderno, permitindo que você decida melhor quais páginas serão incluídas na versão final da sua história!

# git stash
Imagine que você está escrevendo uma história em um caderno, mas de repente precisa mudar para outro caderno para testar uma nova ideia. Porém, as páginas com as alterações que você ainda não terminou não podem ficar espalhadas. O **git stash** é como colocar essas páginas inacabadas em uma gaveta secreta para guardá-las por um tempo e, quando você estiver pronto, pegar tudo de volta e continuar escrevendo.

### O Que o **git stash** Faz?

- **Guarda as Alterações Temporariamente:** Ele salva todas as mudanças que você fez, mas que ainda não estão prontas para serem registradas definitivamente (commit).
- **Permite Trocar de Projeto sem Perder o Trabalho:** Assim, você pode mudar para outro branch (ou caderno) sem perder o que estava escrevendo.
- **Facilita a Retomada:** Quando você quiser voltar ao seu trabalho, é só retirar essas alterações guardadas.

### Exemplo Prático

1. **Você está escrevendo em um arquivo chamado `historia.txt`:**
   - Mas, antes de terminar, você precisa mudar para outro branch para testar uma ideia nova.

2. **Guardar as alterações com o git stash:**
   - No terminal, você digita:
     ```
     git stash
     ```
   - Isso coloca todas as mudanças que você fez num "envelope" seguro, guardado em uma gaveta secreta.

3. **Mudar para outro branch e trabalhar nele:**
   - Você pode mudar para outro branch sem perder suas alterações guardadas.

4. **Retomar suas alterações:**
   - Quando estiver pronto para continuar sua história, você usa:
     ```
     git stash apply
     ```
   - Assim, o Git retira as alterações do "envelope" e as coloca de volta no seu projeto.

### Por Que Usar o **git stash**?

- **Organização:** Permite que você guarde seu trabalho inacabado sem precisar finalizar ou cometer as alterações imediatamente.
- **Flexibilidade:** Dá a liberdade de experimentar novas ideias sem perder o que você já estava escrevendo.
- **Segurança:** Suas alterações ficam guardadas até que você esteja pronto para retomar o trabalho.

Resumindo, o **git stash** é como uma gaveta secreta onde você guarda temporariamente as páginas da sua história, permitindo que você mude de ideia e depois volte a continuar de onde parou!

# git remote
Imagine que você tem um caderno onde escreve suas histórias, e também uma cópia desse caderno que fica guardada na biblioteca da escola para que seus amigos possam ler. O comando **git remote** é como uma lista de contatos que mostra onde as versões online do seu caderno estão armazenadas.

### O Que o **git remote** Faz?

- **Lista Conexões Remotas:** Mostra os "endereços" (URLs) dos repositórios que estão na internet, onde sua história também está guardada.
- **Adiciona Novos Endereços:** Permite que você conecte seu projeto a um repositório online, como no GitHub.
- **Gerencia Conexões:** Você pode ver, renomear ou remover essas conexões se precisar.

### Exemplo Prático

1. **Você tem sua história em um projeto e criou uma cópia online:**
   - Por exemplo, você criou um repositório no GitHub chamado **meu-projeto**.

2. **Adicionar a conexão remota:**
   - No terminal, você digita:
     ```
     git remote add origin https://github.com/usuario/meu-projeto.git
     ```
   - Isso diz ao Git: "Além do meu caderno em casa, guarde também uma cópia desse caderno na biblioteca (GitHub), que vou chamar de **origin**."

3. **Verificar os repositórios remotos:**
   - Para ver essa lista de endereços, use:
     ```
     git remote -v
     ```
   - O Git mostrará algo como:
     ```
     origin  https://github.com/usuario/meu-projeto.git (fetch)
     origin  https://github.com/usuario/meu-projeto.git (push)
     ```

### Por Que Usar o **git remote**?

- **Organização:** Mantém uma lista dos lugares onde sua história (projeto) está armazenada.
- **Compartilhamento e Colaboração:** Permite que você envie suas atualizações para a versão online (com **git push**) ou receba mudanças feitas por amigos (com **git pull**).
- **Backup:** Garante que sua história esteja salva não só no seu computador, mas também online, protegendo seu trabalho.

Assim, o **git remote** é como uma lista de endereços que mostra onde sua história está guardada na internet, facilitando o compartilhamento, a colaboração e o backup do seu trabalho!
