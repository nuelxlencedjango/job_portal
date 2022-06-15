

let menuInfo = false;
let main_menu = document.getElementById("menu");
let mainRow  = document.getElementById("overall");


function checkToggle(){
if(menuInfo===false){

    main_menu.style.display = "block";
    mainRow.style.marginTop ="400px";
   
    menuInfo =true;
}
else{
    main_menu.style.display = "none";
    mainRow.style.marginTop ="30px";
    menuInfo =false;

}
}



/*window.onscroll = function() {myFunction()};
            
var header = document.getElementById("menu");
var sticky = header.offsetTop;
function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    $(".header").css({"background-color":"whitesmoke"});
   
  } else {
    header.classList.remove("sticky");
    $(".header").css({"background-color":"whitesmoke"});
  }
}*/