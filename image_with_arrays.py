import numpy as np
import cv2

# Create a black image
black = np.zeros([600,600])

# # f_row = black[1:2]
# # print(f_row)

# # f_col = black[:,1:2]
# # print(f_col)

black[200:400,200:400] = 255
print(black)

cv2.imshow("black",black)
cv2.waitKey(0)


