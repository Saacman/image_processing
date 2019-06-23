import cv2 as cv
import numpy as np

image = cv.imread('images/input.png')
# cv2.resize(src, dsize[, dst[, fx[optional, fy[optional, interpolation]optional]]])
# El metodo por defecto es el lineal
image_scaled = cv.resize(image, None, fx = 2, fy = 2)
cv.imshow("Scaling - Linear interpolation", image_scaled)
cv.waitKey()
# El algoritmo cubico es mejor pero más lento.
image_scaled = cv.resize(image, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)
cv.imshow("Scaling - Cubic interpolation", image_scaled)
cv.waitKey()

image_scaled = cv.resize(image, (900, 400), interpolation = cv.INTER_AREA)
cv.imshow("Scaling - Skewed Size, image_scaled", image_scaled)
cv.waitKey()
cv.destroyAllWindows()
