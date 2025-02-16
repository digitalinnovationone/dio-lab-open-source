const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value.trim();
  const defaultUrl = 'https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community';

  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.');
    window.open(defaultUrl, '_blank');
    return;
  }

  const url = `${defaultUrl}/${encodeURIComponent(searchValue)}.md`;
  window.open(url, '_blank');
});