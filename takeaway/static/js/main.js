console.log('This is JS from your About')

var closeBtn = document.getElementsByClassName("closeBtn")[0];
var openBtn = document.getElementsByClassName("openBtn")[0];
var modal = document.getElementById("quicksearch-modal");
var cartBtn = document.getElementById("cartBtn");
var cartModal = document.getElementById("cart-modal");

openBtn.onclick = function() {
    modal.style.display = "block";
    openBtn.style.display = "none";
}

closeBtn.onclick = function() {
    modal.style.display = "none";
    openBtn.style.display = "inline-block";
}

cartBtn.onclick = function() {
    if (cartModal.style.display == "block") {
        cartModal.style.display = "none"
    } else {
        cartModal.style.display = "block"
    }
}