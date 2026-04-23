<!-- index.html -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meu Portfólio</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Seu Nome</h1>
    <nav>
      <ul>
        <li><a href="#sobre">Sobre</a></li>
        <li><a href="#projetos">Projetos</a></li>
        <li><a href="#contato">Contato</a></li>
      </ul>
    </nav>
  </header>

  <section id="sobre">
    <h2>Sobre Mim</h2>
    <p>Sou um desenvolvedor apaixonado por tecnologia e design. Amo criar soluções que combinam estética e funcionalidade.</p>
  </section>

  <section id="projetos">
    <h2>Meus Projetos</h2>
    <div class="projetos-grid">
      <div class="projeto">
        <h3>Projeto 1</h3>
        <p>Descrição curta do projeto.</p>
        <a href="#">Ver mais</a>
      </div>
      <div class="projeto">
        <h3>Projeto 2</h3>
        <p>Descrição curta do projeto.</p>
        <a href="#">Ver mais</a>
      </div>
      <!-- Adicione mais projetos conforme necessário -->
    </div>
  </section>

  <section id="contato">
    <h2>Contato</h2>
    <p>Email: seuemail@exemplo.com</p>
    <p>LinkedIn: <a href="#">linkedin.com/in/seunome</a></p>
  </section>

  <footer>
    <p>📍 Informações extras </p>
    <p>Localização: 📍 São Paulo, Brasil</p>    
    <p>Disponibilidade: 🚀 Aberto para freelas ou vagas</p>
    <p>Idiomas que fala: 🌐 Português | Inglês</p>
    <div class="social">
      <a href="#"><img src="linkedin-icon.png" alt="LinkedIn"></a>
      <a href="#"><img src="github-icon.png" alt="GitHub"></a>
      <a href="#"><img src="twitter-icon.png" alt="Twitter"></a>
    </div>
    <form action="#" method="post">
      <label for="email">Receba atualizações:</label>
      <input type="email" id="email" name="email" placeholder="Seu email">
      <button type="submit">Enviar</button>
    </form>
    

    <p>&copy; 2025 Seu Nome. Todos os direitos reservados.</p>
  </footer>
</body>
</html>
