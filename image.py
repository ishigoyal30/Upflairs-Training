import numpy as np 
import cv2
from time import sleep
fd = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
sd = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
vid = cv2.VideoCapture(0)

while True:
    flag , img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        x1,y1,w,h=(100,200,100,100)
        
        faces = fd.detectMultiScale(img_gray, scaleFactor = 1, minNeighbors = 5, minSize = (180,180))
    
        
        for x1,y1,w,h in faces:
            face = img_gray[y1:y1+h, x1:x1+w].copy()
            smiles = sd.detectMultiScale( faces, 1.1, 5)
            
            if len(smiles) == 1:
                xs,ys,ws,hs = smiles[0]
                
                for xs,ys,ws,hs in smiles:
                    cv2.rectangle(
                    img,
                    pt1=(xs,ys), pt2=(xs+ws, ys+hs),
                    color=(255,0,255),thickness=1
                )
            
            cv2.rectangle(
                img,
                pt1=(x1,y1), pt2=(x1+w, y1+h),
                color=(0,0,255),thickness=3
            )
          
        cv2.imshow('Preview' ,img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows() 