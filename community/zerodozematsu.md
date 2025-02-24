Projetos em C
Pequenos projetos e testes simples em linguagem C.
Descrição:
Os programas apresentados neste repositório são apenas projetos simples e testes escritos na linguagem C.
Os programas contidos neste repositório não devem ser levados "a sério", isto é, não possuem muita utilidade prática no dia-a-dia a não ser o aprendizado e o entendimento de como a linguagem C funciona e suas sintaxes.
Os programas aqui contidos foram desenvolvidos pensando na plataforma Linux e UNIX em geral, podendo não funcionar na plataforma Windows!
Programas:
OlaMundo - Programa de Saudação 'Avançado'!
Todo desenvolvedor ou aspirante a desenvolvedor, ao aprender uma nova linguagem de programação, sempre começa com uma aplicação simples para entender como a sintaxe da linguagem funciona.
Com a linguagem C não é diferente, mas decidi 'extrapolar' um pouco neste quesito. Decidi então criar o OlaMundo disponível em linguas diferentes: Português, Inglês, Espanhol, entre outros.
Aqui estão os possíveis argumentos que poderão ser inseridos na hora de executar o programa:
  Ajuda:
  '--help' ou '-h': Mostra a opção de ajuda.
  
  Saudações:
  '--pt' ou '-1': Saudação em português.
  '--en' ou '-2': Saudação em inglês.
  '--es' ou '-3': Saudação em espanhol.
  '--fr' ou '-4': Saudação em francês.
  '--it' ou '-5': Saudação em italiano.
  '--de' ou '-6': Saudação em alemão.
  '--jp' ou '-7': Saudação em japonês.
  '--ch' ou '-8': Saudação em chinês tradicional.
  '--ru' ou '-9': Saudação em russo.
  
  Versão:
  '--version' ou '-v': Mostra a versão atual do programa.
Download:
Você pode baixar o programa já compilado (x64) e executá-lo com o comando abaixo:
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/bin/olamundo'
  chmod +x olamundo
  ./olamundo
Você também poderá compilar o programa em seu sistema através do comando abaixo (é necessário possuir o GCC):
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/src/olamundo.c'
  gcc olamundo.c -o olamundo
  ./olamundo

Power - Biblioteca de Exponenciação em C!
Este programa é apenas um teste para o uso de uma simples biblioteca de funções em C utilizando os arquivos de 'headers' disponíveis para o programa que você deseja criar.
Decidi então criar uma simples biblioteca com uma função de exponenciação como exemplo. A biblioteca 'math.h' já cumpre essa função com a função "pow(int base, int expo)", mas decidi criar uma igual por conta própria.
Decidi também enviar um arquivo de fonte como exemplo de uso da biblioteca.
Download:
Você pode baixar o programa já compilado (x64) e executá-lo com o comando abaixo:
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/bin/power'
  chmod +x power
  ./power
Você também poderá compilar o programa em seu sistema através do comando abaixo (é necessário possuir o GCC):
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/src/power.c'
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/lib/power.h'
  gcc power.c -o power -I .
  ./power

Ctemp - Conversor de Temperatura em C
Este é um programa básico para conversão de temperaturas, convertendo os valores para as outras unidades de temperatura, como Celsius, Fahrenheit e Kelvin.
Basta executar o programa via terminal e inserir os argumentos necessários. O programa então irá fazer os cálculos e irá mostrar seus valores em outras unidades de temperatura.
Programa similar a este e com o uso de interface gráfica pode ser encontrado neste repositório (requer Java): Conversor de Temperatura 2016
Aqui está uma lista com os possíveis argumentos:
  Unidade:
  '-c' ou '--celsius':    Converte de Celsius para Fahrenheit e Kelvin
  '-f' ou '--fahrenheit': Converte de Fahrenheit para Celsius e Kelvin
  '-k' ou '--kelvin':     Converte de Kelvin para Celsius e Fahrenheit
  '-h' ou '--help':       Mostra a tela de ajuda
Download:
Você pode baixar o programa já compilado (x64) e executá-lo com o comando abaixo:
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/bin/ctemp'
  chmod +x ctemp
  ./ctemp [unidade] [temperatura]
Você também poderá compilar o programa em seu sistema através do comando abaixo (é necessário possuir o GCC):
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/src/ctemp.c'
  gcc ctemp.c -o ctemp
  ./ctemp [unidade] [temperatura]

Ytdlc - Download de Vídeos e Músicas com youtube-dl
Movido para outro repositório. Visite https://github.com/Wolfterro/Ytdlc

Trump.c - Construa seu próprio muro!
*** Este programa é apenas fruto de uma simples brincadeira aliada ao ócio de um programador, por favor não leve a sério! ***
Este é um simples programa que, ao ser executado, irá criar um "muro" em seu terminal.
Para encerrar o programa, basta apertar CTRL + C e ele irá dizer o tamanho do muro que você construiu.
Aqui está uma lista com os possíveis argumentos:
  Opções:
  -------
  '-h' ou '--help':                   Mostra o menu de ajuda.
  
  Cores:
  ------
  '-rw' ou '--red-wall':              Constrói um muro vermelho.
  '-gw' ou '--green-wall':            Constrói um muro verde.
  '-yw' ou '--yellow-wall':           Constrói um muro amarelo.
  '-bw' ou '--blue-wall':             Constrói um muro azul.
  '-mw' ou '--magenta-wall':          Constrói um muro magenta.
  '-cw' ou '--cyan-wall':             Constrói um muro ciano.
  '-ww' ou '--white-wall':            Constrói um muro branco.
Download:
Assim como o muro, você também precisa "construir" o programa, isto é, compilar. Faz parte da brincadeira:
  wget 'https://raw.github.com/Wolfterro/Projetos-em-C/master/src/Trump.c'
  gcc Trump.c -o Build -Wall
  ./Build
Ou utilizando o git:
  git clone https://github.com/Wolfterro/Projetos-em-C.git
  cd Projetos-em-C/src
  gcc Trump.c -o Build -Wall
  ./Build
