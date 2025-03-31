const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', async (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;

  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.'); // Exibir um alerta se o campo estiver vazio

    return;
  }

  const url = {
    redirect: `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`,
    api: `https://api.github.com/repos/elidianaandrade/dio-lab-open-source/contents/community/${encodeURIComponent(searchValue)}.md`
  }

  try { 
    const exist = await fetch(url.api); // Faz a requisição para verificar a existência do arquivo

    if (!exist.ok) throw new Error('Ocorreu um erro ou este perfil não existe, por favor confira o nome e tente novamente.');
 
    window.open(url.redirect, '_blank');
  } catch (error) {
    alert(error);
  }
});