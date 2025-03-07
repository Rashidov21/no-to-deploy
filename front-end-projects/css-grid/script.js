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

// alert()  - ogohlanuvchi
// confirm() - userdan tasdiqlash oynasi
// console.log()  - console ga chiqarish 
// prompt() - foydalanuvchidan ma'lumot olish

// let str_number = prompt("Sonni kirit :")
// console.log(str_number + 1) // 10 + 1 = 11 : '10' + '1' = '101'

// let int_number = +prompt("Sonni kirit :")
// console.log(int_number + 1) // 10 + 1 = 11

// comment
/* 
Пример с двумя 
сообщениями.
Это - многострочный 
комментарий.
*/

// Variable - o'zgaruvchi , kompyuterni RAM (tezkor xotirasida) ma'lum bir ma'lumotlarni saqlash uchun joy manzili (katakchaga manzil )

// 0x000001A734E3D080 = 10
// let num = 10 

// 192.168.1.1 
// kun.uz

// const , let , var 
// const x = 10; // o'zgarmas qiymat ya'ni konstanta 
// x = 15
// console.log(x) //Uncaught TypeError: Assignment to constant variable
// let y = 20; // o'zgaruvchi qiymat 
// let y = 65
// var z = 30; // o'zgaruvchi qiymat
// var z = 56
// console.log(z)

// 1-ingliz tilida bo'lishi kerak 
// 2-mantiqan to'g'ri nom 
// 3-faqat lotin harflari va _ , sonlardan ibora bolishi 
// let abc = 'images/profile/1.jpg'
// let userprofileimageurl = 'images/profile/1.jpg'

// let user1 = ''
// let _ = ''

// case styles 
// let userprofileimageurl = 'images/profile/1.jpg'
// // Camel Case 
// let userProfileImageUrl = 'images/profile/1.jpg'

// // Snake Case 
// let user_profile_image_url = 'images/profile/1.jpg'

// alert("Yoshingni kirit men senga yana shuncha yashasang nechiga kirishingni aytaman !")
// let userAge = +prompt("Yoshingni kirit :")
// console.log(userAge * 2)

// let non = 10
// let suv = 20
// console.log(non + suv)

// data type - qachonki ozgaruvchida 1 dona ma'lumot saqlash (str,int,bool)
// let x = 10
// data structure - qachonki ozgaruvchida bir nechta  ma'lumot saqlash
// let arr = [1,2,3,4,5]

// Javascipt DATA TYPES 
//     1. String - matn > !@#$wesdrtrfygbh16352153 >> "",'',``
//     2. Number - son > 013479 > -1,1.0,-2.5
//     3. Boolean - bool > true, false
//     4. Undefined - qiymati topilmagan > js tushunmagan barcha qiymat u uchun undefined    let x;
//     5. Null - mavjud emas 
//     6. Object - murakkab ma'lumotlar tuzilmasi > {name:"John", age:30, city:"New York"}
//     7. Symbol - unikal belgilarni ifodalash uchun
//     8. BigInt - katta butun sonlarni ifodalash uchun

let s1 = "Hello"
let s2 = 'World'
let s3 = `Hello ${s2}` // Hello World
console.log(s1,s2,s3) // Hello World Hello World

let i = 1 
console.log(((i + 2) * 2) - (3 - i)) 

let b1 = true
let b2 = false 
console.log(b1,b2)
console.log(true + 1 )
console.log(true - 1 )

let x;
console.log(x) // undefined

let n = null
console.log(n)


let obj = {
    name:"John",
    age:30,
    city:"New York",

}

console.log(obj)

console.log(typeof Symbol("id"))
console.log(typeof obj)
console.log(typeof s2)
console.log(typeof i)
console.log(typeof b1)
console.log(typeof xzx)
