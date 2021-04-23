# opencv 圖像格式轉 pillow
# opencv 像素格式為 BGR，pillow 像素格式為 RGB

# import cv2
# from PIL import Image
# img = cv2.imread("media\\spurs4.jpg")
# image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# image.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(type(img))
# print(type(image))

# pillow 圖像格式轉 opencv
from PIL import Image
import cv2
import numpy as np
img = Image.open("media\\spurs4.jpg")
image = cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
cv2.namedWindow("frame")
cv2.imshow("frame",image)
cv2.waitKey(0)
cv2.destroyAllWindows()