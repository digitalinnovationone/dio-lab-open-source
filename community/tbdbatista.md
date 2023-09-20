



<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Desenvolvedor Mobile</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <header>
      <h1>Desenvolvedor Mobile</h1>
    </header>
    <section>
      <h2>Sobre Mim</h2>
      <p>Olá, me chamo <b>Thiago Batista</b> e sou um desenvolvedor mobile com habilidades em <b>Swift, Java e Kotlin</b>. Possuo experiência em desenvolvimento de aplicativos para o setor financeiro.</p>
    </section>
    <section class="skills-container">
      <h2>Habilidades</h2>
      <div class="skill">
        <span class="skill-title">Swift</span>
        <span class="skill-progress" style="width: 90%">90</span>
      </div>
      <div class="skill">
        <span class="skill-title">Java</span>
        <span class="skill-progress" style="width: 60%">60</span>
      </div>
      <div class="skill">
        <span class="skill-title">Kotlin</span>
        <span class="skill-progress" style="width: 40%">40</span>
      </div>
    </section>
    <section>
      <h2>Projetos</h2>
      <ul>
        <li><a href="https://github.com/tbdbatista/todo-ios-app">Aplicativo iOS para Gerenciamento de Tarefas</a></li>
        <li><a href="https://github.com/tbdbatista/weather-ios-app">Aplicativo iOS para Consultar o Tempo</a></li>
        <li><a href="https://github.com/tbdbatista/chat-with-me">Aplicativo iOS de Chat</a></li>
      </ul>
    </section>
    <footer>
      <p>&copy; 2023 Dev Mobile: Thiago Batista</p>
    </footer>
    <script src="script.js"></script>
  </body>
</html>




<style>
/* Global styles */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
  
  background: white;
}

a {
  color: #0077cc;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* Header styles */
header {
  background-color: #222;
  color: #fff;
  padding: 1rem;
  text-align: center;
}

h1 {
  margin: 0;
  font-size: 3rem;
}

/* Section styles */
section {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

h2 {
  font-size: 2rem;
  margin-top: 0;
}

p {
  margin-top: 1rem;
  font-size: 1.125rem;
}

/* Skills container styles */
.skills-container {
  display: flex;
  flex-direction: column;
}

.skill {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}

.skill-title {
  flex: 1;
  margin-right: 1rem;
  font-family: sans-serif;
  font-size: 16px;
  font-weight: 700;
}

.skill-progress {
  background-color: #353a80;
  padding: 0.25rem;
  border-radius: 4px;
  color: #fff;
  font-size: 0.875rem;
}

.skill-progress::after {
  content: attr(data-progress) "%";
}

/* Projects list styles */
ul {
  list-style: none;
  padding-left: 0;
}

li {
  margin-top: 0.5rem;
}

/* Footer styles */
footer {
  background-color: #222;
  color: #fff;
  padding: 1rem;
  text-align: center;
}
</style>


<script>
// Função para animar a barra de progresso
function animateSkills() {
    var skills = document.querySelectorAll('.skill-progress');
    skills.forEach(function(skill) {
      var width = 0;
      var targetWidth = parseInt(skill.style.width);
      var intervalId = setInterval(frame, 10);
      function frame() {
        if (width >= targetWidth) {
          clearInterval(intervalId);
        } else {
          width++;
          skill.style.width = width + '%';
        }
      }
    });
  }
  
  animateSkills();
  
</script>
