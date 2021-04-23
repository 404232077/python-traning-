import cv2
pictPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(pictPath)
img = cv2.imread("media\\spurs3.jpeg")
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6, minSize=(20,20))
print(faces)
cv2.rectangle(img, (img.shape[1]-140,img.shape[0]-20), (img.shape[1],img.shape[0]), (0,255,255), -1)
cv2.putText(img, "Finding "+str(len(faces))+" face", (img.shape[1]-135,img.shape[0]-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
cv2.namedWindow("Face", cv2.WINDOW_NORMAL)
cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyWindow("Face")