document.addEventListener("DOMContentLoaded", (event) => {
    document
      .querySelector("#search-btn")
      .addEventListener("click", (event) => {
        event.preventDefault();
        const data = document.querySelector("#search-field").value;
        window.location.href = `/search/${data}/`;
      });
  });