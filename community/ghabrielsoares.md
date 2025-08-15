## Olá. Eu sou o Gabriel Soares. Ciêntista da Computação | Desenvolvedor | Automação | Monitoramento | Virtualização | Contêineres | Bancos de Dados | Análise de Dados | Dashboards | Linux | Cloud | Redes
## Hello. I'm Gabriel Soares. Computer Scientist | Developer | Automation | Monitoring | Virtualization | Containers | Databases | Data Analysis | Dashboards | Linux | Cloud | Networking

<br>

-  Formação: Bacharelado em Ciência da Computação / Education: Bachelor's in Computer Science

-  Tenho experiência no desenvolvimento web, automação de tarefas, monitoramento de sistemas, gerenciamento de servidores, virtualização, contêineres, bancos de dados e hospedagem. Trabalho com análise de dados, criação de dashboards e otimização de desempenho em ambientes Linux e cloud.  / I have experience in web development, task automation, system monitoring, server management, virtualization, containers, databases, and hosting. I work with data analysis, dashboard creation, and performance optimization in Linux and cloud environments.
- Pronomes - Ele, Dele  / Pronouns - He, Him
 


##

<div align="left">
  <a href="https://github.com/ghabrielsoares">
  <img height="131em" src="https://github-readme-stats.vercel.app/api?username=ghabrielsoares&show_icons=true&theme=midnight-purple&include_all_commits=true&count_private=true"/>
  <img height="131em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ghabrielsoares&layout=compact&langs_count=7&theme=midnight-purple"/>
</div>

##   
  <div> 
    <a href="https://www.instagram.com/gabrielcs_dev/" target="_blank">https://www.instagram.com/gabrielcs_dev/</a><BR>
    <a href="https://wa.me/5591985668116" target="_blank">https://wa.me/5591985668116</a><BR>
    <a href="https://www.linkedin.com/in/ghabrielsoares/" target="_blank">https://www.linkedin.com/in/ghabrielsoares/</a><BR>
    <a href = "mailto:ghabrielcsoares@gmail.com">mailto:ghabrielcsoares@gmail.com</a><BR>
    <a href = "mailto:ghabrielcsoares@hotmail.com">mailto:ghabrielcsoares@hotmail.com</a><BR>
   
</div>


---

# 🚀 Projeto SpaceShip

**SpaceShip** é uma recriação moderna do clássico jogo **Asteroids**, desenvolvida com foco didático e arquitetura organizada. O projeto adota o padrão **MVC (Model-View-Controller)** e princípios da **Arquitetura Hexagonal**, promovendo separação de responsabilidades, reutilização de código e fácil manutenção.

## 🎯 Objetivo

Reproduzir o jogo Asteroids de forma modular e progressiva, com foco em boas práticas de desenvolvimento front-end e organização de código. Ideal para fins educativos, experimentação com arquitetura de software e estudo de padrões de projeto.

## 🧱 Estrutura do Projeto

```
spaceship/
├── index.html           # HTML5 simples que carrega a View e inicializa o Controller
├── style.css            # Estilos básicos para visual e animações
├── /controller          # Controladores que gerenciam entrada do usuário e lógica de jogo
├── /view                # Renderização visual do jogo (canvas, nave, asteroides etc.)
├── /model               # Entidades do jogo (nave, asteroides, disparos, colisões)
├── /animation           # Lógica de animação e frames
├── /service.js          # Serviços utilitários, regras e lógica de negócios
```

## ⚙️ Tecnologias Usadas

* HTML5 + Canvas API
* CSS3
* JavaScript (ES6+)
* Arquitetura MVC + Hexagonal

## 📚 Aprendizados

* Separação de responsabilidades com MVC
* Modularização de código com diretórios específicos
* Uso do Canvas para renderização 2D
* Lógica de jogo com detecção de colisões, física básica e animações


# CODE

### paceship/index.html

```
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SpaceShip</title>

  <!-- CSS Principal -->
  <link rel="stylesheet" href="view/css/style.css" />
</head>
<body>
  <!-- Container principal do jogo -->
  <main id="container"></main>

  <!-- Carregador central da aplicação -->
  <script type="module" src="service.js"></script>
</body>
</html>
```

---

### paceship/service.js

