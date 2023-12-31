let formDiv=document.querySelector(".form-wrapper");
document.getElementById("addtask").addEventListener("click", function () {
    if(formDiv.classList.contains("show")){
        formDiv.classList.remove("show");
        console.log("removed");
    }else{
        formDiv.classList.add("show");
        console.log("showed");
    } 
});