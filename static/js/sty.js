
menuQuery =false;

let toggleSelects = function(){
    let getNavbar = document.getElementById("nav-links")
    
    var mainContent  = document.getElementById("content");


    if(menuQuery === false){
        getNavbar.style.display ="block";
        mainContent.style.marginTop ="430px";
        menuQuery =true;

    }
    else if(menuQuery === true){
        getNavbar.style.display ="none";
        mainContent.style.marginTop ="30px";
        menuQuery =false;

    }
}


window.onscroll = function() {myFunction()};
            
var header = document.getElementById("head");
var sticky = header.offsetTop;


function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    //$(".head").css({"background-color":"whitesmoke"});
   
  } else {
    header.classList.remove("sticky");
    //$(".head").css({"background-color":"whitesmoke"});
  }
}



