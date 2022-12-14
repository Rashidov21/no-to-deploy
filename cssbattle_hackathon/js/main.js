window.addEventListener("scroll", () => {
  let header = document.querySelector("header")
  header.classList.toggle("scroll", window.scrollY > 0)
})

let lines = document.querySelectorAll(".line"),
  header_navbar = document.querySelector(".header_navbar")
for (let i = 0; i < lines.length; i++) {
  lines[i].addEventListener("click", () => {
    header_navbar.classList.toggle("opened")
    for (var i = 0; i < lines.length; i++) {
      lines[i].classList.toggle("opened")
    }
  })
}

header_navbar_item = document.querySelectorAll(".header_navbar_item")
for (let i = 0; i < header_navbar_item.length; i++) {
  header_navbar_item[i].addEventListener("click", () => {
    for (var i = 0; i < lines.length; i++) {
      lines[i].classList.toggle("opened")
    }
    header_navbar.classList.toggle("opened")
  })
}

function updateProgressBar() {
  const {
    scrollTop,
    scrollHeight
  } = document.documentElement;
  const scrollPercent = scrollTop / (scrollHeight - window.innerHeight) * 100 + '%';
  let prbar = document.querySelector(".header_line");
  prbar.style.width = `${scrollPercent}`;
  let header_height = document.querySelector("header").getBoundingClientRect().height
  prbar.style.top = `0px`
}

window.addEventListener('scroll', updateProgressBar);


window.addEventListener("load", () => {
  let header_height = document.querySelector("header").getBoundingClientRect().height
  let prbar = document.querySelector(".header_line");
  prbar.style.top = `${header_height}px`
})

document.querySelectorAll(".section_faq_inner_item").forEach((el) => {
  el.addEventListener("click", () => {
    let content = el.nextElementSibling
    let btn = el.lastElementChild
    let btns = document.querySelectorAll(".section_faq_btn")
    if (content.style.maxHeight) {
      let accordions = document.querySelectorAll(".section_faq_inner_item_accordion")
      for (let i = 0; i < accordions.length; i++) {
        accordions[i].style.maxHeight = null
        accordions[i].style.marginTop = 0
        btns[i].classList.remove("opened")
      }
    } else {
      let btn = el.lastElementChild
      let accordions = document.querySelectorAll(".section_faq_inner_item_accordion")
      for (let i = 0; i < accordions.length; i++) {
        accordions[i].style.maxHeight = null
        accordions[i].style.marginTop = 0
        btns[i].classList.remove("opened")
      }
      content.style.maxHeight = content.scrollHeight + "px"
      content.style.marginTop = 18 + "px"
      btn.classList.toggle("opened")
    }
  })
})