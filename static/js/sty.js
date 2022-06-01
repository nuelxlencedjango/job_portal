
menuQuery =false;

let toggleSelects = function(){
    let getNavbar = document.getElementById("nav-links")
    let getSelect = document.getElementsByTagName("li")
    var mainContent  = document.getElementById("content");


    if(menuQuery === false){
        getNavbar.style.display ="block";
        mainContent.style.marginTop ="380px";
        //getSelect.style.transition = "all 0.3s ease-in";
        menuQuery =true;

    }
    else if(menuQuery === true){
        getNavbar.style.display ="none";
        mainContent.style.marginTop ="30px";
        menuQuery =false;

    }
}






