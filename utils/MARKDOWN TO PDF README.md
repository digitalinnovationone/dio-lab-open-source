# 💻 Utilitário de Conversão de README.md para PDF

Este utilitário permite que você converta arquivos `README.md` hospedados no GitHub em arquivos PDF de forma simples e rápida.

## Pré-requisitos

- Node.js instalado na sua máquina. Você pode baixar e instalar a partir de [nodejs.org](https://nodejs.org/).
- Acesso à internet para buscar o conteúdo do arquivo `README.md` no GitHub.

## Como Usar

### Passo 1: Clone o Repositório

Primeiro, clone o repositório do projeto para sua máquina:

```bash
git clone https://github.com/DavigfxSs/dio-lab-open-source.git
cd dio-lab-open-source
```
Após obter sua versão do repositório no repositório local, abra o terminal do node e insira o codigo abaixo

```
node utils/markdown/markdown_to_pdf.js 
https://raw.githubusercontent.com/digitalinnovationone/dio-lab-open-source/refs/heads/main/community/DavigfxSs.md meu_readme.pdf

```
ps important!: o link https precisa ser o raw do seu arquivo md no repositório remoto.

## 🔗 Como pegar o link do seu raw
Passo 1: Acesse o repositório da [DIO](https://github.com/digitalinnovationone/dio-lab-open-source).

Passo 2: Procure pelo seu aquivo README na pasta Comunnity.

Passo 3: clique nele e procure o botão **raw** para abrir o codigo no navegador.

Passo 4: O url que estiver disponivel para copiar acima deve ser guardado para usar no lugar do https exemplo.

## 🗃️ PDF
O pdf vai gerado com o nome: meu_readme.pdf

você pode alterar o nome antes de executar o codigo

será gerado o arquivo pdf dentro da pasta raiz.


