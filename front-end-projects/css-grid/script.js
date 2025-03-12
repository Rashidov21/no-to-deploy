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

// let s1 = "Hello"
// let s2 = 'World'
// let s3 = `Hello ${s2}` // Hello World
// console.log(s1,s2,s3) // Hello World Hello World

// let i = 1 
// console.log(((i + 2) * 2) - (3 - i)) 

// let b1 = true
// let b2 = false 
// console.log(b1,b2)
// console.log(true + 1 )
// console.log(true - 1 )

// let x;
// console.log(x) // undefined

// let n = null
// console.log(n)


// let obj = {
//     name:"John",
//     age:30,
//     city:"New York",

// }

// console.log(obj)

// console.log(typeof Symbol("id"))
// console.log(typeof obj)
// console.log(typeof s2)
// console.log(typeof i)
// console.log(typeof b1)
// console.log(typeof xzx)

// Arifmetika 

// let n = 10;
// let s = "10";
// console.log(n + s)
// concat - birlashtirish > 10 + "10" = 1010
// s = Number(s) // 
// console.log(n + s) // 20
// n = String(n)
// console.log(n + s) // 1010

// let x = Number("abc")
// console.log(x) // NaN > Not a number

// console.log(25 * "2") // 50
// console.log(25 * "abc") // NaN
// console.log(25 / "2") // 12.5
// console.log(25 - "2") // 23
// console.log(25 + "2") // 252

// console.log("olma" - "behi") // NaN
// console.log("olma" + "behi") // olmabehi

// Bolganda qoldigini olish 
// console.log(7 % 3) // 1
// console.log(9 % 3) // 0
// console.log(8 % 3) // 2
// console.log(49 % 25) // 24

// // Darajaga kotarish 
// console.log(2 ** 2) // 4
// console.log(2 ** 10)  // 1024

// console.log(true + 1 * 4 / 3 - 1)  // 1.333333333333333
// console.log(((true + 1) * 4) / (3 - 1))  // 4

// let x = 1
// x += 1
// x -= 1
// x *= 2
// x /= 2
// console.log(x)

// increment / decrement 
// console.log(x++) // 1
// console.log(++x) // 2
// console.log(x--)
// console.log(--x)
// console.log(--x)
// console.log(--x)
// console.log(--x)

// let counter = 2;
// console.log(counter * ++counter)
// console.log(counter * --counter)

// console.log("" + 1 + 0)
// console.log("" - 1 + 0)
// console.log(true + false)
// console.log(6 / "3")
// console.log("2" * "3")
// console.log(4 + 5 + "px")
// console.log("$" + 4 + 5)
// console.log("4" - 2)
// console.log("4px" - 2)
// console.log("  -9  " - 5)
// console.log(null + 1)
// console.log(undefined + 1)
// console.log(" \t \n" - 2)


// task 1 
// let a = +prompt("A ni kiriting:")
// console.log("Perimetr = ", a * 4)

// // task 2 
// let s = +prompt("S ni kiriting:")
// console.log("Yuzasi = ", a ** 2,"kvm")
// console.log(Math.PI * 12)

// task 3
// let a = +prompt("A = ")
// let b = +prompt("B = ")

// console.log("Yuza = ", a * b)
// console.log("Perimetr = ", 2 * (a + b))

// task 4 
// let d = +prompt("D = ")
// console.log("Uzunlugi = ",Math.PI * d)
// console.log(Math.round(18.84955592153876))
// task 5
// let a = 17
// console.log("Hajmi = ",a ** 3)
// console.log("Sirti = ",6 * (a ** 2))

// task 6 
// let a,b,c;
// a = 6
// b = 4
// c = 8
// console.log("Hajmi = ",a * b * c)
// console.log("Sirti = ",2 * (a * b + b * c + a * c))

// console.log(1 > 0)
// console.log(1 < 0)
// let age = 17
// console.log(age >= 18)
// console.log(age <= 18)

// let value = 10;
// console.log(value == 10)
// console.log(value == "10")
// console.log(value === "10")
// console.log(1 == "1")
// console.log(true === "true")
// =  - qiymatni biriktirish operatori 
// == - tenglash operatori 
// === - qatiy tenglash operatori 

// console.log(null == undefined) //true
// console.log(undefined == 0) // false
// console.log(false == 0) // true
// console.log(false == "") // true
// console.log(0 == "") // true
// console.log(false == ".") // false

// let age = 19;
// if(age >= 17)
//     {
//     console.log("Welcome !")
// }
// else{
//     console.log("Close !")
// }

// let age = 120;
// let message;

// if (age < 3) {
//     message = 'Здравствуй, малыш!';
//     console.log(message)
// } else if (age < 18) {
//     message = 'Привет!';
//     console.log(message)
// } else if (age < 100) {
//     message = 'Здравствуйте!';
//     console.log(message)
// } else {
//     message = 'Какой необычный возраст!';
//     console.log(message)
//   }
// task 1 
// user son kiritadi agar soni 1 ga teng bolsa ekranga "Windows" chiqadi ...  
// 2 > "Linux"
// 3 > "Mac"
// 4 > "Android"
// 5 > "IOS"

// let a = 3
// if (a % 2 == 0){
//     console.log("Juft")
// }else{
//     console.log("Toq")
// }

let x = 8
let y = 2
if(x > y){console.log(x -y)}else if(x == y){console.log(0)}else{console.log(y - x)}
let temp = 28
let msg = temp > 25 ? "Issiq" : "Iliq";
console.log(msg)