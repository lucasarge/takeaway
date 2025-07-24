console.log('This is JS from your About')

var closeBtn = document.getElementsByClassName("closeBtn")[0];
var openBtn = document.getElementsByClassName("openBtn")[0];
var modal = document.getElementById("quicksearch-modal");
var cartModal = document.getElementById("cart-modal");
let addBtns = document.querySelectorAll(".card button");
let plusBtns = document.querySelectorAll(".plus-button");
let minusBtns = document.querySelectorAll(".minus-button");

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

if (openBtn != null) {
    openBtn.onclick = function() {
    modal.style.display = "block";
    openBtn.style.display = "none";
    }
}

if (closeBtn != null) {
    closeBtn.onclick = function() {
    modal.style.display = "none";
    openBtn.style.display = "inline-block";
    }
}


// cartBtn.onclick = function() {
//     if (cartModal.style.display == "block") {
//         cartModal.style.display = "none"
//     } else {
//         cartModal.style.display = "block"
//     }
// }

addBtns.forEach(addBtn=>{
    addBtn.addEventListener("click", addToCart)
})

plusBtns.forEach(plusBtn=>{
    plusBtn.addEventListener("click", addToCart)
})

minusBtns.forEach(minusBtn=>{
    minusBtn.addEventListener("click", removeFromCart)
})

function updatePage() {
    setTimeout(function() {
        location.reload()
    }, 100);
}

function removeFromCart(e){
    let product_id = e.target.value
    let url = "/products/remove_from_cart"
    let data = {id:product_id}
    
    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)    
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })

    .catch(error=>{
        console.log(error)
    })
    
    console.log(product_id)
    updatePage()
}

function addToCart(e){
    let product_id = e.target.value
    let url = "/products/add_to_cart"
    let data = {id:product_id}
    
    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)    
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })

    .catch(error=>{
        console.log(error)
    })
    console.log(product_id)
    updatePage()
}
