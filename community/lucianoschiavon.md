
# Currículo de Luciano Eugênio Schiavon

https://redescorporativas.com.br/capacidadetecnica.pdf

## Título do Projeto

Uma breve descrição sobre o que esse projeto faz e para quem ele é.

Inclui traduções automáticas do seu README.md para várias línguas, como inglês, francês, chinês, coreano, russo, alemão, você pode seguir os passos abaixo.

Vamos usar o GitHub Actions junto com a API do Google Translate para automatizar esse processo.

Passo 1: Configurar o Repositório.

Crie um repositório no GitHub:
Se ainda não tiver um, crie um novo repositório no GitHub e inicialize-o com um README.md.

Clone o repositório localmente:
git clone https://github.com/seu-usuario/seu-repositorio.git


Passo 2: Criar o Script de Tradução.

Crie um script Python para traduzir o README.md

Crie um arquivo chamado translate_readme.py no diretório raiz do seu projeto e adicione o código abaixo.

## ## Desenvolvido por Luciano Eugênio Schiavon 
## ## e-mail: luciano@redescorporativas.com.br
## ## Data: 29-08-2024 Hora: 02:47:00
## ## Whatsapp: (44) 99946-4300

### ## Essa função conecta na api do Google e traduz arquivo automaticamente para diversas linguagens.


from googletrans import Translator  
import os  

### ## Função para ler o conteúdo do arquivo README.md  
def ler_arquivo(caminho):  
    with open(caminho, 'r', encoding='utf-8') as arquivo:  
        return arquivo.read()  

### ## Função para escrever o conteúdo traduzido em um novo arquivo 

def escrever_arquivo(caminho, conteudo):  
    with open(caminho, 'w', encoding='utf-8') as arquivo:  
            arquivo.write(conteudo)  

### ## Função para traduzir o conteúdo  

def traduzir_conteudo(conteudo, idioma_destino):  
    try:  
        translator = Translator()  
        traducao = ""  

### ## Dividir o conteúdo em partes de até 4000 caracteres. Importante incluir essa parte porque trata erro de limite de caracter e assim divido em partes de 4000 para obter retorno da API do google
        partes = [conteudo[i:i+4000] for i in range(0, len(conteudo), 4000)]  
        for parte in partes:  
            traducao += translator.translate(parte, dest=idioma_destino).text  
        return traducao  
    except Exception as e:  
        print(f"Erro ao traduzir o conteúdo: {e}")  
        return None  

### ## Caminho do arquivo README.md original  
caminho_readme = 'README.md'  

### ## Ler o conteúdo do arquivo README.md  
conteudo_original = ler_arquivo(caminho_readme)  

### ## Idiomas para os quais queremos traduzir  
idiomas = {  
    'en': 'README_en.md',  
    'es': 'README_es.md',  
    'zh-cn': 'README_zh.md',  
    'ja': 'README_ja.md',  
    'ko': 'README_ko.md'  
}  

### ## Traduzir e salvar o conteúdo em novos arquivos

for idioma, caminho_saida in idiomas.items():
  
    conteudo_traduzido = traduzir_conteudo(conteudo_original, idioma)  
    
    if conteudo_traduzido:  
        escrever_arquivo(caminho_saida, conteudo_traduzido)  
        print(f'Tradução para {idioma} concluída e salva em {caminho_saida}')  
    
    else:  
        print(f"Não foi possível traduzir o conteúdo para o idioma {idioma}")

# Instale a biblioteca googletrans:

pip install googletrans==4.0.0-rc1

### Passo 3: Configurar GitHub Actions

Crie um diretório .github/workflows:

mkdir -p .github/workflows

### Crie um arquivo de workflow:

### Crie um arquivo chamado 

translate.yml

Dentro do diretório .github/workflows.

## Adicione no arquivo

name: Translate README

on:
  push:
    branches:
      - main

jobs:
  translate:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install googletrans==4.0.0-rc1

      - name: Translate README
        run: python translate_readme.py

      - name: Commit and push changes
        run: |
          git config --global user.name 'github-actions'
          git config --global user.email 'github-actions@github.com'
          git add README_en.md README_fr.md README_zh.md README_ko.md README_ru.md README_de.md README_pt.md
          git commit -m 'Add translated README files'
          git push

Passo 4: Commit e Push

### Adicione e commite os arquivos:

git add .

git commit -m "Setup translation workflow"

### Faça o push para o GitHub:

git push origin main

### Estrutura Final do Repositório
Seu repositório deve ter a seguinte estrutura:

seu-repositorio/

├── .github/

│   └── workflows/

│       └── translate.yml

├── translate_readme.py

├── README.md

├── README_en.md

├── README_fr.md

├── README_zh.md

├── README_ko.md

├── README_ru.md

├── README_de.md

└── README_pt.md

Com isso, toda vez que você fizer um push para a branch main, o GitHub Actions irá executar o script de tradução e atualizar os arquivos README em várias línguas automaticamente.