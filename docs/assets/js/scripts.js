const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

document.addEventListener('DOMContentLoaded', () => {
  const html = document.querySelector('html');
  const inputDarkMode = document.getElementById('input-dark-mode');

  inputDarkMode.addEventListener('change', () => {
      if (inputDarkMode.checked) {
          html.setAttribute('dark', 'true');
      } else {
          html.removeAttribute('dark');
      }
  });
});

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.'); 
    return;
  }
  const url = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`; 
  const defaultUrl = 'https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community'
  if(searchValue===''){
    window.open(defaultUrl, '_blank')
  }
  window.open(url, '_blank');
})