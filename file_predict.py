import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from model import Net
from necessary import classes, modelPath

class FilePredict():
    def __init__(self):
        self.model = Net()
        print (f"[SYSTEM] Model ince ayarları yapıldı, RAM'e dahil edildi.")
        self.model.load_state_dict(torch.load(modelPath,weights_only=True))
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"[SYSTEM] Cuda bağlantısı aktif edildi.")
        self.transform = transforms.Compose([
            transforms.Resize((64, 64)), 
            transforms.ToTensor(),    
        ])
        
    def image_convert(self, file, flag = False):
        if flag:
            img = Image.open(file)
        else:
            img = Image.fromarray(file)
            
        inputTensorBatch = self.transform(img).unsqueeze(0) 
        inputTensorBatch = inputTensorBatch.repeat(4, 1, 1, 1) 
        return inputTensorBatch
    
    def imagePredict(self, img):
        self.model.eval()
        self.model.to(self.device)
        inputBatch = img.to(self.device)
        
        with torch.no_grad(): 
            output = self.model(inputBatch)
            probs = F.softmax(output, dim=1)
            predicted = torch.argmax(probs, dim=1)
    
            #print('Sonuclar: ', probs)
            #print("x: ", probs[0, predicted])
            #print(f'Classes: {classes[predicted.item()]}')
            #print("Predicted class indices:", predicted.cpu().numpy())
            #print("Prediction probabilities:", probs.cpu().numpy())
        return classes[predicted[0].item()], probs[0, predicted[0]].item()
