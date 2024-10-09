<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Marcelo Mekaro | Perfil</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      color: #333;
      margin: 0;
      padding: 0;
    }

    h1, h3 {
      color: #0a74da;
    }

    .container {
      max-width: 800px;
      margin: 50px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .skills-title {
      margin-top: 40px;
      font-size: 24px; /* Aumentar tamanho do título */
      text-align: center; /* Centralizar título */
    }

    .loading {
      display: inline-block; /* Mudar para inline-block para ficar ao lado do título */
      width: 150px; /* Aumentar o tamanho do loading */
      animation: loadingAnimation 1s infinite; /* Animação de movimento */
      margin-left: 10px; /* Espaço entre o título e o loading */
    }

    /* Animação do loading */
    @keyframes loadingAnimation {
      0% { transform: scale(1); }
      50% { transform: scale(1.2); }
      100% { transform: scale(1); }
    }

    .skills {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 20px;
      justify-content: center; /* Centralizar habilidades */
    }

    .skills img {
      height: 60px; /* Aumentar altura dos logos das habilidades */
    }

    .logos img {
      height: 80px; /* Aumentar altura dos ícones Tasy e Soul MV */
    }

    .logos {
      display: flex;
      gap: 30px;
      margin: 20px 0;
      justify-content: center;
    }

    .fade-in {
      opacity: 0;
      transition: opacity 1s ease-in-out;
    }

    .fade-in.visible {
      opacity: 1;
    }

    /* Botão dinâmico */
    .dynamic-button {
      background-color: #0a74da;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s;
      font-size: 16px;
    }

    .dynamic-button:hover {
      background-color: #0558a5;
    }
  </style>
</head>

<body>
  <div class="container">
    <h1>Olá, sou Marcelo Mekaro!</h1>
    <h3>Enfermeiro Intensivista | Focado em Tecnologia para a Saúde</h3>

    <p>Experiência com sistemas de prontuário eletrônico, como o <strong>Tasy (Philips)</strong> e o <strong>Soul MV</strong>, focado em inovação na área da saúde.</p>

    <!-- Logos de Tasy e Soul MV -->
    <div class="logos">
      <img src="https://bit.ly/3Yg7vXT" alt="Tasy Logo">
      <img src="https://bit.ly/3BDhzl2" alt="Soul MV Logo">
    </div>

    <h4 class="skills-title">
      Habilidades Técnicas em Desenvolvimento
      <!-- Gif de loading ao lado do título -->
      <img class="loading" src="https://i.pinimg.com/736x/20/c9/b7/20c9b70a173c712abc4d5b0a4149f533.jpg" alt="Loading...">
    </h4>

    <div class="skills">
      <img src="https://img.shields.io/static/v1?message=HTML&logo=html5&label=&color=E34F26&logoColor=white&labelColor=&style=for-the-badge" alt="HTML Logo">
      <img src="https://img.shields.io/static/v1?message=CSS&logo=css3&label=&color=1572B6&logoColor=white&labelColor=&style=for-the-badge" alt="CSS Logo">
      <img src="https://img.shields.io/static/v1?message=JavaScript&logo=javascript&label=&color=F7DF1E&logoColor=black&labelColor=&style=for-the-badge" alt="JavaScript Logo">
      <img src="https://img.shields.io/static/v1?message=Python&logo=python&label=&color=3776AB&logoColor=white&labelColor=&style=for-the-badge" alt="Python Logo">
      <img src="https://img.shields.io/static/v1?message=Canva&logo=canva&label=&color=00C4CC&logoColor=white&labelColor=&style=for-the-badge" alt="Canva Logo">
    </div>

    <p style="margin-top: 20px;">Sempre em busca de novas tecnologias para melhorar o cuidado com a saúde.</p>

    <!-- Botão dinâmico com redirecionamento -->
    <button class="dynamic-button" id="contactBtn">Entre em contato</button>
  </div>

  <script>
    // Animação de fade-in
    document.addEventListener('DOMContentLoaded', () => {
      const elements = document.querySelectorAll('.fade-in');
      elements.forEach((el, index) => {
        setTimeout(() => {
          el.classList.add('visible');
        }, index * 500); // Delay progressivo
      });
    });

    // Redirecionamento ao clicar no botão
    document.getElementById('contactBtn').addEventListener('click', () => {
      window.location.href = 'https://bit.ly/4eB1db5'; // Redireciona para o link
    });
  </script>
</body>
</html>
