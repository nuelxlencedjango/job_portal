
let menuQuery = false;

let toggleChoice = function(){
    //let getCard = document.querySelectorAll(".card")
    let getChoice = document.querySelector(".select-choice")
    let getRow = document.querySelector(".conted");
    let getWhat = document.querySelector(".what-do-want")

    if(menuQuery === false){
        //getRow.style.marginLeft = "-3000px";

        getChoice.style.marginLeft ="300px";
        getChoice.style.visibility = "visible"
        
        getRow.style.visibility = "hidden";

    
        menuQuery =true;

    }
    else if(menuQuery === true){

        getChoice.style.visibility = "hidden";
        getRow.style.marginLeft = "0px";
        getRow.style.visibility = "visible";
        
        menuQuery =false;

    }
}


let toggleSelected = function(){
    //let getCard = document.querySelectorAll(".card")
    let getChoice = document.querySelector(".select-choice")
    let getSelect = document.querySelector(".cont");
    //let getWhat = document.querySelector(".what-do-want")

    if(menuQuery === false){
        getChoice.style.marginLeft ="300px";
        getChoice.style.visibility = "visible";
        
       
        getSelect.style.marginLeft = "-2500px";

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