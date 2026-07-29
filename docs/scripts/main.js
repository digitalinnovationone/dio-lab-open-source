// docs/scripts/main.js

document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById('search');
    const profileCardsContainer = document.getElementById('profiles');
    const profileCount = document.getElementById('profileCount');
    const noResults = document.getElementById('noResults');
    const sortAZ = document.getElementById('sortAZ');
    const sortZA = document.getElementById('sortZA');
    const techFilters = document.querySelectorAll('.tech-filter');
    const themeToggle = document.getElementById('themeToggle');
    const htmlElement = document.documentElement;
    let profileCards = [];
  
    function updateCount() {
      const visibleCards = profileCards.filter(card => card.style.display !== 'none');
      profileCount.textContent = `Perfis encontrados: ${visibleCards.length}`;
      noResults.style.display = visibleCards.length === 0 ? 'block' : 'none';
    }
  
    function createCard(profile) {
      const col = document.createElement('div');
      col.className = 'col-md-4 profile-card';
      col.dataset.name = profile.nome.toLowerCase();
      col.dataset.tech = profile.tech.join(' ');
  
      const card = document.createElement('div');
      card.className = 'card border-primary';
  
      const body = document.createElement('div');
      body.className = 'card-body';
  
      const title = document.createElement('h5');
      title.className = 'card-title';
      title.textContent = profile.nome;
  
      const text = document.createElement('p');
      text.className = 'card-text';
      text.textContent = profile.descricao;
  
      const link = document.createElement('a');
      link.className = 'btn btn-primary';
      link.href = profile.github;
      link.target = '_blank';
      link.textContent = 'Ver GitHub';
  
      body.appendChild(title);
      body.appendChild(text);
      body.appendChild(link);
      card.appendChild(body);
      col.appendChild(card);
  
      return col;
    }
  
    function carregarPerfis() {
      fetch('../utils/perfis.json')
        .then(res => res.json())
        .then(data => {
          profileCardsContainer.innerHTML = '';
          data.forEach(profile => {
            const card = createCard(profile);
            profileCardsContainer.appendChild(card);
          });
          profileCards = Array.from(document.querySelectorAll('.profile-card'));
          updateCount();
        });
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
  
    themeToggle.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      htmlElement.setAttribute('data-theme', newTheme);
      themeToggle.textContent = newTheme === 'dark' ? '☀️ Modo Claro' : '🌙 Modo Escuro';
    });
  
    carregarPerfis();
  });