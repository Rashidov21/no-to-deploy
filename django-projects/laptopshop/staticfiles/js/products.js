// Products pages
let categoryTitle = document.querySelector(".categorys__title");
let categorysList = document.querySelector(".categorys__list");

let manufacturersTitle = document.querySelector(".manufacturers__title");
let manufacturersList = document.querySelector(".manufacturers__list");

let priceTitle = document.querySelector(".price__title");
let priceList = document.querySelector(".price__list");

let colorsTitle = document.querySelector(".colors__title");
let colorsList = document.querySelector(".colors__list");

function toggleClass(clickEl, classEl) {
  clickEl.addEventListener("click", ()=> {
    classEl.classList.toggle("active-lists");
    clickEl.classList.toggle("active-arrow");
  })
}

toggleClass(categoryTitle, categorysList);
toggleClass(manufacturersTitle, manufacturersList);
toggleClass(priceTitle, priceList);
toggleClass(colorsTitle, colorsList);

// ==================================

let productBox = document.querySelector(".tabs-box")
let productOpenBtn = document.querySelector(".products-box__btn");
let productCloseBtn = document.querySelector(".close-btn");

productOpenBtn.addEventListener("click", (evt) => {
  evt.preventDefault();
  productBox.classList.add("tabs-box--active");
})

productCloseBtn.addEventListener("click", () => {
  productBox.classList.remove("tabs-box--active");
})