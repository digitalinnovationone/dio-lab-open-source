const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const suggestionsModal = document.getElementById("suggestionsModal");
const suggestionsList = document.getElementById("suggestionsList");

async function fetchAndDisplaySuggestions() {
  try {
    const apiUrl =
      "https://api.github.com/repos/digitalinnovationone/dio-lab-open-source/contents/community";
    const response = await fetch(apiUrl);
    const data = await response.json();

    const mdFiles = data
      .filter((item) => item.type === "file" && item.name.endsWith(".md"))
      .map((item) => item.name.replace(".md", ""));

    searchInput.addEventListener("input", updateSuggestions);

    function updateSuggestions() {
      const inputValue = searchInput.value.toLowerCase();
      const filteredSuggestions = mdFiles.filter((suggestion) =>
        suggestion.toLowerCase().includes(inputValue)
      );
      displaySuggestions(filteredSuggestions);
    }

    function displaySuggestions(filteredSuggestions) {
      if (filteredSuggestions.length > 0) {
        suggestionsModal.style.display = "block";
      } else {
        suggestionsModal.style.display = "none";
      }

      suggestionsList.innerHTML = "";

      for (let i = 0; i < filteredSuggestions.length; i++) {
        const suggestion = filteredSuggestions[i];
        const suggestionItem = document.createElement("li");
        suggestionItem.textContent = suggestion;
        suggestionItem.addEventListener("click", () => {
          searchInput.value = suggestion;
          suggestionsModal.style.display = "none";
        });

        suggestionsList.appendChild(suggestionItem);
      }
    }
  } catch (error) {
    console.error("Erro ao buscar dados da API:", error);
  }
}

fetchAndDisplaySuggestions();

searchButton.addEventListener("click", (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  if (searchValue === "") {
    alert("Por favor, insira um termo de pesquisa.");
  } else {
    const url = `https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/community/${encodeURIComponent(
      searchValue
    )}.md`;

    window.open(url, "_blank");
  }
});

document.addEventListener("click", (e) => {
  if (!suggestionsModal.contains(e.target) && e.target !== searchInput) {
    suggestionsModal.style.display = "none";
  }
});
