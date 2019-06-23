# 025 Sharpening
import cv2 as cv
import numpy as np
image = cv.imread("images/input.png")

kernel_shapening = np.array([[-1, -1, -1],
                             [-1,  9, -1],
                             [-1, -1, -1]])
# aplicando distintos kernels a la imagen
sharpened = cv.filter2D(image, -1, kernel_shapening)
# hold = image
# for x in range(0, 4):
#     sharpened = cv.filter2D(hold, -1, kernel_shapening)
#     hold = sharpened
cv.imshow("Original", image)
cv.imshow("Image Sharpening", sharpened)
cv.waitKey()
cv.destroyAllWindows()
