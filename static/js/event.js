

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
     
       redirect_url:"https://www.i-wan-wok.com/payment_confirmation/",
     
       //payment_options:true,
       //  country: "US",
       //meta: {
        //consumer_id:document.getElementById("id").value,
        //consumer_mac: "92a3-912ba-1192a",
      //},
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







// working with the below js





let toggleSelect = function(){
    //let getCard = document.querySelectorAll(".card")
    let getChoice = document.querySelector(".nav-check")
    let getSelect = document.querySelector(".carousel");
    //let getWhat = document.querySelector(".what-do-want")

    if(menuQuery === false){
        //getChoice.style.marginLeft ="300px";
        getSelect.style.visibility = "hidden";
        
       
        //getSelect.style.marginLeft = "-2500px";

        menuQuery =true;

    }
    else if(menuQuery === true){

        getChoice.style.visibility = "hidden";
        getSelect.style.marginLeft = "0px";
        
        menuQuery =false;

    }
}


//login button


/*let loginQueryy = false;

let toggleLoginn= function(){
    
    let getlogin = document.querySelector(".h-100");
    let getButton= document.querySelector(".toggle");
    getlogin.style.visibility = "hidden";
    
    if(loginQuery == false){
     

        getlogin.style.visibility = "visible";
        
        getButton.style.visibility = "hidden";
        loginQuery =true;

    }
   
}

const name = document.querySelector(".confirm");

 function changeColor() {
    name.style.display = "none";
 }*/


 //function changeColor(color) {
   // name.style.color = color;
 //}
/* check button here*/

let menuQy = false;

let toggleCheckBtn = function(){
    let getCheck = document.querySelector(".confirm")
    let getRow = document.querySelector("#ourjob");
   

    if(menuQy === false){
        getcheck.style.display ="none";
        menuQy = true;
        
        //getRow.style.visibility = "hidden";

    }
    else if(menuQy=== true){

        //getCheck.style.visibility = "hidden";
        //getRow.style.marginLeft = "0px";
        getcheck.style.visibility = "visible";
        
        menuQueri =false;

    }
}



const navSlide =()=>{
const menuBtn =document.querySelector('.nav-check');
const navlinks = document.querySelector('.carousel');

menuBtn.addEventListener('click', ()=>{
    navlinks.classList.toggle('.nav-check');
    
});
} 

navSlide();






var menuList =document.getElementById('carouselExampleCaptions');
   menuList.style.display="block";

function toggleMenu(){
    if(menuList.style.display == "block"){
        menuList.style.display = "none";
        //menuList.style.marginTop = "200px";
    }
    else{
        menuList.style.display = "visible";
        
    }
}








/* check button here*/

let menuQueri = false;

let toggleChoices = function(){
    //let getCard = document.querySelectorAll(".card")
    let getChoice = document.querySelector(".nav-check")
    let getRow = document.querySelector(".carousel");
    //let getWhat = document.querySelector(".what-do-want")

    if(menuQueri === false){
        //getRow.style.marginLeft = "-3000px";

        getRow.style.display ="none";
        menuQueri = true;
        //getChoice.style.visibility = "visible"
        
        //getRow.style.visibility = "hidden";

;
        
       
      
       

        menuQueri =true;

    }
    else if(menuQueri === true){

        getChoice.style.visibility = "hidden";
        getRow.style.marginLeft = "0px";
        getRow.style.visibility = "visible";
        
        menuQueri =false;

    }
}


//payment inttegration- flutterwaves




const forms  = document.getElementById("payForm");
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
       //redirect_url:"https://iwanwok.herokuapp.com/payment_confirmation/",
       redirect_url:"https://www.i-wan-wok.com/payment_confirmation/",
        
       //payment_options:true,
       //redirect_url:true,
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







$(document).ready(function() {
    $('.js-example-basic-single').select2();
});



