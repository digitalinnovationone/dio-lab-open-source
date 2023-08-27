let size = 16;
const reset = 16;
export const fontIncrease = () => {
  let style = document.body.style;
  let fontIncrease = size++;
  if (fontIncrease >= 20) {
    fontReset();
  }
  style.fontSize = fontIncrease + "px";
};
export const fontDecrease = () => {
  let style = document.body.style;
  let fontDecrease = size--;
  if (fontDecrease <= 12) {
    fontReset();
  }
  style.fontSize = fontDecrease + "px";
};
export const fontReset = () => {
  let style = document.body.style;
  style.fontSize = reset + "px";
  size = reset;
};
