# AutoBot - Automação de Processos em Python

## Descrição
O **AutoBot** é uma ferramenta de automação desenvolvida em Python para facilitar tarefas repetitivas como manipulação de planilhas, envio de e-mails e integração com o WhatsApp. Com o AutoBot, você pode automatizar fluxos de trabalho complexos com simplicidade e eficiência.

## Funcionalidades
- **Manipulação de Planilhas:** Processamento e filtragem automatizada de arquivos Excel (.xlsx) com base em critérios definidos pelo usuário.
- **Envio de E-mails:** Envio automático de e-mails personalizados com anexos, utilizando a integração com servidores IMAP.
- **Integração com WhatsApp:** Envio de mensagens e anexos pelo WhatsApp Web de forma automatizada.

## Tecnologias Utilizadas
- [Python 3.10](https://www.python.org/downloads/release/python-3100/) - Linguagem de programação principal utilizada para desenvolver o AutoBot.
- [Pandas](https://pandas.pydata.org/) - Biblioteca utilizada para manipulação de dados e arquivos Excel.
- [Selenium](https://www.selenium.dev/) - Biblioteca usada para automação do envio de mensagens pelo WhatsApp Web.
- [IMAPClient](https://imapclient.readthedocs.io/en/stable/) - Biblioteca para integração com servidores de e-mail.

## Instalação
Siga os passos abaixo para instalar e configurar o AutoBot em seu ambiente:

```bash
# Clone o repositório
git clone https://github.com/autobotdev/autobot.git

# Entre no diretório do projeto
cd autobot

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
