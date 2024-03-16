const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");

searchButton.addEventListener("click", handleSearch);

function handleSearch(e) {
  e.preventDefault();
  const searchValue = searchInput.value.trim();
  if (searchValue === "") {
    alert("Por favor, insira um termo de pesquisa."); 
    return;
  }
  verifyUsernameExists(searchValue);
}

async function verifyUsernameExists(searchValue) {
  try {
    const urlApi = `https://api.github.com/repos/digitalinnovationone/dio-lab-open-source/git/trees/main`;
    const response = await fetch(urlApi);
    if (response.status === 200) {
      const data = await response.json();
      const url = data.tree.find((o) => o.path === "community").url;
      const response2 = await fetch(url);
      const obj = await response2.json();
      const exist = verify(obj.tree, searchValue);
      if (exist) {
        const urlReadMe = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`;
        window.open(urlReadMe, "_blank");
      } else {
        treatMessageError();
      }
    }
  } catch (error) {
    console.error(error);
  }
}

function verify(tree, searchValue) {
  searchValue += ".md";
  return tree.some((arq) => arq.path === searchValue);
}

function treatMessageError() {
  document.getElementById("alert-message").style.display = "block";
}

searchInput.addEventListener("input", () => {
  document.getElementById("alert-message").style.display = "none";
});
