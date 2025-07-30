console.log('Hello World')

// This Django function helps with authenticity, it collects cookie when called.
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// This function is used to show error message and have it fade after 3 seconds.
function showError(message) {
    const errorDiv = document.getElementById("error-notification");
    if (errorDiv) {
        errorDiv.innerHTML = message;
        errorDiv.classList.remove("hidden")
        setTimeout(() => {
            errorDiv.classList.add("hidden")
        }, 3000);
    }
}

// This portion is to open and close quicksearch-modal for better heuristics.
var modal = document.getElementById("quicksearch-modal");

var openBtn = document.getElementsByClassName("openBtn")[0];
if (openBtn != null) {
    openBtn.onclick = function() {
    modal.style.display = "block";
    openBtn.style.display = "none";
    }
}

var closeBtn = document.getElementsByClassName("closeBtn")[0];
if (closeBtn != null) {
    closeBtn.onclick = function() {
    modal.style.display = "none";
    openBtn.style.display = "inline-block";
    }
}

// This reloads the page after 0.1 second when called to update not JS portions.
function updatePage() {
    setTimeout(function() {
        location.reload()
    }, 100);
}

// This isn't a feature now but will be implemented in the future.
// var cartModal = document.getElementById("cart-modal");
// cartBtn.onclick = function() {
//     if (cartModal.style.display == "block") {
//         cartModal.style.display = "none"
//     } else {
//         cartModal.style.display = "block"
//     }
// }

// This updates the page with JS preventing the page needing to reload.
let quantityDisplay = document.getElementById("quantity-display")
let quantity = 1;

// This adds 1 from quantity in a multiple purchase on the product info page.
let pplusBtn = document.getElementById("pplus")
if (pplusBtn) {
    pplusBtn.addEventListener("click", () => {
        quantity++;
        quantityDisplay.textContent = quantity;
    });
}

// This removes 1 from quantity in a multiple purchase on the product info page.
let pminusBtn = document.getElementById("pminus")
if (pminusBtn) {
    pminusBtn.addEventListener("click", () => {
        if (quantity > 1) {
            quantity--;
            quantityDisplay.textContent = quantity;
        }
    });
}

// This collects all minus buttons in cart.html and removes 1 item on click.
let minusBtns = document.querySelectorAll("#minus");
minusBtns.forEach(minusBtn=>{
    minusBtn.addEventListener("click", removeFromCart)
});

// On click of minusBtn this function gets used, removing one item from cart.
function removeFromCart(e){
    let product_id = e.target.value
    let url = "/products/remove_from_cart"
    let data = {id:product_id}
    // This sends data back to the server which will then update it for user.
    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)    
    })
    .then(res=>res.json().then(data => ({ status: res.status, body:data})))
    .then(({ status, body }) => {
        // This if statement helps display errors and update page relatively.
        if (status=401 && body.error) {
            showError(body.error);
        } else {
            console.log(body);
            updatePage();
        }
    })
    .catch(error=>{
        console.log(error)
    })
}

// This collects all plus/add buttons in cart.html and adds 1 item on click.
let plusBtns = document.querySelectorAll("#add,#plus");
plusBtns.forEach(plusBtn=>{
    plusBtn.addEventListener("click", addToCart)
});

// On click of plusBtn this function gets used, adding one item from cart.
function addToCart(e){
    let product_id = e.target.value
    let url = "/products/add_to_cart"
    let data = {id:product_id, quantity:quantity}
    // This sends data back to the server which will then update it for user.
    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)    
    })
    .then(res=>res.json().then(data => ({ status: res.status, body:data})))
    .then(({ status, body }) => {
        // This if statement helps display errors and update page relatively.
        if (status=401 && body.error) {
            showError(body.error);
        } else {
            console.log(body);
            updatePage();
        }
    })
    .catch(error=>{
        console.log(error)
    })  
}