from flask import Flask, render_template, request, jsonify
from IPAdressControl import is_valid_ip
import necessary
import logging
from file_predict import FilePredict
from ffmpegDetect import FFMpegDetect
from database import AtlasClient
from datetime import datetime
import base64

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

filePredict = FilePredict()
realTimeDetect = FFMpegDetect()
atlasClient = AtlasClient()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/camFrame')
def camFrame():
    return render_template('camFrame.html')

@app.route('/get_predicted_class', methods=['GET'])
def get_predicted_class():
    detected_class, detected_prob = realTimeDetect.get_predicted_class()
    return jsonify({'predicted_class': detected_class, 'predicted_prob': detected_prob})

@app.route('/camFrame/IPControl', methods=['POST'])
def camFrameController():
    data = request.get_json()
    ip_address = data['value']
    if is_valid_ip(ip_address):
        response = {"success": True}
        necessary.url = ip_address
        camIPAdress = 'http://' + ip_address + ':8080/video'
        client_ip = request.remote_addr
        print(f"[LOG] {client_ip} adresi sisteme giriş yaptı.")
        data = {
            'ip_address': client_ip,
            'accessed_at': datetime.now(),
            'cam_ip_address': camIPAdress
        }
        atlasClient.insert('RealTimeConnect', data)

        print(f"[INFO] {camIPAdress} video Akişi Başlatiliyor...")
        realTimeDetect.url_set(camIPAdress)
        realTimeDetect.config()
        realTimeDetect.start_detect_in_background()
    else:
        response = {"success": False}
    return jsonify(response)

@app.route('/photoFrame', methods=['GET', 'POST'])
def photoFrame():
    return render_template('photoFrame.html')

@app.route('/image_upload', methods=['POST'])
def image_upload():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No selected file'})
    
    classPred, probs = filePredict.imagePredict(filePredict.image_convert(file, flag=True))
    
    file.seek(0)  
    file_base64 = base64.b64encode(file.read()).decode('utf-8')
    
    client_ip = request.remote_addr
    data = {
        'ip_address': client_ip,
        'accessed_at': datetime.now(),
        'filename': file.filename,
        'file_content': file_base64,
        'class_pred': str(classPred),
        'probabilities': str(probs)
    }

    atlasClient.insert('Image', data)
    tedavi, ilac, oneri = atlasClient.get_treatment_by_name('Hastalik', classPred)
    
    print(f"[LOG] {client_ip} sisteme bir görsel yükledi ve veri tabanına kayıt edildi.")
    return jsonify({'success': True, 'message': 'File uploaded successfully',
                     'classPred': str(classPred), 'prob': str(probs),
                     'tedavi': tedavi, 'ilac': ilac, 'oneri': oneri})

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
