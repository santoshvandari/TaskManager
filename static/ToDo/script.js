"use strict";
let preloader= document.querySelector("section.preloader");
(()=>{
    window.addEventListener("load",()=>{
        preloader.style.display='none';
    })
})();