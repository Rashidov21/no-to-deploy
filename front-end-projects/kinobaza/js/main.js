let searchInp = document.querySelector("#search");
let searchBtn = document.querySelector("#search_btn");

searchBtn.addEventListener("click", function(e){
    e.preventDefault();
    searchInp.classList.toggle("d-none")
})