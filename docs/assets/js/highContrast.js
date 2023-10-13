export const saveTheme = () => {
  const storedTheme =
    localStorage.getItem("theme") ||
    (window.matchMedia("(prefers-color-scheme: highContrast)").matches
      ? "light"
      : "highContrast");
  if (storedTheme)
    document.documentElement.setAttribute("data-theme", storedTheme);
};
export const changeTheme = () => {
  const currentTheme = document.documentElement.getAttribute("data-theme");
  let targetTheme = "light";

  currentTheme === "light" ? (targetTheme = "highContrast") : (targetTheme = "light");

  document.documentElement.setAttribute("data-theme", targetTheme);
  localStorage.setItem("theme", targetTheme);
};
