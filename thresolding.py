# 026 Thresolding
# Convertir una imagen a forma binaria
# cv.threshold(image, threshold value, max value, threshold type)
# Es necesario convertir a escala de grises ante de Thresolding
# # types:
# cv.THRESH_BINARY
# cv.THRESH_BINARY_INV
# cv.THRESH_TRUNC
# cv.THRESH_TOZERO
# cv.THRESH_TOZERO_INV
import cv2 as cv
import numpy as np
image = cv.imread("images/input.png", 0) # Carga la imagen en escala de grises
cv.imshow("Original", image)

# Valores debajo de 127 son 0, por encima de 127 son 255 (blanco)
ret, thresh1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
cv.imshow("1 Thresold Binary", thresh1)

# Valores debajo de 127 son 255 y por encima 0
ret, thresh2 = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
cv.imshow("2 Thresold Binary Inverse", thresh2)

# Valores sobre 127 son truncados a 127 (se ignora el argumento de 255)
ret, thresh3 = cv.threshold(image, 127, 255, cv.THRESH_TRUNC)
cv.imshow("3 Thresold truncated", thresh3)

# Valores debajo de 127 son 0, por encima de 127 no cambian
ret, thresh4 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO)
cv.imshow("4 Thresold to zero", thresh4)

ret, thresh5 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO_INV)
cv.imshow("5 Thresold to zero inverse", thresh5)

cv.waitKey()

# Adaptive threshold

origin = cv.imread("images/origin.jpg", 0)

origin = cv.pyrDown(origin)
origin = cv.pyrDown(origin)

cv.imshow("0riginal", origin)

# Primero hacer un blur para remover el ruido
origin = cv.GaussianBlur(origin, (3,3), 0)

thresh = cv.adaptiveThreshold(origin, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 5)
cv.imshow("Adaptive Mean Thresholding", thresh)

_, th2 = cv.threshold(origin, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow("Otsu's Thresholding", th2)

blur = cv.GaussianBlur(origin, (5,5), 0)
_, th3 = cv.threshold(blur , 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow("Gaussian Otsu's Thresholding", th3)
cv.waitKey()
cv.destroyAllWindows()
