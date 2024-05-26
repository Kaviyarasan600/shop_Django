const togglebtn = document.getElementById("togglebtn")
const option1 = document.getElementById('option1')
togglebtn.addEventListener('click', ()=>{
    togglebtn.classList.toggle('btn2')
    option1.classList.toggle('option2')
})


let product_img = document.getElementById('product_img')

let getAllImages = document.querySelectorAll('.img_toggler');
for (var i = 0; i < getAllImages.length; i++) {
(function(x) { 
    getAllImages[x].addEventListener('click', function() {

        product_img.setAttribute('src',(this.getAttribute('src')))
})
    }(i))
}

let size = document.querySelector('.size_s')

let getAllSizes = document.querySelectorAll('.various_size');
for (var i = 0; i < getAllSizes.length; i++) {
(function(x) { 
    getAllSizes[x].addEventListener('click', function() {
        size.innerHTML = this.getAttribute('value')
})
    }(i))
}


const count_increase = document.getElementById('count_increase')
const count_decrease = document.getElementById('count_decrease')
let product_count = document.getElementById('product_count')
const product_quantity = document.getElementById('product_quantity').innerHTML

count_increase.addEventListener('click', function(){
    let productCount = parseInt(product_count.value,10)
    productCount = isNaN(productCount)?0:productCount
    if(productCount < 10 && productCount <product_quantity){
        productCount++;
        product_count.value = productCount
    }
})

count_decrease.addEventListener('click', function(){
    let productCount = parseInt(product_count.value,10)
    productCount = isNaN(productCount)?0:productCount
    if(productCount>1){
        productCount--;
        product_count.value = productCount
    }
})