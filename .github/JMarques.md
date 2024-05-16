Como enviar um repositório para o GitHub
Vou dividir esta seção em etapas para ajudá-lo a entender o processo com mais clareza.

Passo 1 – Crie uma conta no GitHub
Para poder usar o GitHub, terá de criar uma conta primeiramente. Você pode fazer isso no site da web do GitHub.

Passo 2 – Crie um repositório
Você pode clicar no símbolo + no canto superior direito da página e escolher "New repository" (Novo repositório). Dê um nome ao seu repositório, role para baixo e clique no botão "Create repository" (Criar repositório).

Passo 3 – Adicionar e confirmar arquivos
Antes de "adicionar" e "confirmar" nossos arquivos, você precisa entender os estágios de um arquivo que está sendo rastreado pelo Git.

Estado confirmado (committed)
Um arquivo está no estado confirmado quando todas as alterações feitas no arquivo foram salvas no repositório local. Os arquivos no estágio confirmado são arquivos prontos para serem enviados para o repositório remoto (no GitHub).

Estado modificado (modified)
Um arquivo no estado modificado tem algumas alterações feitas nele, mas ainda não foi salvo. Isso significa que o estado do arquivo foi alterado de seu estado anterior no estado confirmado.

Estado preparado (staged)
Um arquivo no estado preparado significa que está pronto para ser confirmado. Nesse estado, todas as alterações necessárias foram feitas. Portanto, o próximo passo é mover o arquivo para o estado de confirmação.

Você pode entender isso melhor imaginando o Git como uma câmera. A câmera só tirará um instantâneo quando o arquivo atingir o estado de confirmação. Após este estado, a câmera começa a comparar as alterações feitas no mesmo arquivo com o último instantâneo (este é o estado modificado). Quando as alterações necessárias forem feitas, o arquivo é preparado e movido para o estado de confirmação para um novo instantâneo.

Isso pode ser muita informação para absorver no momento, mas não desanime – fica mais fácil com a prática.
