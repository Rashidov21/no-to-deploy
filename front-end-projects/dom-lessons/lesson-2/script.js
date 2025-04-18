let div = document.querySelector("#div")
console.dir(div);
// class 
// console.log(div.classList)
// div.classList.add() // yangi class qoshish
// div.classList.remove() // class ochirish
// div.classList.contains() // siz bergan className ni tekshiradi agar u bolsa true qaytaradi aks holda false
// if(div.classList.contains("red")){
//     alert("OK")
// }
// div.classList.toggle() // siz bergan className ni qoshib/ochiradi 
// div.onclick = ()=>{
//     div.classList.add("red")
// }
// attribute

// let img = document.querySelector("img")
// console.log(img.getAttribute("src"));
// img.setAttribute("title","Test image");
// // console.log(img.hasAttribute("disabled"))

// img.removeAttribute("title")
// console.log(img.hasAttribute("title"))
// getAttribute - atributini olish 
// setAttribute - atribut qoshish
// hasAttribute - tekshirish 
// removeAttribute - ochirish 



// let span = document.querySelector("span")
// console.log(span);
// let a = document.querySelector("a")
// console.log(a);

let animals = [
    {
        name:"lion",
        url:"https://en.wikipedia.org/wiki/Lion",
        image:"https://avatars.mds.yandex.net/i?id=208f1c0b91d79efa35d1f06afdf3178b_l-11543319-images-thumbs&n=13"
    },
    {
        name:"panda",
        url:"https://en.wikipedia.org/wiki/Giant_panda",
        image:'https://oboi-elysium.ru/upload/iblock/49c/panda-c-371-3-0kh2-38-m.jpg'
    },
    {
        name:"eagle",
        url:"https://en.wikipedia.org/wiki/Eagle",
        image:"https://s3.tradingview.com/userpics/51586631-snfS_orig.png"
    }
]

function setAnimalInfo(animalName){
    let info = document.querySelector("#animalInfo")
    let image = document.querySelector("#animalImage")
    animals.forEach(el =>{
        if(el.name == animalName){
            info.setAttribute("href",el.url)
            image.setAttribute("src",el.image)
        }
    })
}