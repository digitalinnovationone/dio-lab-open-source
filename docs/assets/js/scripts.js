const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', (e) => {
  e.preventDefault();

  const searchValue = searchInput.value.trim();
  if (searchValue === '') {
    alert('Por favor, insira um nome de usuário.');
    return;
  }

  const url = `https://github.com/elidianaandrade/dio-lab-open-source/blob/main/community/${encodeURIComponent(searchValue)}.md`;

  window.open(url, '_blank');
});
