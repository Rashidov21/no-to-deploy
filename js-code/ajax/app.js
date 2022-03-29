function getUsers() {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "https://jsonplaceholder.typicode.com/users");
    xhr.addEventListener('load', () => {
        console.log(xhr.responseText)
    })

    xhr.addEventListener('error', () => {
        console.log("error")
    })

    xhr.send();
}