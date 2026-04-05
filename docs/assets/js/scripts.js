const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

const repoOwner = 'elidianaandrade';
const repoName = 'dio-lab-open-source';
const directoryPath = 'community';

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.'); // Exibir um alerta se o campo estiver vazio
    return;
  }
  const url = `https://github.com/${repoOwner}/${repoName}/tree/main/community/${encodeURIComponent(searchValue)}.md`; 
  const defaultUrl = `https://github.com/${repoOwner}/${repoName}/tree/main/community`
  if(searchValue===''){
    window.open(defaultUrl, '_blank')
  }
  window.open(url, '_blank');
})

$(document).ready(function () {
  $('#searchInput').select2({
      maximumSelectionLength: 1,
      placeholder: 'Search username',
      allowClear: true,
      width: '300px',
      ajax: {
          transport: function (params, success, failure) {
              const query = params.data.term ? params.data.term.toLowerCase() : '';
              console.log(query)

              const url = `https://api.github.com/repos/${repoOwner}/${repoName}/contents/${directoryPath}`;

              $.ajax({
                  url: url,
                  type: 'GET',
                  success: function(data) {
                      const filteredList = data.filter(function (obj) {
                          return obj.name.toLowerCase().includes(query);
                      });
                      success({
                          results: filteredList.map(file => ({ id: file.name.replace(".md", ""), text: file.name.replace(".md", "") }))
                      });
                  },
                  error: function(xhr, status, error) {
                      failure(error);
                  }
              });
          },
          processResults: function (data) {
              return {
                  results: data.results
              };
          }
      }
  });
});