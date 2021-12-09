# opencv-python是与图像处理有关的包
# 定位出图像内的人脸
import cv2

img = cv2.imread('/Users/danco/Desktop/pystart/模块与包/p1.jpg') # 路径都要写全路径，不然会包215错误
face_engine = cv2.CascadeClassifier('/opt/homebrew/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')
faces = face_engine.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),7)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

