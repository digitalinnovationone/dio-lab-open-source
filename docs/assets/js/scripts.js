const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const defaultUrl = 'https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community'

searchButton.addEventListener('click', (e) => {
    e.preventDefault();
    const searchValue = searchInput.value.trim();
    if (searchValue === '') {
        alert('Por favor, insira um nome de usuário válido para pesquisa.'); // Exibir um alerta se o campo estiver vazio
        return;
    }
    const userUrl = `${defaultUrl}/${encodeURIComponent(searchValue)}.md`; 
    window.open(userUrl, '_blank');
})
