const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const textarea = document.getElementById('markdown');
const output = document.getElementById('output');
const convertButton = document.getElementById('convertButton');

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

textarea.addEventListener('input', (e) => {
  e.preventDefault();
  const converter = new showdown.Converter({
    simpleLineBreaks: true,
    strikethrough: true,
    tables: true,
    ghCompatibleHeaderId: true,
    emoji: true,
    disableForced4SpacesIndentedSublists: true, 
    literalMidWordUnderscores: true 
  });

  function updatePreview() {
    const markdownText = textarea.value;
    const html = converter.makeHtml(markdownText);
    output.innerHTML = html;
  }

  updatePreview();
                      
})