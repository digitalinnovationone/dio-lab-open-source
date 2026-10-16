// HTML exemplo
/*
<div id="question">Clique no botão verde</div>
<button id="btnGreen" style="background-color: green;">Verde</button>
<button id="btnRed" style="background-color: red;">Vermelho</button>
<audio id="soundCorrect" src="correct.mp3"></audio>
<audio id="soundWrong" src="wrong.mp3"></audio>
*/

// JS para feedback
const btnGreen = document.getElementById('btnGreen');
const btnRed = document.getElementById('btnRed');
const soundCorrect = document.getElementById('soundCorrect');
const soundWrong = document.getElementById('soundWrong');

btnGreen.addEventListener('click', () => {
  showFeedback(true);
});

btnRed.addEventListener('click', () => {
  showFeedback(false);
});

function showFeedback(isCorrect) {
  if (isCorrect) {
    soundCorrect.play();
    document.body.style.backgroundColor = '#a6f3a6'; // verde claro
    setTimeout(() => {
      document.body.style.backgroundColor = '';
    }, 1000);
  } else {
    soundWrong.play();
    document.body.style.backgroundColor = '#f3a6a6'; // vermelho claro
    setTimeout(() => {
      document.body.style.backgroundColor = '';
    }, 1000);
  }
}
  </script>
</body>
</html>
}
