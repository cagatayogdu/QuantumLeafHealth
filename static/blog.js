document.addEventListener("DOMContentLoaded", () => {
        const buttons = document.querySelectorAll('.read-more');
        
        buttons.forEach(function(button) {
            button.addEventListener('click', function() {
                // Butonun bulunduğu div'in full-text bölümünü göster
                const fullText = button.previousElementSibling;
                fullText.style.display = (fullText.style.display === 'none' || fullText.style.display === '') ? 'block' : 'none';
                
                // Buton metnini değiştirebiliriz
                button.textContent = fullText.style.display === 'block' ? 'Gizle' : 'Devamını Oku';
            });
        });
    });
