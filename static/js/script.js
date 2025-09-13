let lastScrollTop = 0;
const header = document.querySelector('.myheader');

window.addEventListener("scroll", function() {
let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

if (currentScroll > lastScrollTop) {
    // scrolling down → hide header
    header.style.top = "-100px"; 
} else {
    // scrolling up → show header
    header.style.top = "0";
}

lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // avoid negative scroll
}, false);

// image zoom out effect
document.querySelectorAll('.portfolio-img').forEach(img => {
  img.addEventListener('click', function () {
    const src = this.getAttribute('data-img');
    const modalImage = document.getElementById('modalImage');
    modalImage.setAttribute('src', src);
  });
});
