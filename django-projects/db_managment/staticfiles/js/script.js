

function SetArticleRating(rating,article_id){
    let article = document.querySelector("#article_rating")
    let data = JSON.stringify(
        {
            rating:rating,
            article_id:article_id
        }
    )
    let url = `/posts/add/rating/?data=${data}`

    fetch(url) 
    .then(response => response.json())
    .then(data => {
        if(data["status"] == 200){
            article.innerHTML = data["updated_rating"]
        }
        if(data["status"] == 400){
            article.innerHTML = 'You already rated !'
        }
        if(data["status"] == 404){
            article.innerHTML = 'Something went wrong!'
        }
    })

}



document.querySelector("#price").addEventListener("keyup", (e)=>{
    document.querySelector(".slected_price").innerHTML = e.target.value
  })

document.querySelector("#age").addEventListener("change", (e)=>{
    document.querySelector(".slected_age").innerHTML = e.target.value
  })