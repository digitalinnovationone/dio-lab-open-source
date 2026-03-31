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

const searchLinkedinInput = document.getElementById('searchLinkedinInput');
const searchLinkedinButton = document.getElementById('searchLinkedinButton');

searchLinkedinButton.addEventListener('click', (e) => {
    e.preventDefault();
    const searchValue = searchLinkedinInput.value;

    if (searchValue === '') {
        alert('Por favor, insira um nome de usuário do GitHub.');
        return;
    }

    const fileUrl = `https://raw.githubusercontent.com/digitalinnovationone/dio-lab-open-source/main/community/${encodeURIComponent(searchValue)}.md`;

    fetch(fileUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Perfil do GitHub não encontrado.');
            }
            return response.text();
        })
        .then(data => {
            // NOVA EXPRESSÃO REGULAR: mais flexível para encontrar qualquer URL do LinkedIn
            const regex = /https?:\/\/(?:www\.)?linkedin\.com\/in\/[^\s/]+/i;
            const match = data.match(regex);

            if (match) {
                const linkedinUrl = match[0];
                window.open(linkedinUrl, '_blank');
            } else {
                alert('Link do LinkedIn não encontrado no perfil do GitHub.');
            }
        })
        .catch(error => {
            alert(error.message);
        });
});