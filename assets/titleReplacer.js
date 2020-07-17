let titleSlug = document.querySelector("input[name=title]");
let slugTitle = document.querySelector("input[name=slug]");
let titleReplacer = (input) => {
  return input
    .toString()
    .toLowerCase()
    .trim()
    .replace([/&/g, "-and-"])
    .replace(/[\s\W-]+/g, "-");
};

titleSlug.addEventListener("keyup", (e) => {
  slugTitle.setAttribute("value", titleReplacer(titleSlug.value));
});
