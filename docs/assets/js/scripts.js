searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value.trim(); // Remover espaços extras

  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.');
    return;
  }

  const url = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`;
  window.open(url, '_blank');
});