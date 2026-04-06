import cv2

# Read Image
#imread loads the picture
img = cv2.imread("C:/Users/rajka/Downloads/PRO-c116-Teacher-Reference-Code-main (1)/PRO-c116-Teacher-Reference-Code-main/butterfly.jpg")

# Display Colored Image
#imshow displays the image
cv2.imshow("Display Image",img)

# Convert Colored Image To Grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Display Grayscale Image
cv2.imshow("Grayscale", gray_img)


#print(gray_img)

cv2.waitKey(0)