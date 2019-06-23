import cv2 as cv
import numpy as np
# tambien se puede hacer:
# input = cv.imread("./images/input.jpg", 0)
input = cv.imread("./images/input.jpg")
cv.imshow('Original', input)
cv.waitKey()

gray_image = cv.cvtColor(input, cv.COLOR_BGR2GRAY)

cv.imshow('Grayscale', gray_image)
cv.waitKey()

cv.destroyAllWindows()
