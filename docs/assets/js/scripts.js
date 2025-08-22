const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', (e) => {
  e.preventDefault(); // Impede o comportamento padrão do botão
  const searchValue = searchInput.value; // Captura o valor digitado no campo de pesquisa

  // Verifica se o campo de pesquisa está vazio
  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.'); // Exibe um alerta se o campo estiver vazio
    return; // Sai da função se o campo estiver vazio
  }

  // Monta a URL com o valor da pesquisa
  const url = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`; 
  const defaultUrl = 'https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community';

  // Abre a URL em uma nova aba
  window.open(url, '_blank');

  // Limpa o campo de pesquisa após a ação de abrir a URL
  searchInput.value = ''; // Isso limpa o campo de pesquisa

  // Verifica se o campo de pesquisa estava vazio para abrir a URL padrão
  if (searchValue === '') {
    window.open(defaultUrl, '_blank'); // Abre a URL padrão em uma nova aba
    return; // Sai da função após abrir a URL padrão
  }

  // Este trecho não será alcançado, porque o retorno já foi executado se o campo estava vazio
  // window.open(url, '_blank'); // Esta linha é desnecessária
});