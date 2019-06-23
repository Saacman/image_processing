import cv2 as cv
import numpy as np
image = cv.imread("images/input.png")

smaller = cv.pyrDown(image)
larger = cv.pyrUp(image) # Retorna una imagen del size original, pero tiene perdida de calidad

cv.imshow("Original", image)
cv.imshow("Smaller", smaller)
cv.imshow("Larger", larger)
cv.waitKey()
cv.destroyAllWindows()
# Se puede usar en un loop para obtener imagenes mas reducidas.
