import { fontDecrease, fontIncrease, fontReset } from "./font.js";
import { saveTheme, changeTheme } from "./highContrast.js";

const theme = document.getElementById("theme");
const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const fontIncreaseButton = document.getElementById("font__increase");
const fontResetButton = document.getElementById("font__reset");
const fontDecreaseButton = document.getElementById("font__decrease");
saveTheme();


searchButton.addEventListener("click", (e) => {
  e.preventDefault();
  const searchValue = searchInput.value;
  const url = `https://github.com/elidianaandrade/dio-lab-open-source/tree/main/community/${encodeURIComponent(
    searchValue
  )}.md`;
  window.open(url, "_blank");
});

fontIncreaseButton.addEventListener("click", () => {
  fontIncrease();
});
fontResetButton.addEventListener("click", () => {
  fontReset();
});
fontDecreaseButton.addEventListener("click", () => {
  fontDecrease();
});
theme.addEventListener("click", () => {
  changeTheme();
});
