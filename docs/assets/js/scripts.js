const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  const url = `https://github.com/elidianaandrade/dio-profile-readme/tree/main/examples/${encodeURIComponent(searchValue)}.md`; 
  window.open(url, '_blank');
})