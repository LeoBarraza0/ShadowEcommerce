
const slider = document.querySelector('.photo-slider');
const nextBtn = document.querySelector('.next-btn');


const images = document.querySelectorAll('.photo-slider img');


let currentIndex = 0;


nextBtn.addEventListener('click', () => {
    
    currentIndex++;

    
    if (currentIndex >= images.length) {
        currentIndex = 0;
    }

    
    slider.style.transform = `translateX(-${currentIndex * 315}px)`; 
});

window.onload = function() {
    
    const userName = sessionStorage.getItem("userName");

    
    if (userName) {
        
        const loginButton = document.querySelector(".iniciar-sesion");
        loginButton.textContent = `Hola, ${userName}`;  
        
        const logoutLink = document.createElement("a");
        logoutLink.textContent = "Cerrar sesión";
        logoutLink.href = "#";
        logoutLink.addEventListener("click", function() {
            
            sessionStorage.removeItem("userName");

           
            window.location.href = "/index.html";
        });

       
        loginButton.appendChild(logoutLink);
    }
};