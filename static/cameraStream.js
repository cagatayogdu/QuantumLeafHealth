var streamUrl = '';
var flag = false;
const imgElement = document.getElementById('cameraStream');
const outButton = document.getElementById('outButton');
const ipInput = document.getElementById('ipInput');
const submitIpButton = document.getElementById('submitIpButton');
const result = document.getElementById('disease-result');

function fetchMJPEGStream() {
    const img = new Image();
    img.src = streamUrl;
    img.onload = function() {
        imgElement.src = img.src;
    };
}
setInterval(fetchMJPEGStream, 100);
setInterval(fetchPredictedClass, 500);

submitIpButton.addEventListener('click', async function () {
    const ipAddress = ipInput.value;
    const data = { value: ipAddress };
    
    try {
        const response = await fetch('/camFrame/IPControl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const responseData = await response.json();
        if (responseData.success === true) {
            streamUrl = 'http://' + ipAddress +':8080/video';   
            flag = true;   
        } else {
            alert('Invalid IP address. Please enter a valid address.');
        }
    } catch (error) {
        console.error('Error occurred:', error);
    }
});

outButton.addEventListener('click', function () {
    console.log('Button clicked! Redirecting to localhost:8080');
    streamUrl = '';
    window.location.href = '/';
});

function fetchPredictedClass() {
    if(flag){
        fetch('/get_predicted_class')
            .then(response => response.json())
            .then(data => {
                result.textContent = data.predicted_class;
            })
            .catch(error => {
                console.error("Hata:", error);
                result.textContent = "Hata oluştu, görüntü alınamamış olabilir.";
            });
    }
}