```
// service.js
(async function loadApp() {
  try {
    // Carrega o conteúdo do corpo principal (nave, cenário, HUD)
    await import('./view/Content/ship.js');

    // Carrega os arquivos de movimentação da nave e dos asteroides
    await import('./view/action/moveShip.js');
    await import('./view/action/moveAsteroids.js');

    await import('./view/action/shoot.js');

    // Carrega os arquivos de animação de colisão
    await import('./view/animation/collision.js');

    // Carrega os controladores e lógica de jogo
    await import('./controller/gameController.js');

    console.log('[SpaceShip] Aplicação carregada com sucesso.');
  } catch (error) {
    console.error('[SpaceShip] Erro ao carregar a aplicação:', error);
  }
})();
```
---
### spaceship/view/css/style.css

```
/* style.css */

/* Reset básico */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Tela principal */
body {
  background-color: #000;
  color: #fff;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  overflow: hidden;
}

/* Container do jogo */
#container {
  width: 100vw;
  height: 100vh;
  position: relative;
}

/* Nave */
.ship {
  width: 40px;
  height: 40px;
  background-color: #0ff;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%) rotate(0deg);
  clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
}

/* Asteroides */
.asteroid {
  position: absolute;
  background-color: gray;
  border-radius: 50%;
  opacity: 0.8;
}

/* HUD */
.hud {
  position: absolute;
  top: 10px;
  left: 10px;
  color: #fff;
  font-size: 18px;
  background-color: rgba(0, 0, 0, 0.6);
  padding: 8px 12px;
  border-radius: 8px;
  user-select: none;
}

/* Tiros */
.bullet {
  width: 8px;
  height: 8px;
  background-color: yellow;
  border-radius: 50%;
  position: absolute;
  z-index: 10;
}

/* HUD */
.hud {
  position: absolute;
  top: 10px;
  right: 10px;
  color: #fff;
  font-size: 16px;
  background-color: rgba(0, 0, 0, 0.6);
  padding: 8px 12px;
  border-radius: 8px;
  user-select: none;
  text-align: right;
  line-height: 1.4em;
}

/* Tela inicial/final */
.overlay {
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.85);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.overlay .screen {
  text-align: center;
}

.overlay button {
  margin-top: 20px;
  padding: 10px 24px;
  font-size: 18px;
  border: none;
  background-color: #0ff;
  color: #000;
  cursor: pointer;
  border-radius: 8px;
}

/* Explosão */
.explosion {
  position: absolute;
  width: 40px;
  height: 40px;
  margin-left: -20px;
  margin-top: -20px;
  background: radial-gradient(circle, orange 0%, red 60%, transparent 100%);
  border-radius: 50%;
  animation: explode 0.5s ease-out;
  pointer-events: none;
  z-index: 20;
}

@keyframes explode {
  0% {
    transform: scale(0.5);
    opacity: 1;
  }
  100% {
    transform: scale(2);
    opacity: 0;
  }
}
```
---
### spaceship/view/action/moveAsteroids.js

```
// moveAsteroids.js

import { getShipMovementState } from './moveShip.js';

const container = document.getElementById('container');
const asteroids = [];

// Função que cria um único asteroide
function createAsteroid() {
  const asteroid = document.createElement('div');
  asteroid.classList.add('asteroid');

  const size = Math.random() * 30 + 30;
  asteroid.style.width = `${size}px`;
  asteroid.style.height = `${size}px`;

  const x = Math.random() * window.innerWidth;
  const y = Math.random() * window.innerHeight;

  const dx = (Math.random() - 0.5) * 1.5;
  const dy = (Math.random() - 0.5) * 1.5;

  asteroid.dataset.dx = dx;
  asteroid.dataset.dy = dy;

  container.appendChild(asteroid);
  asteroids.push({ element: asteroid, x, y, dx, dy });
}

// Atualiza a posição de todos os asteroides
function moveAsteroids() {
  const { angle, moving } = getShipMovementState();

  for (let asteroid of asteroids) {
    let moveX = parseFloat(asteroid.dx);
    let moveY = parseFloat(asteroid.dy);

    // Simula que a nave está empurrando o cenário
    if (moving) {
      const rad = (angle - 90) * (Math.PI / 180);
      moveX -= Math.cos(rad) * 2;
      moveY -= Math.sin(rad) * 2;
    }

    asteroid.x += moveX;
    asteroid.y += moveY;

    if (asteroid.x < 0) asteroid.x = window.innerWidth;
    if (asteroid.x > window.innerWidth) asteroid.x = 0;
    if (asteroid.y < 0) asteroid.y = window.innerHeight;
    if (asteroid.y > window.innerHeight) asteroid.y = 0;

    asteroid.element.style.left = `${asteroid.x}px`;
    asteroid.element.style.top = `${asteroid.y}px`;
  }
}

// Listener para receber pedido de criação de asteroide (evento disparado pelo gameController.js)
document.addEventListener('createAsteroid', () => {
  createAsteroid();
});

// Cria os asteroides iniciais (por compatibilidade)
for (let i = 0; i < 5; i++) {
  createAsteroid();
}

setInterval(moveAsteroids, 30);
```

