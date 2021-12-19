//buttons
let menuBtn = document.querySelector(".carding");
let menuButton = document.querySelector(".card-linky");
let menuBtnLink = document.querySelector(".card-linking");

//displayed div
let menuchoice = document.querySelectorAll(".select-choice");
let menuOption = document.querySelector(".select-option");
let menuDecision = document.querySelector(".select-decision");


let menuCard = document.querySelector(".carding");
let mainDiv = document.querySelector(".card-deck")
//let menuLink = document.querySelector(".linky")
let menuStatus = false;


//menuchoice.style.marginLeft ="-900px"
//menuOption.style.marginLeft ="-900px"
//menuDecision.style.marginLeft ="1300px"

function menuToggle(){
    //e.preventDefault();
    if (menuStatus == false){
        menuchoice.style.marginLeft ="300px";
        menuStatus =true;
       
    }
    
   
    /*else if(menuStatus == true){
        menuchoice.style.marginLeft = "-300px";
        menuStatus = false;
    }*/
}


function menuToggling(){
    if (menuStatus == false){
        menuOption.style.marginLeft ="300px";
        //menuOption.style.marginTop ="70%";
        menuStatus =true;
       
    }
    
}



function menuToggled(){
    if (menuStatus == false){
        menuDecision.style.marginLeft ="300px";
        //menuOption.style.marginTop ="70%";
        menuStatus =true;
       
    }
    
}


function disappearCard(){
    mainDiv.style.display ="none";
    mainDiv.style.visibility ="visible";
    menuStatus =true;
}

function ntnClick(e){
    e.preventDefault();
    menuToggle(e);
   // menuTogglling(e);
    disappearCard();
    
}
function ntnClicked(e){
    e.preventDefault();
  
    menuToggling(e);
    disappearCard();
    
}

function ntnClicking(e){
    e.preventDefault();
  
    menuToggled(e);
    disappearCard();
    
}
//menuBtn.onclick = menuToggle;

/*menuBtn.addEventListener("click" ,menuToggle);
menuBtn.addEventListener("click",function(){
    
});*/
menuBtn.onclick = ntnClick;
menuButton.onclick =ntnClicked
menuBtnLink.onclick =ntnClicking





var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 3000,
  autoplay:true,
 
})



var myCarousel = document.querySelector('.slider-two')
var carousel = new bootstrap.Carousel(myCarousel, {
  prevArrow: "site-slider-two .prev",
  prevArrow: "site-slider-two .next",
  slidesToShow:5,
  slidesToScroll:1,
  autoplayspeed:3000,
 
})

//let menu = document.querySelector('#menu-bar');

//let navbar = document.querySelector('.navbar');

//menu.onclick =()=>{
   // menu.classList.toggle('fa-times');
   // navbar.classList.toggle('active')
//}
//window.onscroll=()=>{

 //   menu.classList.remove('fa-times');
 // navbar.classList.remove('active')

//}


let menuQuery = false;

let toggleChoice = function(){
    let getCard = document.querySelectorAll(".card")
    let getChoice = document.querySelector(".select-choice")

    if(menuQuery === false){
        getChoice.style.marginLeft ="300px";
        getChoice.style.visibility = "visible"

        menuQuery =true;

    }
}