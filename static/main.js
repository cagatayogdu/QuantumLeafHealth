document.querySelector('.upload').addEventListener('click', function() {
    this.classList.add('active-animation');
    setTimeout(() => this.classList.remove('active-animation'), 300); 
});


function navigateTo(page) {
    window.location.href = page;
}

function navigateTo(route) {
    window.location.href = route;
}

function navigateTo(url) {
    window.location.href = url; 
}

const scrollTopButton = document.getElementById("scrollTopButton");

window.onscroll = function () {
    toggleScrollButton();
};

function toggleScrollButton() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        scrollTopButton.style.display = "block"; 
    } else {
        scrollTopButton.style.display = "none";
    }
}

scrollTopButton.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" }); 
});
