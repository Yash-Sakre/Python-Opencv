import cv2

#load cascade 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Read Image
img = cv2.imread('image.jpg')
# Convert image to gray image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Detect faces
faces = face_cascade.detectMultiScale(gray,1.1,4)
#Draw a Rectangle around deteted faces
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#Output
cv2.imshow('img',img)
cv2.waitkey()
