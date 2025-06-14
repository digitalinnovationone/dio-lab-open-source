def perguntar_obrigatorio(campo, min_chars=1, max_chars=100, apenas_numeros=False):         # Cria a função perguntar_obrigatorio com os parâmetros campo, min_chars, max_chars e apenas_numeros 
    while True:                                                                             # Loop infinito para garantir que o usuário preencha corretamente
        resposta = input(f"{campo}: ").strip()                                              # Pede ao usuário para preencher o campo e remove espaços em branco (campo obrigatorio)
        if resposta == "":                                                                  # Verifica se o campo estiver vazio
            print("⚠️ Campo obrigatório. ⚠️")                                              # Mensagem de erro se o campo estiver vazio          
        elif len(resposta) < min_chars:                                                     # Verifica se o tamanho da resposta é menor que o mínimo (1 caractere)
            print(f"⚠️ O campo deve ter no mínimo {min_chars} caracteres. ⚠️")             # Mensagem de erro se o campo for menor que o mínimo 
        elif len(resposta) > max_chars:                                                     # Verifica se o tamanho da resposta é maior que o máximo (100 caracteres)
            print(f"⚠️ O campo deve ter no máximo {max_chars} caracteres. ⚠️")             # Mensagem de erro se o campo for maior que o máximo
        elif apenas_numeros and not resposta.isdigit():                                     # Verifica se o campo deve conter apenas números e se a resposta não é um número (apenas_numeros=True)
            print("⚠️ Este campo deve conter apenas números. ⚠️")                          # Mensagem de erro se o campo não for um número
        else:                                                                               # Se todas as condições acima forem atendidas
            return resposta                                                                 # Retorna a resposta do usuário


def perguntar_numero(campo):                                                                # Cria a função perguntar_numero com o parâmetro campo
    while True:                                                                             # Loop infinito para garantir que o usuário preencha corretamente
        resposta = input(f"{campo}: ").strip()                             # Pede ao usuário para preencher o campo e remove espaços em branco (campo obrigatorio) strip() remove espaços em branco no início e no final
        if resposta.isdigit():                                                              # Verifica se a resposta é um número (apenas_numeros=True)
            return int(resposta)                                                            # Retorna a resposta do usuário convertida para inteiro
        else:                                                                               # Se a resposta não for um número
            print("⚠️ Este campo deve ser um número. Tente novamente. ⚠️")                 # Mensagem de erro se o campo não for um número
            
def perguntar_sexo(campo="Sexo?"):                                                          # Cria a função perguntar_sexo com o parâmetro campo
    while True:                                                                             # Loop infinito para garantir que o usuário preencha corretamente
        resposta = input(f"{campo} (masculino/feminino):").strip().lower()        # Pede ao usuário para preencher o campo e remove espaços em branco (campo obrigatorio) lower() converte a resposta para minúsculas
        if resposta in ['masculino', 'feminino']:                                           # Verifica se a resposta é 'masculino' ou 'feminino'
            return resposta                                                                 # Retorna a resposta do usuário
        else:                                                                               # Se a resposta não for 'masculino' ou 'feminino' 
            print("⚠️️ Preencha somente com 'masculino' ou 'feminino'.⚠️")                  # Mensagem de erro se o campo não for 'masculino' ou 'feminino'
                
palavra_chave_qualidades = {                                                                                             # Dicionário com palavras-chave para identificar qualidades
    "empatia": ["ouvir", "ajudar", "entender", "pessoas", "sensível", "compreensivo", "gentil", "relacionar"],
    "comunicação": ["conversar", "falar", "explicar", "comunicar", "expressar", "dialogar"],
    "criatividade": ["ideia", "inovar", "criativo", "diferente", "solução", "novo"],
    "organização": ["organizar", "planejar", "agenda", "horário", "metódico"],                                           # O que se encontra dentro do [] é o que o usuário pode digitar para identificar a qualidade 
    "foco": ["concentrar", "atenção", "focado", "distrações", "determinado"],
    "ética": ["honestidade", "respeito", "integridade", "moral", "valores"],
    "adaptação": ["flexível", "mudança", "ajustar", "adaptar", "novas situações"],
    "dedicação": ["esforço", "comprometido", "trabalhar", "dedicar", "aplicado"],
    "disciplina": ["disciplina", "cumprir", "regras", "organização", "metódico"],
    "iniciativa": ["tomar", "iniciativa", "agir", "resolver", "antecipar"],
    "proatividade": ["antecipar", "resolver", "agir", "adiantar", "iniciativa"],
    "resiliência": ["superar", "pressão", "persistência", "adversidade", "resistir"],
    "trabalho em equipe": ["colegas", "grupo", "ajudar", "time", "colaborar", "equipe"],
    "responsabilidade": ["pontual", "compromisso", "dever", "responsável", "cumprir"],
    "perfeccionista": ["perfeito", "caprichoso", "cuidadoso", "detalhista", "exigente", "rigoroso"]
}
def identificar_qualidade(frase_usuario):
    frase = frase_usuario.lower()
    for qualidade, palavras in palavra_chave_qualidades.items():
        for palavra in palavras:
            if palavra in frase:
                return qualidade
    return None
    
