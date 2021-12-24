
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

let menuQuery = false;

let toggleChoice = function(){
    //let getCard = document.querySelectorAll(".card")
    let getChoice = document.querySelector(".nav-check")
    let getRow = document.querySelector(".carousel");
    //let getWhat = document.querySelector(".what-do-want")

    if(menuQuery === false){
        //getRow.style.marginLeft = "-3000px";

        getRow.style.display ="none";
        menuQuery = true;
        //getChoice.style.visibility = "visible"
        
        //getRow.style.visibility = "hidden";

;
        
       
      
       

        menuQuery =true;

    }
    else if(menuQuery === true){

        getChoice.style.visibility = "hidden";
        getRow.style.marginLeft = "0px";
        getRow.style.visibility = "visible";
        
        menuQuery =false;

    }
}

menuQuery =false;

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


let loginQuery = false;

let toggleLogin= function(){
    
    let getlogin = document.querySelector(".h-100");
    let getButton= document.querySelector(".toggle");
    getlogin.style.visibility = "hidden";
    
    if(loginQuery == false){
     

        getlogin.style.visibility = "visible";
        
        getButton.style.visibility = "hidden";
        loginQuery =true;

    }
   
}