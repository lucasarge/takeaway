console.log('This is JS from your About')

var closeBtn = document.getElementsByClassName("closeBtn")[0];
var openBtn = document.getElementsByClassName("openBtn")[0];
var modal = document.getElementById("quicksearch-modal");
var cartBtn = document.getElementById("cartBtn");
var cartModal = document.getElementById("cart-modal");
let addBtns = document.querySelectorAll(".card button")

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

openBtn.onclick = function() {
    modal.style.display = "block";
    openBtn.style.display = "none";
}

closeBtn.onclick = function() {
    modal.style.display = "none";
    openBtn.style.display = "inline-block";
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
}
