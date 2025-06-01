console.log('This is JS from your About')

var closeBtn = document.getElementsByClassName("closeBtn")[0];
var openBtn = document.getElementsByClassName("openBtn")[0];
var modal = document.getElementById("quicksearch-modal");

console.log("test")

openBtn.onclick = function() {
    modal.style.display = "block";
    openBtn.style.display = "none";
}

closeBtn.onclick = function() {
    modal.style.display = "none";
    openBtn.style.display = "inline-block";
}