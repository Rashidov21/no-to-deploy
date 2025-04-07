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

// let x = 8
// let y = 2
// if(x > y){console.log(x -y)}else if(x == y){console.log(0)}else{console.log(y - x)}
// let temp = 28
// let msg = temp > 25 ? "Issiq" : "Iliq";
// console.log(msg)

// let a = 1
// let b = 2
// and , or , not 
// and > && 
// or > ||
// not > !

// if(a > 2 && b <= 3){
//     console.log("OK")
// }else{
//     console.log("NO")
// }
// if(a > 2 || b <= 3){
//     console.log("OK")
// }else{
//     console.log("NO")
// }
// not true 
// console.log(!true)
// // not false 
// console.log(!false)

// let username = ""
// if(!username){
//     console.log("Ism kiritilmadi !")
// }else{
//     console.log(username)
// }

// const username = "johndoe"
// const age = 23
// if(username && age){
//     console.log(`username = ${username} \nage=${age}`)
// }else if(username || age){
//     console.log("username yoki age bo'sh qolgan !")
// }
// else{
//     console.log("Maydonlar toldirilmagan !")
// }

// console.log(1 || 0) // 1
// console.log(1 && 0) // 0
// console.log(!0) // true
// console.log(!1) // false
// console.log("" || 0 || false || 1) // 1
// console.log(1 && false && 0 && '') // false

// let counter = 0
// let a = 1;
// let b = -11;
// let c = -1;
// if(a >= 0){
//     counter += 1
// }
// if(b >= 0){
//     counter += 1
// }
// if(c >= 0){
//     counter += 1

// }
// if(counter == 1){
//     console.log("Faqat bittasi musbat")
// }else{
//     console.log("musbatlar yoq")
// }


// let num = "313"

// if(num[0] != num[1] && num[2] != num[0]){
//     console.log(true)
// }else{
//     console.log(false)
// }

// for while do while


// console.log(1)
// console.log(2)
// console.log(3)
// console.log(4)

// loop - sikl  > takrorlanish 
// for - sanoqli takrorlanish 
// let username = "John"
// console.log(username.length)
// for(let i = 0; i < username.length; i++){
//     // let x = +prompt("X = ")
//     // let y = +prompt("Y = ")
//     // console.log(x+y)
//     console.log(username[i])
// }

// for(let i = 1; i <= 10;i++){
//     console.log(i)
// }

// for(let k = 10; k >= 1; k--){
//     console.log(k)
// }

// i , j , k , x , n  



// while  - cheksiz takrorlanish 
// while(true){
//     console.log("Hello while")
// }

// let i = 0;
// while(i < 0){
//     i++
//     console.log(i)
// }
// let x = 0;
// do{
//     x++
//     console.log(x)
// }while(x < 0)

// for(let i = 0; i < 10;i++){
//     if(i % 2 == 0){
//         continue // siklni bajarmasdam keyingisi o'tish
//     }else if (i == 7){
//         break
//     }else{
//         console.log(i)
//     }
// }

// for(let i = 0; i < 5; i++){
//     let password = prompt("parolni kiriting : ")
//     if(password == "abc123"){
//         console.log("Xush kelibsiz !")
//         break // siklni toxtatish
//     }else{
//         console.log("Parol notogri !")
//     }
//     if(i == 2){
//         alert("Tizim blocklandi !")
//         break
//     }
// }
// const myNumber = 6;
// let counter = 0;
// while(true){
//     if(counter == 3){
//         alert("topolmadiz !")
//         break
//     }
//     counter++
//     let guess = +prompt("son kirit :")
//     if(guess == myNumber){
//         alert("yuttiz !")
//         break
//     }else{
//         continue
//     }
// }



// task 1
// userdan matn qabul qiling va matnda nechta unli harf bor ekanini aniqlang 

// input : olma olma duo ol 
// output: "unli harflar soni = 7"

// let text = "olma olma duo ol"
// let counter1 = 0
// let counter2 = 0
// for(let i = 0; i < text.length; i++){
//     if(text[i] == "a" || text[i] == "i" || text[i] == "e" || text[i] == "o" || text[i] == "u"){
//         counter1 += 1
//     }else{
//         if(text[i] != " "){
//             counter2 += 1
//         }
//     }
// }
// console.log("Unli harflar = ", counter1)
// console.log("Undosh harflar = ", counter2)

// const user = "johndoe"
// console.log(user[0])
// console.log(user[user.length - 1])

// task 2 
// berilgan matnni teskari qilib ekranga chiqaring
// input: "salom"
// output : "molas"
// let txt = "apple"
// let reversedText = ""
// for(let i = txt.length - 1; i >= 0; i--){
//     reversedText += txt[i]
// } 
// console.log(reversedText)

