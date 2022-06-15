

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


$(document).ready(function(){
  if ($('.owl-carousel').length){
  $('.owl-carousel').owlCarousel({
      loop:true,
      //margin:10,
      nav:true,

     // autoplayTimeout: 2000,
      autoplay:true,
  //autoplayTimeout:10000,
  //autoPlayHoverPause:false,
      //animateOut: 'slideOutDown',
      //animateIn: 'flipInX',
      responsiveClass:true,
      responsive:{
          0:{
              items:1,
              
          },
       
          600:{
              items:2,
             
          },
          900:{
              items:3,

          },
          1000:{
              items:4,
             
              loop:true,
          }
      }
  })
}
})

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