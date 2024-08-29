from googletrans import Translator
import os

# Função para ler o conteúdo do arquivo README.md
def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

# Função para escrever o conteúdo traduzido em um novo arquivo
def escrever_arquivo(caminho, conteudo):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

# Função para traduzir o conteúdo
def traduzir_conteudo(conteudo, idioma_destino):
    translator = Translator()
    traducao = translator.translate(conteudo, dest=idioma_destino)
    return traducao.text

# Caminho do arquivo README.md original
caminho_readme = 'README.md'

# Ler o conteúdo do arquivo README.md
conteudo_original = ler_arquivo(caminho_readme)

# Idiomas para os quais queremos traduzir
idiomas = {
    'en': 'README_en.md',
    'es': 'README_es.md',
    'zh-cn': 'README_zh.md',
    'ja': 'README_ja.md',
    'ko': 'README_ko.md'
}

# Traduzir e salvar o conteúdo em novos arquivos
for idioma, caminho_saida in idiomas.items():
    conteudo_traduzido = traduzir_conteudo(conteudo_original, idioma)
    escrever_arquivo(caminho_saida, conteudo_traduzido)
    print(f'Tradução para {idioma} concluída e salva em {caminho_saida}')
