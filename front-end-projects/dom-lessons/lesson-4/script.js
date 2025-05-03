// Event - object userni harakatlarini kuzatish va unga mos javob berish obyekti 
// click events 
// onclick - chap tugma bosilganda 
// let counter = 0;
// chap tugma 
// window.onclick = function(){
//     console.log(counter++)
// }
// o'ng tugma 
// window.oncontextmenu = function(){
//     console.log(counter--)
// }
// console.dir(window)
// console.dir(document)
// let box = document.querySelector(".box");
// console.dir(box)
// kursor ustiga kelganda
// box.onmouseover = function(){
//     box.style.width = "150px"
// }
// kursor ustidan ketganda
// box.onmouseout = function(){
//     box.style.width = "100px"
// }
// chap tugmani bosib turgan vaqtda 
// box.onmousedown = function(){
//     box.style.background = "khaki"
// }
// chap tugmani qoyib yuborgandan so'ng
// box.onmouseup = function(){
//     box.style.background = "blueviolet"
// }
// dragstart 
// dragover
// drop 
// let tasks = [
//     {id:1,name:"Nonushta"},
//     {id:2,name:"Trenerovka"},
//     {id:3,name:"Dars qilish"},
// ]
// localStorage.setItem("tasks",JSON.stringify(tasks))
// console.log(localStorage.getItem("tasks"))

window.onload = () =>{
    tasks = JSON.parse(localStorage.getItem("tasks"))
    let todos = document.querySelector("#todo");
    tasks.forEach((task)=>{
        let divTask = document.createElement("div");
        let deleteBtn = document.createElement("button")
        deleteBtn.setAttribute("onclick",`deleteTask('${task.name}')`)
        deleteBtn.innerHTML = "O'chirish"
        divTask.setAttribute("draggable","true")
        divTask.classList.add("item")
        divTask.innerHTML = task.name
        divTask.appendChild(deleteBtn)
        todos.appendChild(divTask)
    })

    const items = document.querySelectorAll(".item");
    const columns = document.querySelectorAll(".column");

    let draggedItem = null;

    items.forEach(item => {
        item.addEventListener("dragstart", () =>{
            draggedItem = item;
            item.classList.add("dragging")
        })
        item.addEventListener("dragend", () =>{
            draggedItem = null;
            item.classList.remove("dragging")
        })
    })

    columns.forEach( column =>{
        column.addEventListener("dragover", (e)=>{
            e.preventDefault();
        })
        column.addEventListener("drop", ()=>{
            if(draggedItem){
                column.appendChild(draggedItem)
            }
        })
    });
}
function addTask(){
    let name = document.querySelector('#taskName').value
    tasks = JSON.parse(localStorage.getItem("tasks"))
    tasks.push(
        {name:name}
    )
    localStorage.setItem("tasks",JSON.stringify(tasks))
    window.location.reload()
};
function deleteTask(name){
    tasks = JSON.parse(localStorage.getItem("tasks"))
    tasks.forEach(item =>{
        if(item.name == name){
            let index = tasks.indexOf(item)
            tasks.splice(index,1)
        }
    })
    localStorage.setItem("tasks",JSON.stringify(tasks))
    window.location.reload()
};

function clearTasks(){
    tasks = JSON.parse(localStorage.getItem("tasks"))
    tasks = []
    localStorage.setItem("tasks",JSON.stringify(tasks))
    window.location.reload()
}