let navList = document.querySelector(".nav-list");
let burgerBtn = document.querySelector(".burger");

burgerBtn.addEventListener("click", ()=> {
  navList.classList.toggle("nav-list--active");
  burgerBtn.classList.toggle("burger-active")
})