// task 3  
// quyidagi shaklda # larni ekranga chiqaring 
// #
// ## 
// ###
// ####
// #####
// let hashtag = "######"
// for(let i = 5; i > 0;i--){
//     console.log(hashtag.slice(0,i))
// }

// let n = "3211353465"
// let result = 0
// for(let i = 0; i < n.length; i++){
//     result += Number(n[i])
// }
// console.log(result)

// SWITCH CASE 
// switch(x) {
//     case 'value1':  // if (x === 'value1')
//       ...
//       [break]
  
//     case 'value2':  // if (x === 'value2')
//       ...
//       [break]
  
//     default:
//       ...
//       [break]
//   }

// let num = 4;
// switch(num){
//     case 1:
//         console.log("bir")
//         break
//     case 2:
//         console.log("ikki")
//         break
//     case 3:
//         console.log("uch")
//         break
//     case 4:
//         console.log("tort")
//         break
//     case 5:
//         console.log("besh")
//         break
// }

// let user = "admin"
// switch(user){
//     case "moderator":
        
//         if(prompt("enter your moderator password :") == "moder1"){
//             console.log("Welcome moderator !")
//         }else{
//             break 
//         }
//     case "admin":
//         if(prompt("enter your admin password :") == "admin1"){
//             console.log("Welcome Admin !")
//         }else{
//             break 
//         }
// }
// let browser = prompt("enter your actual browser :")
// switch (browser) {
//     case 'Edge':
//       alert( "You've got the Edge!" );
//       break;
  
//     case 'Chrome':
//     case 'Firefox':
//     case 'Safari':
//     case 'Opera':
//       alert( 'Okay we support these browsers too' );
//       break;
  
//     default:
//       alert( 'We hope that this page looks ok!' );
//   }

// Function 
// function - kod bo'lagi uni kodni istalgan joyida istalgan marta ishlatish mumkin 
// function declaration 
// function plus(a,b){
//     return a + b
// }
// let result = plus(1,2)
// console.log(result) // 3
// console.log(plus(2,2)) // 4

// function getUserFullName(firstName,lastName){
//     const fullName = firstName + " " + lastName
//     return fullName
// }
// console.log(getUserFullName("Ali","Valiyev"))
// console.log(getUserFullName("John","Doe"))
// console.log(getUserFullName("apple","banana"))
// console.log(getUserFullName("10","20"))

// console.log(Math.pow(2,2))
// console.log(Math.pow(2,3))
// console.log(Math.pow(2,4))
// console.log(Math.pow(2,10))
// function customPow(number){
//     return number ** 3
// }
// console.log(customPow(2,2))
// console.log(customPow(2,3))
// console.log(customPow(2,4))
// console.log(customPow(2,10))

// Calculator 
// let number1 = +prompt("Number 1 : ")
// let number2 = +prompt("Number 2 : ")
// let action = prompt("+ / - / * / / : ")
// if(action == "+"){
//     alert(plus(number1,number2))
// }else if(action == "-"){
//     alert(minus(number1,number2))
// }else if(action == "*"){
//     alert(multiply(number1,number2))
// }else{
//     alert(division(number1,number2))
// }
// function plus(a,b){
//         return a + b
// }
// function minus(a,b){
//         return a - b
// }
// function multiply(a,b){
//         return a * b
// }
// function division(a,b){
//         return a / b
// }
// min - 6 length 
// letters , numbers , symbols

// function checkPassword(text){
//     if(text.length < 6){
//         return "Password min 6 length "
//     }else{
//         return "Password set !"
//     }
// }

// console.log(checkPassword("admin123"))

// function expressions 
// console.log(checkPassword)

// let x = checkPassword
// console.log(x("qwerty123"))



// let z = 1;
// if(z){
//     let getName = function(a,b){
//         return a + b
//     }
//     console.log(getName(1,2))
// }
// console.log(getName(2,3))

// function functionName () {}
// let fname = function(){}
// let func = (c,e,d) => {
//     return c + e + d
// }
// console.log(func(1,2,3)) // 6

// let text = "witcher"
// let checkW = (text) => {
//     if(text[0]=="w" || text[0] == "W"){
//         console.log("W !")
//     }else{
//         console.log("W not defined!")
//     }
// } 
// checkW(text)

// task 1 
// userdan 1 dan 10 gacha bolgan istalgan son qabul qiling agar son 5 dan kichik bolsa uni 2 ga kopaytiramiz
// agar 5 dan katta bolsa uni 2 ga bolamiz 

