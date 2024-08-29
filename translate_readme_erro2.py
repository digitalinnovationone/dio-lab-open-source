from translate import Translator  
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
        translator = Translator(to_lang=idioma_destino)  
        traducao = ""  
        # Dividir o conteúdo em partes de até 500 caracteres  
        partes = [conteudo[i:i+500] for i in range(0, len(conteudo), 500)]  
        for parte in partes:  
            traducao += translator.translate(parte)  
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
    'ko': 'README_ko.md'  
}  

# Traduzir e salvar o conteúdo em novos arquivos  
for idioma, caminho_saida in idiomas.items():  
    conteudo_traduzido = traduzir_conteudo(conteudo_original, idioma)  
    if conteudo_traduzido:  
        escrever_arquivo(caminho_saida, conteudo_traduzido)  
        print(f'Tradução para {idioma} concluída e salva em {caminho_saida}')  
    else:  
        print(f"Não foi possível traduzir o conteúdo para o idioma {idioma}")