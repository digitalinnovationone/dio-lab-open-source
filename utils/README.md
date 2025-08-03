<!DOCTYPE html>
<html lang="pt-BR">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Projeto da DIO para prática de contribuição em open source">
  <title>DIO Lab - Open Source</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-color: #f8f9fa;
    }
    .card {
      margin: 1rem;
      border-radius: 1rem;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      transition: transform 0.2s ease-in-out;
    }
    .card:hover {
      transform: scale(1.02);
    }
    .search-input {
      max-width: 400px;
      margin: 2rem auto;
    }
    .counter {
      font-weight: bold;
      margin-top: 1rem;
      text-align: center;
    }
    .filter-buttons {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }
  </style>
</head>

<body>
  <div class="container py-4">
    <h1 class="text-center mb-4">👥 Comunidade DIO - Open Source</h1>

    <div class="d-flex justify-content-center">
      <input type="text" id="search" class="form-control search-input" placeholder="Buscar por nome ou tecnologia...">
    </div>

    <div class="d-flex justify-content-center mb-3">
      <button id="sortAZ" class="btn btn-outline-primary mx-1">Ordenar A-Z</button>
      <button id="sortZA" class="btn btn-outline-secondary mx-1">Ordenar Z-A</button>
    </div>

    <div class="filter-buttons">
      <button class="btn btn-sm btn-outline-dark tech-filter" data-tech="all">Todos</button>
      <button class="btn btn-sm btn-outline-info tech-filter" data-tech="html">HTML</button>
      <button class="btn btn-sm btn-outline-info tech-filter" data-tech="css">CSS</button>
      <button class="btn btn-sm btn-outline-info tech-filter" data-tech="javascript">JavaScript</button>
      <button class="btn btn-sm btn-outline-info tech-filter" data-tech="python">Python</button>
    </div>

    <div id="profileCount" class="counter">Perfis encontrados: 1</div>

    <div id="profiles" class="row justify-content-center">
      <!-- Perfil principal exibido: juhz1k4 -->
      <div class="col-md-4 profile-card" data-name="juhz1k4" data-tech="javascript python html css">
        <div class="card border-primary">
          <div class="card-body">
            <h5 class="card-title">Juhz1k4</h5>
            <p class="card-text">Entusiasta em tecnologia, desenvolvedor apaixonado por projetos criativos e open source. Explorando o mundo com código e propósito 🚀</p>
            <a href="https://github.com/Juhz1k4" class="btn btn-primary" target="_blank">Ver GitHub</a>
          </div>
        </div>
      </div>
      <!-- Outros perfis podem ser adicionados abaixo -->
    </div>

    <div id="noResults" class="text-center text-muted" style="display: none;">
      Nenhum perfil encontrado 😢
    </div>
  </div>

  <script>
    const searchInput = document.getElementById('search');
    const profileCardsContainer = document.getElementById('profiles');
    const profileCards = document.querySelectorAll('.profile-card');
    const profileCount = document.getElementById('profileCount');
    const noResults = document.getElementById('noResults');
    const sortAZ = document.getElementById('sortAZ');
    const sortZA = document.getElementById('sortZA');
    const techFilters = document.querySelectorAll('.tech-filter');

    function updateCount() {
      const visibleCards = Array.from(profileCards).filter(card => card.style.display !== 'none');
      profileCount.textContent = `Perfis encontrados: ${visibleCards.length}`;
      noResults.style.display = visibleCards.length === 0 ? 'block' : 'none';
    }

    searchInput.addEventListener('input', () => {
      const term = searchInput.value.toLowerCase();

      profileCards.forEach(card => {
        const name = card.dataset.name;
        const tech = card.dataset.tech;
        const visible = name.includes(term) || tech.includes(term);
        card.style.display = visible ? 'block' : 'none';
      });

      updateCount();
    });

    function sortProfiles(order) {
      const cards = Array.from(profileCards);
      cards.sort((a, b) => {
        const nameA = a.dataset.name;
        const nameB = b.dataset.name;
        return order === 'asc' ? nameA.localeCompare(nameB) : nameB.localeCompare(nameA);
      });

      cards.forEach(card => profileCardsContainer.appendChild(card));
    }

    sortAZ.addEventListener('click', () => sortProfiles('asc'));
    sortZA.addEventListener('click', () => sortProfiles('desc'));

    techFilters.forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.dataset.tech;

        profileCards.forEach(card => {
          const techs = card.dataset.tech.split(" ");
          const show = filter === "all" || techs.includes(filter);
          card.style.display = show ? "block" : "none";
        });

        updateCount();
      });
    });

    updateCount();
  </script>
</body>

</html>
