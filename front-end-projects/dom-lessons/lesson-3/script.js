
window.addEventListener("scroll", (evt)=>{
    let top = evt.target.scrollingElement.scrollTop
    console.log(top)
    if(top >= 400 ){
        let section1 = document.querySelector("#section1")
        section1.style.position = "sticky"
        section1.style.top = "0"
        section1.style.height = "100px"
    }
    if(top >= 800 ){
        let section2 = document.querySelector("#section2")
        section2.style.position = "sticky"
        section2.style.top = "100px"
        section2.style.height = "100px"
    }
    if(top >= 800 ){
        let section3 = document.querySelector("#section3")
        section3.style.position = "sticky"
        section3.style.top = "300px"
        section3.style.height = "100px"
    }
    
})



// let box = document.querySelector(".box")
// // width bilan height olish 
// console.log(box.offsetWidth) // 200
// console.log(box.offsetHeight) // 200
// // box.style.width = `${box.offsetWidth * 2}px` // 400px
// // borderlarni olish 
// console.log(box.clientTop)
// console.log(box.clientLeft)
// // element ichidagi kontent egallagan joyni toliq olish 
// console.log(box.scrollWidth)
// console.log(box.scrollHeight)

// box.addEventListener("scroll", ()=>{
//     console.log(box.scrollTop) // skrol bolayotgan elementni TOP qismidan qancha px skrol bolgani
//     console.log(box.scrollLeft) // bu esa LEFT dan 
// })
