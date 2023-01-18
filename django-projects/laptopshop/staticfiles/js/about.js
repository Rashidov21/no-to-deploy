const addBtn = document.querySelector(".add-btn"),
  minusBtn = document.querySelector(".minus-btn"),
  result = document.querySelector(".amount-result");

let a = 1;

addBtn.addEventListener("click", () => {
  a++;
  result.textContent = a;
})

minusBtn.addEventListener("click", () => {
  if (a > 1) {
    a--;
    result.textContent = a;
  }
})