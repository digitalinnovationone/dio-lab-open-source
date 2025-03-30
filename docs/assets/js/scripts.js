const searchInput = document.getElementById('searchInput');
        const searchButton = document.getElementById('searchButton');
        const searchResults = document.getElementById('searchResults');

        searchButton.addEventListener('click', async (e) => {
            e.preventDefault();
            const searchValue = searchInput.value.trim();
            if (searchValue === '') {
                alert('Por favor, insira um termo de pesquisa.');
                return;
            }

            // Fetch profiles dynamically
            try {
              const response = await fetch('https://api.github.com/repos/elidianaandrade/dio-lab-open-source/contents/community');
              const files = await response.json();

                // Filter profiles matching the search term
                const filteredFiles = files.filter(file => file.name.includes(searchValue));

                // Clear previous results
                searchResults.innerHTML = '';
                searchResults.style.display = 'block';

                if (filteredFiles.length > 0) {
                  for (const file of filteredFiles) {
                      const li = document.createElement('li');
                      li.classList.add('fade-in');
                      li.innerHTML = `<a href="${file.html_url}" target="_blank">${file.name}</a>`;
                      searchResults.appendChild(li);
                  }
              } else {
                  const li = document.createElement('li');
                  li.classList.add('fade-in');
                  li.textContent = 'Nenhum perfil encontrado.';
                  searchResults.appendChild(li);
              }
          } catch (error) {
              console.error('Erro ao buscar perfis:', error);
              alert('Erro ao buscar perfis. Por favor, tente novamente mais tarde.');
          }
        });