const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.'); // Exibir um alerta se o campo estiver vazio
    return;
  }
  const url = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`; 
  const defaultUrl = 'https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community'
  if(searchValue===''){
    window.open(defaultUrl, '_blank')
  }
  window.open(url, '_blank');
})

// Feat Dark Mode \\
const toggleButton = document.getElementById('switch');
const htmlElement = document.documentElement; 

toggleButton.addEventListener('click', () => {
  htmlElement.classList.toggle('dark');
});