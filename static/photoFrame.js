function customPreviewImage(input) {
    const previewBox = document.getElementById('preview-box');
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            previewBox.innerHTML = `<img src="${e.target.result}" alt="Yüklenen Resim">`;
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        previewBox.innerHTML = '<p>Henüz bir resim seçilmedi.</p>';
    }
}

const fileInput = document.getElementById('file-upload');
const uploadButton = document.getElementById('upload-btn');
const responseBox = document.getElementById('response-box');
const diseaseResult = document.getElementById('disease-result');
const treatmentResult = document.getElementById('treatment-result');
const medicineResult = document.getElementById('medicine-result');
const suggestionResult = document.getElementById('suggestion-result');

uploadButton.addEventListener('click', async function () {
    const file = fileInput.files[0];
    if (!file) {
        alert("Lütfen bir dosya seçin.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/image_upload', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (data.success) {
            diseaseResult.textContent = `Tespit Edilen Hastalık: ${data.classPred}, %${(100 * data.prob).toFixed(3)} olarak tespit edildi.`;
            treatmentResult.textContent = data.tedavi ? `Tedavi: ${data.tedavi}` : "";
            medicineResult.textContent = data.ilac ? `İlaç: ${data.ilac}` : "";
            suggestionResult.textContent = data.oneri ? `Öneriler: ${data.oneri}` : "";    

            responseBox.style.display = 'block';
        } else {
            alert("Bir hata oluştu.");
            diseaseResult.textContent = "Hastalık tespit edilemedi.";
            responseBox.style.display = 'block';
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Bir hata oluştu.');
        diseaseResult.textContent = "Sunucuyla bağlantı kurulamadı.";
        responseBox.style.display = 'block';
    }
});

fileInput.addEventListener('change', function() {
    customPreviewImage(this);
});
