let months = document.querySelector(".calendar--months");
let days = document.querySelector(".calendar--days");
let monthsList = document.querySelector(".months");
let daysList = document.querySelector(".days");

days.addEventListener("click", ()=>{
    days.classList.toggle("days_active");
    months.classList.toggle("months_active");
    monthsList.classList.toggle("months_list_active");
    daysList.classList.toggle("days_list_active");
})
months.addEventListener("click", ()=>{
    days.classList.toggle("days_active");
    months.classList.toggle("months_active");
    monthsList.classList.toggle("months_list_active");
    daysList.classList.toggle("days_list_active");
})