// Event - object userni harakatlarini kuzatish va unga mos javob berish obyekti 
// click events 
// onclick - chap tugma bosilganda 
let counter = 0;
// chap tugma 
window.onclick = function(){
    console.log(counter++)
}
// o'ng tugma 
window.oncontextmenu = function(){
    console.log(counter--)
}
// console.dir(window)
// console.dir(document)