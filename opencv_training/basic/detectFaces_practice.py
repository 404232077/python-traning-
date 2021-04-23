# import cv2
# pictPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# face_cascade = cv2.CascadeClassifier(pictPath)
# img = cv2.imread("media\\spurs4.jpg")
# print(img.shape[0])
# print(img.shape[1])
# face_locat = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
# cv2.rectangle(img,(0,0),(130,30),(0,255,127),-1)
# cv2.putText(img,"Find "+str(len(face_locat))+" face",(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
# for (x,y,w,h) in face_locat:
#     cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255), 2)
# cv2.namedWindow("detectface")
# cv2.imshow("detectface",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# 存取辨識的臉部資料
# import cv2
# pictPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# face_cascade = cv2.CascadeClassifier(pictPath)
# img = cv2.imread("media\\spurs4.jpg")
# face_locat = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
# count = 0
# for (x,y,w,h) in face_locat:
#     cut = img[y:y+h, x:x+w]
#     count += 1
#     filename = "media\\cut" + str(count) + ".jpg"
#     cv2.imwrite(filename, cut)

# 截取圖片與設定圖片大小語法
# img1 = img[10:43,388:421]       #[左上角y座標:右下角y座標, 左上角x座標:右下角x座標]
# img2 = cv2.resize(img1, (300,300))
# cv2.imwrite("media\\img01.jpg",img2)

# 取得像素
# import cv2
# img = cv2.imread("media\\spurs4.jpg")
# print(img.shape[0], img.shape[1])       #img.shape[0]:圖片高度, img.shape[1]::圖片寬度
# for y in range(1,571):
#     for x in range(1,426):
#         print(img[y,x], end = "")       #回傳的串列為[B,G,R]
