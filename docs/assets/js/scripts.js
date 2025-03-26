const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  if (searchValue === '') {
    alert('Por favor, insira um termo de pesquisa.'); 
    return;
  }
  const url = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(searchValue)}.md`; 
  const defaultUrl = 'https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community'
  if(searchValue===''){
    window.open(defaultUrl, '_blank')
  }
  window.open(url, '_blank');
})

document.addEventListener("DOMContentLoaded", () => {
    const toggleThemeBtn = document.getElementById("toggleTheme");
  
    
    if (localStorage.getItem("theme") === "dark") {
      document.body.classList.add("dark-mode");
      toggleThemeBtn.textContent = "☀️";
    } else {
      toggleThemeBtn.textContent = "🌙"; 
    }
  
    
    toggleThemeBtn.addEventListener("click", () => {
      document.body.classList.toggle("dark-mode");
  
      if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
        toggleThemeBtn.textContent = "☀️"; 
      } else {
        localStorage.setItem("theme", "light");
        toggleThemeBtn.textContent = "🌙"; 
      }
    });
  });
  