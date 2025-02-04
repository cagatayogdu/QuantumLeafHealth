import ffmpeg
import numpy as np
import time
from file_predict import FilePredict
from threading import Thread
from PIL import Image

class FFMpegDetect():
    def __init__(self):
        self.predictor = FilePredict()
        self.prob = 0
        self.center_size = 300 

    def url_set(self, url):
        self.url = url
    
    def config(self):
        self.process = (
            ffmpeg
            .input(self.url, fflags='nobuffer', vsync='passthrough')
            .output('pipe:', format='rawvideo', pix_fmt='rgb24', s='640x600')
            .run_async(pipe_stdout=True, pipe_stderr=True, quiet=True)
        )
    
    def detect(self):
        time.sleep(1)
        #start_time = time.time()
        #last_time = start_time

        try:
            while True:
                frame_bytes = self.process.stdout.read(640 * 600 * 3)
                if not frame_bytes:
                    print("[INFO] Kare alınamadı, çıkılıyor.")
                    break

                frame = np.frombuffer(frame_bytes, np.uint8).reshape((600, 640, 3))
                cropping = self.cropFrame(frame)

                #current_time = time.time()
                #fps = 1.0 / (current_time - last_time)
                #last_time = current_time
                #print(f"FPS: {fps:.2f}")
                
                inputTensorBatch = self.predictor.image_convert(cropping)
                predicted_class, prob = self.predictor.imagePredict(inputTensorBatch)

                if prob > 0.6:
                    self.predicted_class = predicted_class
                    self.prob = prob
                    print(f"[SYSTEM] Tespit Edilen Sınıf: {predicted_class}, Olasılık: %{100*prob:.3f}")

                time.sleep(0.05)

        except KeyboardInterrupt:
            print("[INFO] Kullanıcı tarafından durduruldu.")
        finally:
            print("[INFO] Durdu")
            self.process.terminate()
            
    def cropFrame(self, frame):
        h, w, _ = frame.shape
        top = (h - self.center_size) // 2
        left = (w - self.center_size) // 2
        center_crop = frame[top:top + self.center_size, left:left + self.center_size]
        return center_crop


    def get_predicted_class(self):
        if self.prob > 0.01:
            return self.predicted_class, self.prob
        else:
            return None, 0
    
    def start_detect_in_background(self):
        detection_thread = Thread(target=self.detect)
        detection_thread.daemon = True
        detection_thread.start()