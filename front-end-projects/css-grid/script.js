// console.log("Hello world");
const input = document.getElementById("bgchange");
input.addEventListener("input", (e) => {
    const body = document.getElementsByClassName("body-dark")[0];
    console.log(`rgb(${e.target.value*2.5}, ${e.target.value*2.5}, ${e.target.value*2.5})`)
    const value = 255 - (e.target.value*2.5)
    body.style.background = `rgb(${value}, ${value}, ${value})`;
    const span = document.getElementById("value");
    span.innerHTML = value
})

// Js Framewroks 
// React 
// Node.js
//     Tez , mashxur , ish kop , keng ommalashgan
//     O'rganish ko'p vaqt talab qiladi 
// Vue
//     Eng Tez , mashxur , ish o'rtacha
//     Organish osonroq nisbatan, 
// Node.js

// JavaScript basic 
