def classificar_temperatura(temp):
    if temp < 35:
        return "Hipotermia"
    elif 35 <= temp <= 37.5:
        return "Normal"
    elif 37.6 <= temp <= 39:
        return "Febre leve"
    else:
        return "Febre alta"

def classificar_batimentos(bpm):
    if bpm < 60:
        return "Bradicardia"
    elif 60 <= bpm <= 100:
        return "Normal"
    else:
        return "Taquicardia"

def classificar_pressao(pressao):
    if pressao < 10.1:
        return "Baixa"
    elif 10.1 <= pressao <= 14:
        return "Normal"
    else:
        return "Alta"

def classificar_atendimento(temp_status, bpm_status, pressao_status):
    if temp_status == "Normal" or temp_status == "Febre leve":
        if bpm_status == "Normal" and pressao_status == "Normal":
            return "Atendimento Normal"
    if temp_status == "Febre alta" and bpm_status == "Taquicardia" and pressao_status == "Alta":
        return "Atendimento Grave"
    if temp_status == "Hipotermia" and bpm_status == "Bradicardia" and pressao_status == "Baixa":
        return "Atendimento Urgente"
    return "Caso fora dos padrões específicos (avaliar clinicamente)"

# Entrada de dados
try:
    pressao = float(input("Informe sua pressão arterial (ex: 12.5): "))
    temperatura = float(input("Informe sua temperatura corporal em °C (ex: 36.7): "))
    batimentos = int(input("Informe seus batimentos cardíacos por minuto (BPM): "))

    # Classificações
    temp_status = classificar_temperatura(temperatura)
    bpm_status = classificar_batimentos(batimentos)
    pressao_status = classificar_pressao(pressao)

    # Exibição dos resultados
    print("\n--- RESULTADO DA AVALIAÇÃO ---")
    print(f"Temperatura: {temperatura}°C - {temp_status}")
    print(f"Batimentos Cardíacos: {batimentos} BPM - {bpm_status}")
    print(f"Pressão Arterial: {pressao} - {pressao_status}")
    print(f"Classificação Geral: {classificar_atendimento(temp_status, bpm_status, pressao_status)}")

except ValueError:
    print("Erro: por favor, insira valores numéricos válidos.")
