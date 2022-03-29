// api >> 8fbfbadfa5da4acd8237984c8e26cf4b
let url = "https://newsapi.org/v2/everything?q=keyword&apiKey=8fbfbadfa5da4acd8237984c8e26cf4b";

// author: "David Ogletree"
// content: "Negative keywords are the backbone of any PPC strategy. Ever since Google all but eliminated the ability to specifically target keywords by expanding phrase match to include broad match traffic, nega… [+5420 chars]"
// description: "Want to dramatically reduce the number of negative keywords you need to maintain? Save time and money with this method.\n\nPlease visit Search Engine Land for the full article."
// publishedAt: "2022-03-15T06:00:00Z"
// source: { id: null, name: 'Search Engine Land' }
// title: "Save time on negative keywords using the lowest common denominator method"
// url: "https://searchengineland.com/negative-keywords-lowest-common-denominator-method-382296"
// urlToImage: "http


function render(data) {
    let postsDiv = document.querySelector(".posts")
    for (let news of data) {
        console.log(news)
        let card = document.createElement("div").classList.add("card")
        let post = `
        <div class="card" style="width: 50%;">
        <img src="${news.urlToImage}" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">${news.title}</h5>
          <p class="card-text">${news.description}</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
        `
        postsDiv.insertAdjacentElement("afterbegin", post)
    }
}

function getNews() {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);

    xhr.addEventListener('load', () => {
        render(JSON.parse(xhr.responseText).articles)
    })


    xhr.addEventListener('error', () => {
        console.log("error")
    })

    xhr.send();
}
getNews()