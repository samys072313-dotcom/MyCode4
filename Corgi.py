import cv2

img = cv2.imread("C:/Users/rajka/Downloads/PRO-c116-Teacher-Reference-Code-main (1)/PRO-c116-Teacher-Reference-Code-main/corgiImg.jpg")
cv2.imshow("display image", img)
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayScale",gray_img)
cv2.waitKey(0)