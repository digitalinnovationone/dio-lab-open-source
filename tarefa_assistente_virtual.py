"""Este é um sistema de assistema virtual, projeto do Bootcamp da DIo e Bairesdev
  Estou fazendo alterações para criar um sistema virtual para ajudar idosos em suas rotinas.
  Algumas considerações importantes:
  1- Não utilizei a biblioteca ipython, utilizei a pygame e a speech_recognition, alterei o idioma para português
  2- Foi testado todas as funcionalidades!
  3- Validei todas as funções (Youtube, Pesquisa/Wikipedia, Piada,), removi a função music
  4- Adicionei a função: Google (para pesquisa)
  5- Adicionei a função "Uber". Connvivo com vários idosos e percebo que todos tem dificuldade 
    de utilizar o aplicativo da Uber, por isso, fiz integração com a API do Uber Developer e consegui 
    chamar o uber pelo assistente. Próximo passo é fazer a integração com a API do Google maps, 
    para passar as coodenadas corretamente da origem e do destino da viagem, por hora, utilizei dados ficticios.
 7- Pretendo adicionar ainda outras funcionalidades a esse sistema, como a pesquisa de produtos, projeto anterior da DIO.
"""
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import pyjokes
import wikipedia
import webbrowser
from pygame import mixer
import time
import requests

# Configurar Wikipedia em português
wikipedia.set_lang("pt")

# Configurações do Uber (client_id e client_secret são gerados no site de desenvolvedor da Uber)
CLIENT_ID = 'okXKm_hkf3YsSDwtt6DJx4SA2r0eV5qT'
CLIENT_SECRET = 'NBBLX2dFI2byBfAm_IuOBEKWOP6TUuyrlTVj2ytu'
REDIRECT_URI = "https://teiabessa.github.io/callback"
SCOPE = 'rides.request'

# Função para capturar o áudio do usuário
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='pt-BR')  # Reconhecimento em português
            print(said)
        except sr.UnknownValueError:
            speak("Desculpe, não entendi. Pode repetir?")
            said = get_audio()
        except sr.RequestError:
            speak("Desculpe, o serviço está indisponível")
    return said.lower()

# Função para falar o texto
def speak(text):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(os.path.dirname(__file__), f"voz_{timestamp}.mp3")
    
    tts = gTTS(text=text, lang='pt-br')  # Voz em português brasileiro
    tts.save(filename)
    
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    
    while mixer.music.get_busy():
        time.sleep(0.1)
    
    mixer.music.stop()
    mixer.quit()
    try:
        os.remove(filename)
    except Exception as e:
        print(f"Erro ao apagar arquivo: {e}")

# Função para perguntar o endereço de origem ou destino ao usuário (targetu)
def get_address_from_user(prompt, targetu):
    speak(f"Você prefere Falar ou Escrever o seu endereço de {targetu}?")

    choice = get_audio()
    frase_speak="Por favor, diga o endereço de " + targetu + " ?"
    if 'falar' in choice or 'fala' in choice:        
        speak(frase_speak)
        address = get_audio()  # Captura o endereço falado
    elif 'escrever' in choice or 'escreve' in choice:
        address= input(frase_speak)  # Captura o endereço digitado
        speak(f"Então o seu endereço de {targetu} é {address}")
    else:
        speak("Opção inválida. Vamos tentar novamente...")
        address = get_address_from_user(prompt, targetu)  # Rechama a função caso o reconhecimento falhe
    
    return address

# Função para obter coordenadas a partir do endereço
def get_coordinates_from_address(address):
    # Futuramente usarei uma API de Geolocalizacao do Google Maps como o Geocoding para obter as coordenadas a partir do endereço.
    # AQui usando dados fictício. 
  
    return (37.7759792, -122.41823)  # Retorne as coordenadas reais dependendo da implementação da API.

# Função para obter a localização atual do dispositivo
def get_current_location():
    # Aqui estamos apenas simulando uma localização fictícia.
    return (37.7759792, -122.41823)