---
### spaceship/view/action/moveShip.js

```
// moveShip.js

let angle = 0;
let moving = false;

const ship = document.querySelector('.ship');

function rotateShip(direction) {
  angle += direction === 'left' ? -5 : 5;
  ship.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`;
}

document.addEventListener('keydown', (e) => {
  switch (e.key) {
    case 'ArrowLeft':
      rotateShip('left');
      break;
    case 'ArrowRight':
      rotateShip('right');
      break;
    case 'ArrowUp':
      moving = true;
      break;
  }
});

document.addEventListener('keyup', (e) => {
  if (e.key === 'ArrowUp') {
    moving = false;
  }
});

// Exporta se a nave está se movendo e seu ângulo
export function getShipMovementState() {
  return { angle, moving };
}
```

---
### spaceship/view/action/shoot.js

```
// shoot.js

import { getShipMovementState } from './moveShip.js';
import { registerScore } from '../../controller/gameController.js';
import { createExplosion } from '../animation/explosion.js';

const container = document.getElementById('container');
const bullets = [];

function createBullet() {
  const { angle } = getShipMovementState();

  const bullet = document.createElement('div');
  bullet.classList.add('bullet');

  bullet.style.left = `calc(50% - 4px)`;
  bullet.style.top = `calc(50% - 4px)`;

  const rad = (angle - 90) * (Math.PI / 180);
  const dx = Math.cos(rad) * 5;
  const dy = Math.sin(rad) * 5;

  container.appendChild(bullet);
  bullets.push({ element: bullet, x: window.innerWidth / 2, y: window.innerHeight / 2, dx, dy });
}

function moveBullets() {
  const asteroids = document.querySelectorAll('.asteroid');

  for (let i = bullets.length - 1; i >= 0; i--) {
    const bullet = bullets[i];
    bullet.x += bullet.dx;
    bullet.y += bullet.dy;

    bullet.element.style.left = `${bullet.x}px`;
    bullet.element.style.top = `${bullet.y}px`;

    // Remove se sair da tela
    if (
      bullet.x < 0 || bullet.x > window.innerWidth ||
      bullet.y < 0 || bullet.y > window.innerHeight
    ) {
      bullet.element.remove();
      bullets.splice(i, 1);
      continue;
    }

    // Verifica colisão com asteroides
    for (let j = 0; j < asteroids.length; j++) {
      const a = asteroids[j];
      const aRect = a.getBoundingClientRect();
      const bRect = bullet.element.getBoundingClientRect();

      const dx = (bRect.left + 4) - (aRect.left + aRect.width / 2);
      const dy = (bRect.top + 4) - (aRect.top + aRect.height / 2);
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance < aRect.width / 2) {
        // Colisão detectada
        createExplosion(aRect.left + aRect.width / 2, aRect.top + aRect.height / 2);
        bullet.element.remove();
        a.remove();
        bullets.splice(i, 1);
        registerScore(50); // +50 pontos por acerto
        return;
      }
    }
  }
}

document.addEventListener('keydown', (e) => {
  if (e.code === 'Space') {
    createBullet();
  }
});

setInterval(moveBullets, 20);
```

---
### spaceship/view/animation/collision.js

```
// collision.js

function detectCollision(ship, asteroid) {
  const shipRect = ship.getBoundingClientRect();
  const asteroidRect = asteroid.getBoundingClientRect();

  const dx = (shipRect.left + shipRect.width / 2) - (asteroidRect.left + asteroidRect.width / 2);
  const dy = (shipRect.top + shipRect.height / 2) - (asteroidRect.top + asteroidRect.height / 2);
  const distance = Math.sqrt(dx * dx + dy * dy);

  const shipRadius = shipRect.width / 2;
  const asteroidRadius = asteroidRect.width / 2;

  return distance < shipRadius + asteroidRadius;
}

function checkCollisions() {
  const ship = document.querySelector('.ship');
  const asteroids = document.querySelectorAll('.asteroid');

  for (let asteroid of asteroids) {
    if (detectCollision(ship, asteroid)) {
      ship.style.backgroundColor = 'red';
      console.warn('[SpaceShip] Colisão detectada!');
      return;
    }
  }

  // Sem colisão, mantém a cor normal
  ship.style.backgroundColor = '#0ff';
}

