// let form = document.forms

// console.log(document.forms)
// console.log(document.forms[0])
// console.log(document.forms[1])
// console.log(document.forms[1].children[0].children[0])

// const form = document.getElementById("form1")
// form.addEventListener("change", (e)=>{
//     e.preventDefault();
//     console.log(form.elements[0].value)
//     console.log(form.elements[1].value)

// })
// let name = document.querySelector("#fname")
// console.log(name.value)
// name.setAttribute("class","form-control")
// name.removeAttribute("required")


let searchForm = document.querySelector("#search")
let result = document.querySelector(".result")
searchForm.addEventListener("keydown", (e)=>{
    let query = e.target.value
    if(query.length >= 3){
        fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => response.json())
        .then(data => {
            data.forEach(user=>{
                if(user.name.includes(query)){
                    let li = document.createElement("li")
                    li.innerHTML = user.name
                    result.appendChild(li)
                }else{
                    // result.innerHTML = "";
                }
            })
        })
    }
})


