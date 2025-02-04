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
│── app.py              # Flask-based server
│── models/             # Quantum and classical learning models
│── static/             # Web interface static files
│── templates/          # HTML templates
│── requirements.txt    # Dependency list
│── README.md           # Project description
```

## Working Principle
1. The user uploads the image of the plant leaf to the system via IP Webcam.
2. The Flask-based backend processes the image using ffmpeg and transmits it to the quantum deep learning model.
3. The model detects the presence of the disease and offers possible diagnosis and treatment suggestions.
4. The results are saved to the MongoDB database and displayed to the user.

## Conclusion and Recommendations
This project demonstrates how quantum computing techniques can be integrated into agricultural disease diagnosis. The process has been accelerated thanks to real-time data processing and ffmpeg integration. In the future, it is planned to integrate lower cost IoT solutions and extend the model to different plant species.

