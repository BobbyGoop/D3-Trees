window.addEventListener('load', function () {
    openModal(prompt("Пожалуйста, введите имя"))
    //openModal("Хозяин!")
})

// Overlay section
const overlay = document.getElementById('overlay')
const modal = document.getElementById('modal')
const slideshow = document.getElementById('slideshow')

overlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.modal.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

document.getElementById('confirm').addEventListener('click', () => {
    slideshow.classList.add('active')
})
document.querySelectorAll('[data-close-button]').forEach(button => {
    button.addEventListener('click', () => {
        closeModal()
    })
})

function openModal(name) {
    if (modal == null) return
    modal.children[1].innerHTML = `<h1>Здравствуйте, ${name}!</h1>Хотели бы вы посмотреть рекламу наших продуктов?
    Наш сервис специализируется на подборке красивых обоев рабочего стола как для мобильных устройств, так и для
    персональных компьютеров. Мы предлагаем ознакомиться с рейтингом ТОП-5 изображений за прошедшую неделю `
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal() {
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}

// Slideshow section
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");

    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";

}