# Função para obter o token de acesso da API do uber developer
def get_uber_access_token():
    url = "https://auth.uber.com/oauth/v2/token"
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'scope': SCOPE
    }
    response = requests.post(url, data=data)
   
    if response.status_code == 200:
        return response.json().get('access_token')
    else:        
        speak("Erro ao obter token de acesso do Uber")
        return None

# Função para chamar um Uber
def call_uber():
    speak("Você gostaria de usar sua localização atual como origem? (Sim ou Não)")
    response = get_audio()
    #localizacao atual
    if 'sim' in response:
        # Obtém a localização atual do dispositivo
        current_location = get_current_location()
        if current_location:
            start_latitude, start_longitude = current_location
            #comentei o codigo abaixo pois ainda irei fazer a integração com a api do google maps
            #speak(f"Sua localização atual é latitude: {start_latitude} e longitude: {start_longitude}. Isso está correto?")
            confirmation="sim"
            #confirmation = get_audio()
            if 'sim' not in confirmation:
                start_address = get_address_from_user("Qual é o seu endereço de" , "origem")
                coordinates = get_coordinates_from_address(start_address)
                if coordinates:
                    start_latitude, start_longitude = coordinates
            else:
                speak("Ótimo! Vamos definir o destino.")
        else: #nao 
            start_address = get_address_from_user("Qual é o seu endereço de", "origem")
            coordinates = get_coordinates_from_address(start_address)
            if coordinates:
                start_latitude, start_longitude = coordinates
    else: #usuario nao esta na localizacao atual
        start_address = get_address_from_user("Qual é o seu endereço de", "origem")
        coordinates = get_coordinates_from_address(start_address)
        if coordinates:
            start_latitude, start_longitude = coordinates

    # Pergunta ao usuário o destino
    speak("Qual é o seu destino?")
    #chama a função passando como parametro destino
    
    destination_address = get_address_from_user("Qual é o seu endereço", "destino")
    destination_coordinates = get_coordinates_from_address(destination_address)
    
    if destination_coordinates:
        end_latitude, end_longitude = destination_coordinates
        # Solicita o Uber
        token = get_uber_access_token()
        if not token:
            return
    #estrutura becessaria para fazer integração à API do Uber
        
        url = "https://api.uber.com/v1.2/requests"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            "start_latitude": start_latitude,
            "start_longitude": start_longitude,
            "end_latitude": end_latitude,
            "end_longitude": end_longitude
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 202:
            speak("Uber solicitado com sucesso")
        else:
            speak("Falha ao solicitar o Uber")

# Função para responder aos comandos do usuário
def respond(text):
    print("Texto reconhecido: " + text)
    
    if 'youtube' in text:
        speak("O que você quer pesquisar no YouTube?")
        keyword = get_audio()
        if keyword:
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Aqui estão os resultados para {keyword} no YouTube")
    elif 'google' in text:
        speak("O que quer pesquisar no Google?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.google.com/search?q={keyword}"
            webbrowser.get().open(url)
            speak(f"Aqui estão os resultados para {keyword} no Google")
    #pesquisa no wikipidia
    elif 'pesquisa' in text or 'wikipedia' in text:
        speak("O que você quer pesquisar?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("De acordo com wikipedia")
            print(result)
            speak(result)
    elif 'piada' in text:
        try:
            joke = pyjokes.get_joke(language='pt')  # Algumas piadas em português
        except:
            joke = pyjokes.get_joke()  # Caso não tenha em português
        speak(joke)
    elif 'que horas são' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    
    elif 'uber' in text:   
        speak("Chamarei seu uber!")     
        call_uber()        
    elif 'sair' in text or 'desligar' in text:
        speak("Até logo! Estarei aqui se precisar")
        exit()


# Função principal
if __name__ == "__main__":
    speak("Olá! Como posso ajudar?")
    while True:
        print("Escutando...")
        text = get_audio()
        respond(text)

