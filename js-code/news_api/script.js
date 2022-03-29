// api >> 8fbfbadfa5da4acd8237984c8e26cf4b
let url = "https://newsapi.org/v2/everything?q=keyword&apiKey=8fbfbadfa5da4acd8237984c8e26cf4b";

function getNews() {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.addEventListener('load', () => {
        console.log(xhr.responseText)
    })

    xhr.addEventListener('error', () => {
        console.log("error")
    })

    xhr.send();
}