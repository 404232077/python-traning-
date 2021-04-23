# 開啟攝影機並截圖存檔

import cv2
cv2.namedWindow("frame")
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, img = cap.read()
    print(ret, img)
    if ret:
        cv2.imshow("frame", img)
        k = cv2.waitKey(100)
        if k == ord("z") or k == ord("Z"):
            cv2.imwrite("media\\s.jpg", img)
            break
cap.release()
cv2.destroyWindow("frame")