setInterval(checkCollisions, 50);
```
---

### spaceship/view/animation/explosion.js

```
// explosion.js

export function createExplosion(x, y) {
  const explosion = document.createElement('div');
  explosion.classList.add('explosion');
  explosion.style.left = `${x}px`;
  explosion.style.top = `${y}px`;

  document.getElementById('container').appendChild(explosion);

  // Remove a explosão após a animação
  setTimeout(() => {
    explosion.remove();
  }, 500); // duração da explosão
}
```

---

### spaceship/view/Content/ship.js

```
// ship.js

export function createShip() {
  const container = document.getElementById('container');

  const ship = document.createElement('div');
  ship.classList.add('ship');

  // Define posição inicial da nave
  ship.style.left = '50%';
  ship.style.top = '50%';

  container.appendChild(ship);
}

// Executa ao importar
createShip();
```

---

### spaceship/controller/gameController.js

```
// gameController.js

let score = 0;
let lives = 5;
let level = 1;
let isGameRunning = false;
let lastBonusTime = Date.now();

const container = document.getElementById('container');

// HUD
const hud = document.createElement('div');
hud.classList.add('hud');
hud.innerHTML = `
  <div><strong>Pontos:</strong> <span id="score">0</span></div>
  <div><strong>Vidas:</strong> <span id="lives">5</span></div>
  <div><strong>Nível:</strong> <span id="level">1</span></div>
`;
container.appendChild(hud);

// Tela de início/fim
const overlay = document.createElement('div');
overlay.classList.add('overlay');
overlay.innerHTML = `
  <div class="screen">
    <h1>🚀 SpaceShip</h1>
    <button id="startBtn">Iniciar Jogo</button>
  </div>
`;
container.appendChild(overlay);

document.getElementById('startBtn').onclick = startGame;

function updateHUD() {
  document.getElementById('score').textContent = score;
  document.getElementById('lives').textContent = lives;
  document.getElementById('level').textContent = level;
}

function startGame() {
  score = 0;
  lives = 5;
  level = 1;
  isGameRunning = true;
  lastBonusTime = Date.now();
  updateHUD();
  overlay.style.display = 'none';

  resetShip();
  clearAsteroids();
  createAsteroids(5);
}

function resetShip() {
  const ship = document.querySelector('.ship');
  ship.style.backgroundColor = '#0ff';
  ship.style.left = '50%';
  ship.style.top = '50%';
  ship.style.transform = `translate(-50%, -50%) rotate(0deg)`;
}

function clearAsteroids() {
  document.querySelectorAll('.asteroid').forEach(a => a.remove());
}

function createAsteroids(count) {
  for (let i = 0; i < count; i++) {
    const event = new CustomEvent('createAsteroid');
    document.dispatchEvent(event);
  }
}

function handleCollision() {
  if (!isGameRunning) return;

  lives--;
  score = Math.max(0, score - 40);
  updateHUD();

  if (lives <= 0) {
    isGameRunning = false;
    overlay.querySelector('.screen').innerHTML = `
      <h1>☠️ Game Over</h1>
      <p>Sua pontuação final: <strong>${score}</strong></p>
      <button id="startBtn">Jogar Novamente</button>
    `;
    overlay.style.display = 'flex';
    score = 0;
    document.getElementById('startBtn').onclick = startGame;
  } else {
    resetShip();
  }
}

function increaseDifficulty() {
  level++;
  createAsteroids(1);

  document.querySelectorAll('.asteroid').forEach(a => {
    a.dataset.dx *= 1.1;
    a.dataset.dy *= 1.1;
  });
  updateHUD();
}

function gameLoop() {
  if (!isGameRunning) return;

  const now = Date.now();

  // +10 pontos a cada 30s
  if (now - lastBonusTime >= 30000) {
    score += 10;
    lastBonusTime = now;
    updateHUD();
    increaseDifficulty();
  }

  // Verifica se houve colisão (cor vermelha)
  const ship = document.querySelector('.ship');
  if (ship && ship.style.backgroundColor === 'red') {
    handleCollision();
  }
}

setInterval(gameLoop, 500);

// Usado por outros módulos para adicionar pontos (ex: tiros)
export function registerScore(amount) {
  if (!isGameRunning) return;
  score += amount;
  updateHUD();
}

```
