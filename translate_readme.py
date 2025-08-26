## Desenvolvido por Luciano Eugênio Schiavon 
## e-mail: luciano@redescorporativas.com.br
## Data: 29-08-2024 Hora: 02:47:00
## Whatsapp: (44) 99946-4300

# Essa função conecta na api do Google e traduz arquivo automaticamente
# para diversas linguagens.

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
    try:  
        translator = Translator()  
        traducao = ""  
        # Dividir o conteúdo em partes de até 4000 caracteres 
        # Importante incluir essa parte porque trata erro de limite de caracter e assim
        # divido em partes de 4000 para obter retorno da API do google
        partes = [conteudo[i:i+4000] for i in range(0, len(conteudo), 4000)]  
        for parte in partes:  
            traducao += translator.translate(parte, dest=idioma_destino).text  
        return traducao  
    except Exception as e:  
        print(f"Erro ao traduzir o conteúdo: {e}")  
        return None  

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
    'ko': 'README_ko.md',
    'fr': 'README_fr.md'
}  

# Traduzir e salvar o conteúdo em novos arquivos  
for idioma, caminho_saida in idiomas.items():  
    conteudo_traduzido = traduzir_conteudo(conteudo_original, idioma)  
    if conteudo_traduzido:  
        escrever_arquivo(caminho_saida, conteudo_traduzido)  
        print(f'Tradução para {idioma} concluída e salva em {caminho_saida}')  
    else:  
        print(f"Não foi possível traduzir o conteúdo para o idioma {idioma}")