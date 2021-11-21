import cv2
from model import FacialExpression
import numpy as np

model = FacialExpression('model.json', 'model_weights.h5')
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class VideoCamera(object) :
    def __init__(self) :
        self.video = cv2.VideoCapture('Face Test.mp4')
    def __del__(self) :
        self.video.release()
        
    def get_frame(self) :
        _, frame = self.video.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = face_detector.detectMultiScale(gray_frame, 1.3, 5)
        
        for [x, y, w, h] in faces :
            face = gray_frame[y : y+h, x : x+w]
            face = cv2.resize(face, (48, 48))
            
            pred = model.predict(face[np.newaxis, :, :, np.newaxis])
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 3)
            
            cv2.putText(frame, pred, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0), 3)
            
        _, jpeg = cv2.imencode('.jpg', frame)
        
        return jpeg.tobytes()    