# Masking
import cv2 as cv
import numpy as np

# Cuadrado
square = np.zeros((300, 300), np.uint8)
cv.rectangle(square, (50, 50), (250, 250), 255, -1)
cv.imshow("Square", square)
# cv.waitKey()

# Elipse
ellipse = np.zeros((300, 300), np.uint8)
cv.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
# cv.imshow("Ellipse", ellipse)
# cv.waitKey()

# Operaciones bitwise
bit_and = cv.bitwise_and(square, ellipse)
cv.imshow("AND", bit_and)
cv.waitKey()

bit_or = cv.bitwise_or(square, ellipse)
cv.imshow("OR", bit_or)
cv.waitKey()

bit_xor = cv.bitwise_xor(square, ellipse)
cv.imshow("XOR", bit_xor)
cv.waitKey()

bit_not = cv.bitwise_not(square)
cv.imshow("NOT", bit_not)
cv.waitKey()

cv.destroyAllWindows()
