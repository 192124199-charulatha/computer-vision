import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread(r"C:\Users\HI\Pictures\spy x family.jpg")
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
