const canvas = document.querySelector("#canv");
const context = canvas.getContext("2d")

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

context.fillStyle = 'orange';
// context.fillRect(50, 50, 300, 300);
context.arc(canvas.width / 2, canvas.height / 2, 100, 0, Math.PI);
context.fillStyle()