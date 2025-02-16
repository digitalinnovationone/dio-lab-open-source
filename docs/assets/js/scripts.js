const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const textarea = document.getElementById('markdown');
const output = document.getElementById('output');
const convertButton = document.getElementById('convertButton');

const converter = new showdown.Converter({
  simpleLineBreaks: true,
  strikethrough: true,
  tables: true,
  ghCompatibleHeaderId: true,
  emoji: true,
  disableForced4SpacesIndentedSublists: true, 
  literalMidWordUnderscores: true 
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

function updatePreview() {
  const markdownText = textarea.value;
  const html = converter.makeHtml(markdownText);
  output.innerHTML = html;
}

function loadCommunityMarkdown() {
  fetch('/community/ViniciusKoiti.md')
    .then(response => {
      if (!response.ok) {
        throw new Error(`Erro ao buscar o arquivo: ${response.statusText}`);
      }
      return response.text();
    })
    .then(markdown => {
      textarea.value = markdown;
      updatePreview();
    })
    .catch(error => {
      console.error('Erro ao carregar o Markdown:', error);
      output.innerHTML = `<p>Erro ao carregar o conteúdo: ${error.message}</p>`;
    });
}

loadCommunityMarkdown();


textarea.addEventListener('input', updatePreview);