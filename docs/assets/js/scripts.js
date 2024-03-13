const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");

searchButton.addEventListener("click", (e) => {
  e.preventDefault();
  const searchValue = searchInput.value.trim();
  if (searchValue === "") {
    alert("Por favor, insira um termo de pesquisa."); // Exibir um alerta se o campo estiver vazio
    return;
  }

  verifyUsernameExists(searchValue);
});

function verifyUsernameExists(searchValue) {
  const urlApi = `https://api.github.com/repos/digitalinnovationone/dio-lab-open-source/git/trees/81f84c8cabb62b4c7138e77283603305cd526812`;
  const urlReadMe = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(
    searchValue
  )}.md`;

  fetch(urlApi)
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      } else if (response.status === 404) {
        console.log("O arquivo não existe.");
      } else {
        console.error("Erro:", response.status);
      }
    })
    .then((data) => {
      return verify(data.tree, searchValue);
    })
    .then((exist) => {
      if (exist) window.open(urlReadMe, "_blank");
      else treatMessageError();
    })
    .catch((error) => console.error(error));
}

function verify(tree, searchValue) {
  searchValue += ".md";

  return new Promise((resolve) => {
    tree.forEach((arq) => {
      if (arq.path == searchValue) {
        resolve(true);
      }
    });
    resolve(false); // Se o arquivo não for encontrado
  });
}

function treatMessageError() {
  document.getElementById("alert-message").style.display = "block";
}
document.getElementById("searchInput").addEventListener("input", () => {
  document.getElementById("alert-message").style.display = "none";
});
