### Olá, eu sou Akyama de Souza Vieira 👋

🛡️ **Analista de Suporte** com foco em suporte e gestão, desenvolvedor front-end e freelancer em web design.

![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white)

🏢 **Atuação Profissional**
- 🚀 Analista de Suporte e Desenvolvedor Front-End
- 💼 Especialista em políticas de segurança e configuração de servidores
- 💻 Freelancer em web design com experiência em WordPress

### 📌 Projetos em Destaque

#### Página Web em WordPress (https://nibbv.com.br)

#### 🛠️Ferramentas Utilizadas 
- Serviço em Nuvem Gratuito Oracle Free Hosting https://www.oracle.com/cloud/free/
- Ubuntu Server Minimal 
- Servidor Web Nginx
- WordPress
- Elementor
- Serviço CDN/WAF gratuito Cloudflare (https://www.cloudflare.com/pt-br/)
- Certificado SSL gratuito Let's Encrypt (https://letsencrypt.org/pt-br/)
- MariaDB

### 🛡️Políticas de Segurança
**Configuração do WAF CloudFlare**:

1. Block SQL Injection (Bloquear Injeção SQL)

- O que é: SQL Injection é uma técnica de ataque onde o invasor insere ou "injeta" código SQL malicioso em uma consulta, com o objetivo de manipular o banco de dados. Como funciona o bloqueio: O WAF detecta e bloqueia padrões de entrada que se parecem com comandos SQL maliciosos, impedindo que o ataque chegue ao banco de dados.

2. Block RFI Attempts (Bloquear Tentativas de Inclusão Remota de Arquivo)

- O que é: Remote File Inclusion (RFI) é um ataque onde o invasor tenta incluir um arquivo remoto malicioso no servidor web. Como funciona o bloqueio: O WAF verifica e bloqueia tentativas de incluir arquivos externos que não sejam permitidos ou que tenham intenções maliciosas.

3. Block Directory Traversal Attempts (Bloquear Tentativas de Travessia de Diretórios)

- O que é: Directory Traversal é um ataque onde o invasor tenta acessar arquivos e diretórios restritos fora do diretório raiz da web. Como funciona o bloqueio: O WAF impede tentativas de acessar caminhos de diretórios não autorizados, como usando “../” para navegar para cima na estrutura de diretórios.

4. Block Evasion Attempts (Bloquear Tentativas de Evasão)

- O que é: Evasion Attempts são técnicas usadas por invasores para evitar a detecção de suas atividades maliciosas, tentando enganar o sistema de segurança.
Como funciona o bloqueio: O WAF detecta e bloqueia padrões de comportamento que tentam contornar as regras de segurança, mantendo a proteção ativa.

5. Block XSS Attempts (Bloquear Tentativas de XSS)

- O que é: Cross-Site Scripting (XSS) é um ataque onde o invasor injeta scripts maliciosos em páginas web visualizadas por outros usuários. Como funciona o bloqueio: O WAF identifica e bloqueia tentativas de injeção de scripts em páginas web, protegendo os usuários de códigos maliciosos que podem ser executados em seus navegadores.

**Security Headers**

Para garantir a segurança e integridade do meu projeto WordPress, implementei várias configurações de headers de segurança que ajudam a proteger contra uma ampla gama de ameaças cibernéticas. As principais configurações incluem:

1. Content Security Policy (CSP):

- O que é: A CSP é uma medida de segurança que ajuda a prevenir uma série de ataques, incluindo Cross-Site Scripting (XSS) e injeção de dados, limitando as fontes de conteúdo que o navegador pode carregar.
Implementação: Configurei o cabeçalho Content-Security-Policy para permitir apenas scripts e estilos necessários para o funcionamento do WordPress, bloqueando todas as fontes não confiáveis. Isso impede que scripts maliciosos sejam executados no site.

2. Strict-Transport-Security (HSTS):

- O que é: HSTS é um mecanismo que força os navegadores a sempre usar conexões HTTPS seguras, evitando ataques de downgrade e sequestro de cookies.
Implementação: Adicionei o cabeçalho Strict-Transport-Security para garantir que todas as comunicações entre o navegador e o servidor sejam criptografadas, fortalecendo a segurança das sessões dos usuários.

3. X-Content-Type-Options:

- O que é: Este cabeçalho impede que os navegadores tentem adivinhar o tipo de conteúdo, uma prática que pode ser explorada para injeção de scripts.
Implementação: Configurei o cabeçalho X-Content-Type-Options para nosniff, garantindo que os navegadores respeitem os tipos de conteúdo declarados e não executem conteúdo não autorizado.

4. X-Frame-Options:

- O que é: Este cabeçalho protege contra ataques de clickjacking ao controlar se o conteúdo do site pode ser embutido em frames de outros sites.
Implementação: Adicionei o cabeçalho X-Frame-Options com o valor DENY, impedindo que o site seja carregado em iframes de outros domínios, o que protege contra tentativas de clickjacking.

5. X-XSS-Protection:

- O que é: Este cabeçalho ativa o filtro XSS do navegador, que detecta e bloqueia ataques de Cross-Site Scripting.
Implementação: Configurei o cabeçalho X-XSS-Protection para 1; mode=block, ativando a proteção contra XSS nos navegadores compatíveis e impedindo a execução de scripts maliciosos.
Essas configurações de headers de segurança são fundamentais para fortalecer a defesa do meu projeto WordPress contra diversas ameaças e garantir uma experiência segura para todos os usuários.

---

## Sobre Mim

- **Nome**: Akyama de Souza Vieira
- **Profissão**: Analista de Suporte e Desenvolvedor Front-End
- **Interesses**: Desenvolvimento Web, Segurança da Informação, Jiu-Jitsu

## Contato

- **Email**: [akyama.souza@gmail.com](mailto:akyama.souza@gmail.com)
- **LinkedIn**: [https://www.linkedin.com/in/akyama-de-souza/](https://www.linkedin.com/in/akyama-de-souza/)
- **GitHub**: [https://github.com/akyamasouza](https://github.com/akyamasouza)

---

Obrigado por visitar! bye!👋😁
