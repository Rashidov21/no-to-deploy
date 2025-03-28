const toggle = document.querySelector('.sidebar-toggle'); 
const sidebar = document.querySelector('.sidebar');
toggle.addEventListener("click", function(evt){
    sidebar.classList.toggle("off")
    let pos = Number(toggle.style.left.slice(0,2))
    if(pos == 50){
        toggle.style.left = "220px"
    }else{
        toggle.style.left = "50px"
    }

})

for(let i = 0; i < 5; i++){
    const menu = document.querySelector(".menu")
    let li = document.createElement("li")
    li.textContent = i
    li.style.padding = "10px 20px"
    li.style.color= "white"
    menu.appendChild(li)
}