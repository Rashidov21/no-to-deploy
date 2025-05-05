let box = document.getElementById("box")
let top = 0;
let left = 0;

window.addEventListener("keydown", (evt) => {
    if (evt.key == "ArrowUp") {
        top -= 10;
        box.style.top = `${top}px`;
    }
    if (evt.key == "ArrowDown") {
        top += 10;
        box.style.top = `${top}px`;
    }
    if (evt.key == "ArrowRight") {
        left += 10;
        box.style.left = `${left}px`;
    }
    if (evt.key == "ArrowLeft") {
        left -= 10;
        box.style.left = `${left}px`;
    }
});