print("\n🔹 Seja bem vindo!!!")

nome = perguntar_obrigatorio("Qual é o seu nome completo?", 5, 50).title()
print(f"Olá, {nome}!")

print("\n🔹 Está é uma entrevista de emprego guiada por um bot em projeto ainda sendo desenvolvido. Vamos começar!")

print("\n🔹 Dados pessoais:")

data_de_nascimento = perguntar_numero("Data de nascimento?")
cpf = perguntar_numero("CPF?(Sem pontos)")
rg = perguntar_obrigatorio("RG?(Sem pontos)", 5, 15, apenas_numeros=True)
nacionalidade = perguntar_obrigatorio("Nacionalidade?").strip().lower()
sexo = perguntar_sexo("Sexo?").strip().lower()
cidade_nascimento = perguntar_obrigatorio("Cidade de nascimento?").strip().lower()
cidade_atual = perguntar_obrigatorio("Cidade atual?").strip().lower()
telefone = perguntar_obrigatorio("Telefone?", 11, 11, apenas_numeros=True)
email = perguntar_obrigatorio("Email?").strip().lower()
endereco = perguntar_obrigatorio("Endereço?").strip().lower()
estado_civil = perguntar_obrigatorio("Estado civil?").strip().lower()

print("\n🔹 Historico profissionais:")

primeiro_emprego = perguntar_obrigatorio("Qual foi seu primeiro emprego?").strip().lower()
ultimo_emprego = perguntar_obrigatorio("Ultimo emprego?").strip().lower()

quanto_tempo = input("Quanto tempo ficou na ultima empresa? (Em anos ou meses) ")
partes = quanto_tempo.split()           # Divide a entrada do usuário
quantidade = int(partes[0])             # Converte a primeira parte (número) para inteiro
unidade = partes[1]                     # A segunda parte (ano ou mês) fica como string

porque_saiu = perguntar_obrigatorio("Porque saiu?").strip().lower()
ultimo_cargo = perguntar_obrigatorio("Ultimo cargo?(Ex: Auxiliar de RH, Operador de Máquinas, Analista de Vendas)").strip().lower()

print("\n🔹 Competencias")

faz_bem = perguntar_obrigatorio("O que sabe fazer bem?").strip().lower()
area_de_trabalho = perguntar_obrigatorio("Qual sua área de trabalho?(Ex: Logística, RH, TI, Produção)").strip().lower()
nivel_conhecimento = perguntar_numero(f"Qual seu nivel de conhecimento na {area_de_trabalho} ? Escala de 1 a 10")

print("\n🔹 Pontos fortes e fracos")

qualidade = perguntar_obrigatorio("Sua melhor qualidade?").strip().lower()

qualidade_identificada = identificar_qualidade(qualidade)

if qualidade_identificada:
    print(f"Identificamos que você possui a qualidade: {qualidade_identificada.title()}")
else:
    print("Qualidade neutra ou não reconhecida.")
    
defeito = perguntar_obrigatorio("Seu maior defeito?").strip().lower()
melhorar_defeito = perguntar_obrigatorio("Como pretende melhorar seu defeito?").strip().lower()

print("\n🔹 Objetivos e expectativas")

motivo = perguntar_obrigatorio("Porque quer trabalhar aqui?").strip().lower()
objetivo = perguntar_obrigatorio("Qual seu objetivo profissional?").strip().lower()
expectativa = perguntar_obrigatorio("Qual sua expectativa na empresa?").strip().lower()
cinco_anos = perguntar_obrigatorio("Onde se vê em 5 anos?").strip().lower()

import time 
for i in range(1,4): 
    print(f"\rAnalisando{'.' * i}", end="")
    time.sleep(1) 

for i in range(1,10):
    print(f"\rCarregando {'▓'*i}", end="")
    time.sleep(1)
    
print()

if int(nivel_conhecimento) >= 8:
    print("Bom conhecimento na sua área de trabalho.")
elif int(nivel_conhecimento) >= 5:
    print("Conhecimento razoável na sua área de trabalho.")
elif int(nivel_conhecimento) >= 1:
    print("Conhecimento básico na sua área de trabalho.")
else:
    print("Não preencheu o campo de conhecimento.")

if (quantidade) >= 5:
    print("Experiência profissional sólida.")
elif int(quantidade) == 2:
    print("Experiência profissional razoável.")
elif int(quantidade) <= 1:
    print("Experiência profissional básica.")
else:
    print("Não preencheu o campo de experiência profissional.")

qualidade = {
    "dedicação": "✅ Excelente comprometimento com tarefas.",
    "responsabilidade": "✅ Demonstra maturidade profissional.",
    "empatia": "✅ Sabe lidar bem com pessoas.",
    "criatividade": "✅ Boa para cargos que exigem inovação.",
    "organização": "✅ Boa gestão do tempo e processos.",
    "proatividade": "✅ Toma iniciativa e resolve problemas rapidamente.",
    "foco": "✅ Mantém-se concentrado mesmo com distrações.",
    "ética": "✅ Age com honestidade e respeito.",
    "adaptação": "✅ Se adapta rapido a qualquer emprego ou situação."
    }