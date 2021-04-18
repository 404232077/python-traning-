# import cv2

# cv2.namedWindow("picture1")
# cv2.namedWindow("picture2")
# image1 = cv2.imread("crayon.png",1)
# image2 = cv2.imread("crayon.png",0)
# cv2.imshow("picture1",image1)
# cv2.imshow("picture2",image2)
# cv2.waitKey(3000)
# cv2.destroyWindow("picture1")
# cv2.waitKey(3000)
# cv2.destroyWindow("picture2")

import cv2

pictPath = r"C:\code\Python\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)
img = cv2.imread("spurs1.jfif")
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(20,20))

cv2.rectangle(img, (img.shape[1]-140,img.shape[0]-20), (img.shape[1],img.shape[0]), (0,255,255), -1)

cv2.putText(img, "Finding"+str(len(faces))+"face", (img.shape[1]-135,img.shape[0]-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
cv2.namedWindow("Face", cv2.WINDOW_NORMAL)
cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyWindow("Face")
cv2.imwrite("spurs2.png", img)