# Quantum Leaf Health

## Project Description

**Quantum Leaf Health**, is a quantum deep learning based leaf disease detection and treatment recommendation system. While traditional methods are slow and have a high margin of error, a faster and more accurate diagnosis process is provided by using quantum computing techniques and deep learning.

This project uses real-time images from an IP Webcam to detect plant diseases, transfers them to a Flask-based server, and then analyzes them using a quantum deep learning model. The results provide treatment recommendations to increase agricultural productivity.

## Features
- **Real-time disease detection**: Images taken from the IP camera are analyzed instantly to diagnose the disease.
- **Quantum deep learning model**: Provides a more optimized and faster analysis process compared to traditional deep learning models.
- **Web-based interface**: Users can view disease detection and recommendations thanks to the interface developed with Flask.
- **MongoDB database integration**: Disease history and analysis results can be stored.
- **Real-time ffmpeg integration**: Images taken from the IP camera are quickly processed using ffmpeg and transferred to the system.

## Technologies Used
- **Backend**: Flask, WSGI, Waitress
- **Frontend**: JavaScript
- **Database**: MongoDB
- **Machine Learning & Quantum Computing**:
  - PennyLane
  - Torch
  - NumPy
  - base64
- **Other**:
  - IP Webcam
  - ffmpeg (For real-time image processing)

## Installation
1. Install the required dependencies:
    ```bash
    pip install flask torch pennylane numpy pymongo ffmpeg-python waitress
    ```
2. Start the server:
    ```bash
    python app.py
    ```
3. You can use the interface by going to `http://localhost:5000` in your web browser.

## Project Structure
```
QuantumLeafHealth/
│── app.py                          # Flask-based server
│── model/                          # Quantum and classical learning models
│── static/                         # Web interface static files
│── templates/                      # HTML templates
│── requirements.txt                # Dependency list
│── DatasetPreparationCode.ipynb    # Code for data augmentation and creation of general dataset
│── README.md                       # Project description
```

## Working Principle
1. The user uploads the image of the plant leaf to the system via IP Webcam.
2. The Flask-based backend processes the image using ffmpeg and transmits it to the quantum deep learning model.
3. The model detects the presence of the disease and offers possible diagnosis and treatment suggestions.
4. The results are saved to the MongoDB database and displayed to the user.

## Model Performance

The performance of the quantum deep learning model was evaluated using a dataset of plant leaf images. Below are the key metrics and visualizations that summarize the model's performance:

### Balanced vs. Imbalanced Dataset
Here, you can compare the effects of a balanced and an imbalanced dataset on model performance.
<p align="center">
  <img src="https://github.com/user-attachments/assets/324cd07a-161f-4f5c-b67e-183731060741" width="800"/>
  <img src="https://github.com/user-attachments/assets/9b715240-e16b-4e32-8f7f-afa9f222fe4a" width="800"/>
</p>

### Training Curve
The training curve demonstrates the loss and accuracy of the model over time, showing how the model learned during the training process.  
<p align="center">
  <img src="https://github.com/user-attachments/assets/8eca0976-d1b2-432c-95c7-d5f4aec89fcd" width="800"/>
</p>

### Confusion Matrix
The confusion matrix provides a clear picture of the classification performance of the model. It shows the true positive, true negative, false positive, and false negative results.
<p align="center">
  <img src="https://github.com/user-attachments/assets/174f5a7c-8341-45b8-8491-fb4f6ad27a8f" width="800"/>
</p>

### ROC Curve
The ROC (Receiver Operating Characteristic) curve shows the trade-off between the true positive rate and false positive rate, providing insight into the model's ability to discriminate between classes.  
<p align="center">
  <img src="https://github.com/user-attachments/assets/39e23987-b6fd-428f-9fcc-23e3e9098555" width="800"/>
</p>

These metrics collectively highlight the effectiveness of the quantum deep learning model in diagnosing plant diseases and provide further insights into areas for improvement.

### Some Images From The Project
<p align="center">
  <img src="https://github.com/user-attachments/assets/b6ab2bcc-5531-4cb5-94d3-5307310f728f" width="400"/>
  <img src="https://github.com/user-attachments/assets/edf53421-e4c2-485a-99ad-1f7e3704d77f" width="400"/>
  <img src="https://github.com/user-attachments/assets/7642e1e6-7ea5-4d9a-9d5f-fbfec95fa5aa" width="400"/>
  <img src="https://github.com/user-attachments/assets/3ccde689-14c9-49c9-b29d-bff0b74eb1f5" width="400"/>
</p>

## Conclusion and Recommendations
This project demonstrates how quantum computing techniques can be integrated into agricultural disease diagnosis. The process has been accelerated thanks to real-time data processing and ffmpeg integration. In the future, it is planned to integrate lower cost IoT solutions and extend the model to different plant species.

