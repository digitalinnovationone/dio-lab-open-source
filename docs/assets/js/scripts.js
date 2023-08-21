const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', async (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  const url = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`; 

  await fetch(url)
          .then(res => {
            if (res.status == 404)
              window.alert("Esse usuário não existe no repositório!")
            else
              window.open(url, '_blank');
          })
          .catch(e => {
            console.error(e);
          })
})