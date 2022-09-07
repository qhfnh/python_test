import cv2
import numpy as np
img = cv2.imread('u.jpeg')
# 进行人脸识别
#img = cv2.resize(img, (400, 600))
img = img.copy()
faceDetect = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml') # 级联分配器
faces = faceDetect.detectMultiScale(img)
for x, y, w, h in  faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), color=[0,0,255], thickness=2) #矩形

cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()