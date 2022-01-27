

/*var updateBtns =document.getElementsByClassName('update-cart')
for(i =0;i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action  = this.dataset.action
        console.log('productId:' ,productId,'Action:', action)

        console.log('USER:',user)
        if(user === "AnonymousUser"){
            console.log('user is not authenticated')
        }
        else{
            console.log('user is authenticated:',user)
            updateUserOrder(productId ,action)
        }
    })
}



function updateUserOrder(productId, action){
    console.log('User is logged in');

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken, 
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
        location.reload()
        
    })
   
}*/


const form  = document.getElementById("payForm");
form.addEventListener("submit", payNow);


function payNow(e){
    //prevent normal form submission
    e.preventDefault();
    
    // set configurations
    FlutterwaveCheckout({
       public_key:"FLWPUBK_TEST-6941e4117be9902646d54ec0509e804c-X",
       tx_ref: "iwanwok_" +Math.floor((Math.random()*1000000000)+1),
       amount: document.getElementById("amount").value,
       currency:"NGN",
       redirect_url:"https://iwanwok.herokuapp.com/payment_confirmation/",
     
       //payment_options:true,
       //  country: "US",
       meta: {
        consumer_id:document.getElementById("id").value,
        //consumer_mac: "92a3-912ba-1192a",
      },
       customer:{
           email: document.getElementById("email").value,
           phone_number:document.getElementById("phoneNumber").value,
           name:document.getElementById("fullname").value,
       },
       callback:function(data){
           const reference = data.tx_ref;
           alert("Payment was successfully completed!" + reference);
           //console.log(data);
       },
       customizations: {
        title: "Iwan_wok",
        description: "Payment for the services requested"
        //logo: "https://assets.piedpiper.com/logo.png",
      },
       //customizations:true
    });
}







