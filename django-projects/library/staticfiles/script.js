let username = document.querySelector('#id_username')
let password = document.querySelector('#id_password')
let password1 = document.querySelector('#id_password1')
let password2 = document.querySelector('#id_password2')
let lst = document.querySelector('#id_last_name')
let fst = document.querySelector('#id_first_name')
let inputs = [username, password, password1, password2, lst, fst]

for (item of inputs) {
    if (item) {
        item.classList.add("form-control")
    }
}