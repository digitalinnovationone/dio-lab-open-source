const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

// Melhoria: Variável movida para fora para não ser recriada a cada clique
const baseUrl = 'https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community';

// Melhoria: Criação de uma função separada para lidar com a busca
function handleSearch(e) {
  
  if (e) e.preventDefault(); 

  // Melhoria: .trim() evita que o usuário passe na validação digitando apenas espaços
  const searchValue = searchInput.value.trim();

  if (searchValue === '') {
    
    window.open(baseUrl, '_blank');
    
    return;
  }

  const url = `${baseUrl}/${encodeURIComponent(searchValue)}.md`; 
  window.open(url, '_blank');
}
searchButton.addEventListener('click', handleSearch);

searchInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    handleSearch(e);
  }
});
