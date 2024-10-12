const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const carouselContainer = document.querySelector(".carousel-container");
const slides = document.querySelectorAll(".carousel-slide img");
let counter = 0;
const size = slides[0].clientWidth;

carouselContainer.style.transform = `translateX(${-size * counter}px)`;

// Função para mover o carrossel para a esquerda
nextBtn.addEventListener("click", () => {
    if (counter >= slides.length - 1) return;
    carouselContainer.style.transition = "transform 0.4s ease-in-out";
    counter++;
    carouselContainer.style.transform = `translateX(${-size * counter}px)`;
});

// Função para mover o carrossel para a direita
prevBtn.addEventListener("click", () => {
    if (counter <= 0) return;
    carouselContainer.style.transition = "transform 0.4s ease-in-out";
    counter--;
    carouselContainer.style.transform = `translateX(${-size * counter}px)`;
});
