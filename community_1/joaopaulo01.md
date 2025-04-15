##Conecte-se comigo

[![LinkedIn](https://img.shields.io/badge/LinkedIn-FFF?style=for-the-badge&logo=linkedin)]() 

<h1>
    <a href="(https://www.linkedin.com/in/joao-paulo-da-silva-cavalcante-971414a7/)">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span>João Paulo da Silva Cavalcante</span>
</h1>

Repositório desenvolvido para fins de comentar um pouco sobre um projeto profissional que estou desenvolvendo sobre **Automação Web de permissões de trabalho e criação de análises de risco** na [Petrobrás](https://www.dio.me/).

## Objetivo

Desenvolver uma aplicação web para automatizar a emissão de permissões de trabalho e análise de riscos na Usina UTE-NPI, otimizando a segurança e eficiência operacional.

## Tecnologias

[![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python&logoColor=3776AB)]()  
[![Django](https://img.shields.io/badge/Django-000?style=for-the-badge&logo=django&logoColor=092E20)]()  
[![Flet](https://img.shields.io/badge/Flet-000?style=for-the-badge&logo=flutter&logoColor=02569B)]()  
[![Selenium](https://img.shields.io/badge/Selenium-000?style=for-the-badge&logo=selenium&logoColor=43B02A)]()  
[![Pandas](https://img.shields.io/badge/Pandas-000?style=for-the-badge&logo=pandas&logoColor=150458)]()  
[![HTML5](https://img.shields.io/badge/HTML5-000?style=for-the-badge&logo=html5&logoColor=E94D5F)]()  
[![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=30A3DC)]()  

## Desafio: Automação de Permissões de Trabalho e Análises de Risco

Desenvolver uma solução de automação para o processo de emissão de permissões de trabalho e análise de riscos na Usina UTE-NPI. A proposta é criar uma ferramenta eficiente que otimize a gestão de segurança e conformidade, reduzindo o tempo de processamento e garantindo um controle mais preciso sobre as atividades operacionais.

## Descrição do Projeto

O sistema utilizará Python e frameworks como Django para o backend, garantindo uma aplicação escalável e segura. O Selenium será empregado para automação web no gerenciamento das permissões de trabalho, enquanto Pandas facilitará o tratamento e análise de dados. A interface será desenvolvida com Flet para proporcionar uma experiência amigável e intuitiva para os usuários.

A implementação da automação visa não apenas melhorar a eficiência no controle de riscos na execução das tarefas, mas também permitir uma tomada de decisão mais ágil baseada em dados concretos. A integração com tecnologias web modernas como HTML5 e CSS3 garantirá um ambiente responsivo e acessível para todos os envolvidos no processo.

## Exemplo de Código

Aqui está uma demonstração de como está a automatização do login no sistema utilizando Selenium:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait

#Caminho para o WebDriver do Edge
driver_path = caminho_driver
service = Service(driver_path)
driver = None

# Inicializa o navegador
browser = webdriver.Edge()

# Acessa a página de login
browser.get("https://sistema-ute-npi.com/login")

# Preenche os campos de login
browser.find_element(By.CSS_SELECTOR, 'form#LoginForm fieldset label input[name="j_username"]').send_keys("meu_usuario")
browser.find_element(By.CSS_SELECTOR, 'form#LoginForm fieldset label input[name="j_password"]').send_keys("minha_senha", Keys.RETURN)

# Confirma login
print("Login realizado com sucesso!")
```

Este código demonstra uma automação simples do processo de login no site que utilizo, um dos primeiros passos na automação das permissões de trabalho.

---

---
<div align="center">Feito por <a href="https://github.com/joaopaulo01">JP</a>.</div>

