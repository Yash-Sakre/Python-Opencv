import cv2
#Load Haarcascade xml files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#load Image from Local Computer
img = cv2.imread('image3.jpeg')
#convert Image to gray image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detect faces first
faces = face_cascade.detectMultiScale(gray,1.1,4)
#loop to create rectangle around the faces
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #detect the smile in face 
    smile = smile_cascade.detectMultiScale(gray,1.5,10)
    #create rectangle around smiles 
    for v,t,g,f in smile:
        cv2.rectangle(img,(v,t),(v+g,t+f),(0,0,255),3)
    
#display output    
cv2.imshow('smile',img)
cv2.waitkey()

