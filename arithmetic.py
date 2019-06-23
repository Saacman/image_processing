import cv2 as cv
import numpy as np
image = cv.imread("images/input.png")

# Matriz del mismo size de image con valores de un escalar
M = np.ones(image.shape, dtype = "uint8") * 50

# Suma
added = cv.add(image, M)
cv.imshow("Added", added)

# Resta
subtracted = cv.subtract(image, M)
cv.imshow("subtracted", subtracted)

cv.waitKey()
cv.destroyAllWindows()
