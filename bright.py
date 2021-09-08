import cv2
import numpy as np
img = cv2.imread('bri1.jpeg', 0)



kernel=np.ones((11,11),np.uint8)

erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)

erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)

erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)

erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
kernel=np.ones((9,9),np.uint8)

erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)

erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)

erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)


erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)

cv2.imshow("img", img)
kernel=np.ones((7,7),np.uint8)
erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)
erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)
erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)


kernel=np.ones((5,5),np.uint8)

erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)
erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)


kernel=np.ones((3,3),np.uint8)
erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)
erosion1=cv2.erode(img,kernel,iterations=2)
img=cv2.dilate(erosion1,kernel,iterations=1)
erosion1=cv2.erode(img,kernel,iterations=1)
img=cv2.dilate(erosion1,kernel,iterations=2)





m_img = cv2.blur(img,(9,9))

kernel=np.ones((7,7),np.uint8)
erosion1=cv2.erode(m_img,kernel,iterations=4)
m_img=cv2.dilate(erosion1,kernel,iterations=4)

cv2.imshow("m_img", m_img)



timg = cv2.inpaint(img,m_img,9,cv2.INPAINT_NS)
_, threshold=cv2.threshold(timg,85,255,cv2.THRESH_BINARY)





des = cv2.bitwise_not(threshold)
contour,hier = cv2.findContours(des,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contour:
    cv2.drawContours(des,[cnt],0,255,-1)

gray = cv2.bitwise_not(des)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
res = cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel)

cv2.imshow("treshold", threshold)
#cv2.imshow("res", res)

cv2.waitKey(0)
cv2.destroyAllWindows()