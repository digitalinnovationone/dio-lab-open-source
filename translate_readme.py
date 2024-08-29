from googletrans import Translator

translator = Translator()

# Leitura do README.md original
with open('README.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Função para traduzir e salvar o conteúdo
def translate_and_save(content, dest_lang, filename):
    translated = translator.translate(content, dest=dest_lang).text
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(translated)

# Traduções para várias línguas
translate_and_save(content, 'en', 'README_en.md')
translate_and_save(content, 'es', 'README_en.md')
translate_and_save(content, 'fr', 'README_fr.md')
translate_and_save(content, 'zh-cn', 'README_zh.md')
translate_and_save(content, 'ko', 'README_ko.md')
translate_and_save(content, 'ru', 'README_ru.md')
translate_and_save(content, 'de', 'README_de.md')
translate_and_save(content, 'pt', 'README_pt.md')
