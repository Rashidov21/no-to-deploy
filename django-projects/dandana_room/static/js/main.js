let elBurger = document.querySelector(".dandana-header__inner-burger")
let elSidebar = document.querySelector(".sidebar")
let elTitle = document.querySelector(".sidebar-inner__services-title")
let elSecBurger = document.querySelector(".sec-burger")

elBurger.addEventListener("click", ()=>{
  elSidebar.classList.add("active")
  document.body.classList.add("body-hidden")
})
elSecBurger.addEventListener("click", ()=>{
  elSidebar.classList.remove("active")
  document.body.classList.remove("body-hidden")
})
