const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

document.addEventListener("DOMContentLoaded", function () {
  const apiUrl =
    "https://api.github.com/repos/digitalinnovationone/dio-lab-open-source/contents/community";
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      const fileNames = data.map((file) => file.name.replace(/\.md$/, ""));

      const randomIndex = Math.floor(Math.random() * fileNames.length);
      const randomFileName = fileNames[randomIndex];

      searchInput.value = randomFileName;
    })
    .catch((error) => {
      console.error("Error fetching file list:", error);
    });
});

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