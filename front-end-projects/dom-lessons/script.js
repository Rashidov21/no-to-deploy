// DOM - document object model

// document > html 
// object > js object > {name:"Document"}
// model > ko'rinish 

// let obj = {
//     name:"Document",
//     length: 100,
//     pageCount:2,
//     load:function(){
//         alert("Welcome to my Page !")
//     }
// }

// console.log(obj);
// console.log(obj.name);
// console.log(obj.length);
// console.log(obj.pageCount);
// obj.load();
// obj.load = () => {
//     alert(2 + 2)
// }
// obj.load();

// console.log(document);
// console.dir(document);

// const main = document.getElementById("main");
// console.log(main);
// main.style.display = "none";
// let li = document.getElementsByTagName("li")
// console.log(li)
// let ul = document.getElementsByClassName("navbar")

// let sec = document.querySelector(".section")
// console.log(sec)
// let lis = document.querySelectorAll(".li-item")
// lis.forEach(li => {
//     li.style.fontSize = "20px"
// })

// document.getElementById  - hujjatdan siz korsatgan ID boyicha elementni topish 
// document.querySelector - hujjatdan siz korsatgan css selector boyicha elementni topish
// document.getElementsByClassName - hujjatdan siz korsatgan class boyicha elementni topish
// document.getElementsByTagName - hujjatdan siz korsatgan tag boyicha elementni topish
// document.querySelectorAll - hujjatdan siz korsatgan class boyicha elementni topish

// let body = document.body;
// let colors = ["red","blue","yellow","orange"]
// // console.log(Math.floor(Math.random() * colors.length));
// function getRandomColor(){
//     let randomNumber = Math.floor(Math.random() * colors.length)
//     return colors[randomNumber]
// }
// // console.log(getRandomColor());
// setInterval(() => {
//     body.style.backgroundColor = getRandomColor();
// },1000)
let section = document.querySelector(".section")
console.log(section.parentElement)
console.log(section.childElementCount)
console.log(section.children)
console.log(section.firstElementChild)
console.log(section.lastElementChild)
let li = document.querySelector("#about")
console.log(li.nextElementSibling)
console.log(li.previousElementSibling)

let closeBtn = document.querySelector("#close")

closeBtn.onclick = function(){
    closeBtn.parentElement.style.display = "none"
}