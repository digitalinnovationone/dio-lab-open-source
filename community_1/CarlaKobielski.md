Lista de comandos essenciais do Git e do GitHub, incluindo alguns menos conhecidos, mas úteis, que podem facilitar seu trabalho no controle de versão e colaboração em projetos de desenvolvimento.


 Comandos Git:

| Comando                                               | Descrição                                                                                    |
|-------------------------------------------            |--------------------------------------------------------------------------------------------- |
| `git bisect`                                          | Ajuda a encontrar o commit que introduziu um bug, utilizando uma pesquisa binária.           |
| `git cherry-pick <commit>`                            | Aplica as mudanças de um commit específico para a branch atual.                              | 
| `git reflog`                                          | Mostra um registro de referências de HEAD, útil para recuperar commits "perdidos".           |
| `git stash`                                           | Salva temporariamente as mudanças não cometidas para aplicá-las posteriormente.              |
| `git blame <arquivo>`                                 | Mostra quem modificou cada linha de um arquivo, e em que commit a modificação foi feita.     |
| `git archive --format=zip --output=<arquivo.zip> HEAD`| Cria um arquivo zip do estado atual do repositório.                                          |
| `git submodule`                                       | Permite trabalhar com repositórios dentro de repositórios, útil para gerenciar dependências. |

 Comandos GitHub:

| Comando                                             | Descrição                                                                                    |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------- |
| `hub create`                                        | Cria um novo repositório diretamente do terminal, com suporte a opções avançadas.            |
| `hub pull-request -b <base_branch>`                 | Cria uma solicitação de pull especificando a branch base.                                    |
| `hub issue`                                         | Cria uma nova issue diretamente do terminal, com suporte a opções avançadas.                 | 
| `hub compare <branch1> <branch2>`                   | Mostra uma comparação entre duas branches.                                                   |
| `hub release create <tag> -a <arquivo.zip>`         | Cria um novo release no GitHub, com um arquivo anexado.                                      |
| `hub browse`                                        | Abre o repositório no navegador padrão.                                                      | 
| `hub fork --remote-name=<nome_do_remote> <repo>`    | Faz um fork do repositório especificado, com controle sobre o nome do remote.                |
| `hub ci-status`                                     | Mostra o status do último build CI para o repositório.                                       |

