const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");

searchButton.addEventListener("click", async (e) => {
  e.preventDefault();
  const searchValue = searchInput.value.trim();

  if (searchValue === "") {
    alert("Por favor, insira um termo de pesquisa."); // Exibir um alerta se o campo estiver vazio
    return;
  }

  const textContentButtonDefault = searchButton.getHTML();

  searchButton.disabled = true;
  searchButton.textContent = "Verificando...";

  try {
    // Usar a API do GitHub para verificar se o arquivo existe
    const apiUrl = `https://api.github.com/repos/elidianaandrade/dio-lab-open-source/contents/community/${encodeURIComponent(
      searchValue
    )}.md`;

    const response = await fetch(apiUrl);

    if (response.ok) {
      const fileUrl = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(
        searchValue
      )}.md`;

      window.open(fileUrl, "_blank");
    } else if (response.status === 404) {
      alert(
        "Perfil não encontrado. Verifique o nome de usuário e tente novamente."
      );
    } else {
      alert("Erro ao verificar o arquivo. Tente novamente mais tarde.");
    }
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro de conexão. Verifique sua internet e tente novamente.");
  } finally {
    // Restaurar estado inicial do botão
    searchButton.disabled = false;
    searchButton.innerHTML = textContentButtonDefault;
  }
});
