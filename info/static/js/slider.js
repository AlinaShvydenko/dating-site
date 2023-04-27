let slider = document.querySelector(".slider");
let currentSlideNumber = 0;
let isPaused = false;

updateSlide();

function setActiveSlide(slideNumber) {
    let slides = slider.querySelectorAll(".content>a");
    let indicators = slider.querySelectorAll(".indicators>.circle");

    slides.forEach(slide => {
        if (slide.classList.contains('active')) {
            slide.classList.remove('active');
        }
    });

    indicators.forEach(indicator => {
        if (indicator.classList.contains('active')) {
            indicator.classList.remove('active');
        }
    });

    slides[slideNumber].classList.add("active");
    indicators[slideNumber].classList.add("active");
}

function updateSlide() {
    if (!isPaused) {
        setActiveSlide(currentSlideNumber);
        currentSlideNumber = (currentSlideNumber + 1) % 3;
    }

    setTimeout(updateSlide, 3000);
}

slider.querySelector(".content").addEventListener("mouseover", event => {
    isPaused = true;
});

slider.querySelector(".content").addEventListener("mouseout", event => {
    isPaused = false;
});