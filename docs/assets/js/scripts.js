// Alteração feita por cassio luciano da silva em 21/08/2023
// Descrição da alteração: Aplicação de filtro na pesquisa de perfil.

const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const fileList = document.getElementById('fileList');

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value.trim();

  const url = 'https://api.github.com/repos/elidianaandrade/dio-lab-open-source/contents/community';

  fileList.innerHTML = '';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const filteredFiles = data.filter(file => {
        const fileName = file.name.toLowerCase();
        return (searchValue.length === 1 && fileName.startsWith(searchValue.toLowerCase())) ||
          (searchValue.length >= 3 && fileName.includes(searchValue.toLowerCase()));
      });
      filteredFiles.forEach(file => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(file.name)}`;
        a.textContent = file.name;
        li.appendChild(a);
        fileList.appendChild(li);
      });
    })
    .catch(error => console.error('Erro:', error));
});