// bo'lish va kopayritish amallarini alohida funksiyalar orqali amalga oshiring ,

// task 2
// userdan 10 ta familya qabul qiling va nechta erkak kishi nechta ayol kishini familyasi bor ekanini hisoblaysiz 


// let man = 0
// let women = 0
// function checkGender(surname){
//     if(surname.endsWith("v")){
//         man += 1
//     }else{
//         women += 1
//     }
// }
// for(let i = 0; i < 5; i++){
//     checkGender(prompt("surname :"))
// }
// console.log("Mans : ", man)
// console.log("Woman : ", women)

// task 3
// userdan cheklanmagan miqdorda sozlar qabul qiling , agar soz "stop" bolsa barcha kiritgan sozlari ichida nechta url yoki sayt nomi bor ekanini toping 
// let site_count = 0
// while(true){
//     let word = prompt("soz kiriting : ")
//     if(word == "stop"){
//         break
//     }else{
//         if(word.startsWith("http") || word.startsWith("www")){
//             site_count += 1
//         }
//     }
// }
// console.log(site_count)

// homework 
// userdan istalgancha soz qabul qiling
//  va kiritilgan sozlar ichida nechta harf ,
//  nechta raqam va nechta maxsus belgi borligini aniqlang
//  , "stop" deb soz kiritilsa kod toxtashi kerak 
// va natijalar ekranga chiqadi 
// let letters = "qwertyuiopasdfghjklzxcvbnm"
// let numbers = "0123456789"
// let symbols = "!@#$%^&*()_"
// let letters_count = 0
// let numbers_count = 0
// let symbols_count = 0

// while(true){
//     let word = prompt("Soz kiriting:")
//     if(word == "stop"){
//         break
//     }
//     for(let i=0;i < word.length; i++){
//         for(let i = 0; i < letters.length; i++){
//             if(word[i] == letters[i]){
//                 letters_count += 1
//             }else{
//                 continue
//             }
//         }
//         for(let i = 0; i < number.length; i++){
//             if(word[i] == number[i]){
//                 numbers_count += 1
//             }
//         }
//         for(let i = 0; i < symbols.length; i++){
//             if(word[i] == symbols[i]){
//                 symbols_count += 1
//             }
//         }
//     }
   
// }

// let str = "abc01273910"
// let numbers = []
// for(let i = 0; i < str.length; i++){
//     if(Number(str[i])){
//         numbers.push(Number(str[i]))
//     }
//     if(Number(str[i]) % 2 == 0){
//         console.log("Juft son ", str[i])
//     }else{
//         console.log("Toq son ", str[i])
//     }
// }

// console.log(Boolean(NaN)) // false
// console.log(numbers)
// numbers.sort()
// console.log(numbers)
// console.log(numbers[numbers.length - 1])


// OBJECTS 

// let x = 10
// let array = [1,2,3,4,5]

// object - attribute , method 

// let user = new Object()
// let user = {
//     firstName:"John",
//     lastName:"Doe",
//     age:26,
//     username:"admin",
//     password:"******",
//     sayHi:function(){
//         alert(`Hi, iam ${this.firstName}`)
//     },
//     plus:function(x,y){
//         return x + y
//     }
// }
// console.log(typeof user) // object
// console.log(user) // object
// console.dir(user) // object
// user.sayHi()
// console.log(user.plus(1,2))

// let customSayHI = user.sayHi
// customSayHI()

// array , node lists 
// [0,1,2,3]
// let obj = {
//     name:"John",
//     age:20,
//     "game_console":"PS5"
// }
// // in  - mavjudlikka tekshirish 
// console.log("name" in obj) // true
// console.log("points" in obj) // false

// for (key in obj) {
//     console.log(obj[key])
// }
// obj.salary = 5200
// console.log(obj)
// delete obj.salary
// console.log(obj)
// obj["points"] = 54
// console.log(obj)

// task 1
let salaries = {
    john: 100,
    ann: 160,
    pete: 130
  }
// ushbu objectdagi userlar oylik maoshlarini hisoblang
let summa = 0
for (key in salaries) {
    summa += salaries[key]
}
console.log("umumiy summa = ", summa)

// task 2 
// name va age qabul qilib, shu qiymatlar bilan obyekt qaytaradigan funksiya yozing
// input: "John",23
// output: {name:"John",age:23}

function createObj(name,age){
    return {name:name,age:age}
}
console.log(createObj("john",23))
console.log(createObj("Valijon",30))

// new Object(), new Array, new Date
console.log(new Date().getFullYear())
console.log(new Date().getMonth())