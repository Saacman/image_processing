# 024 - Blurring
import cv2 as cv
import numpy as np
image = cv.imread("images/input.png")
cv.imshow("Original", image)
cv.waitKey()

# La suma de todos los elementos del kernel es 1

# Kernel 3 x 3
kernel_3x3 = np.ones((3, 3), np.float32) / 9

# Kernel 7 x 7
kernel_7x7 = np.ones((7, 7), np.float32) / 49

# la funcion filter2D hace una convolucion de la matriz con la imagen
# cv2.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
blurred = cv.filter2D(image, -1, kernel_3x3)
cv.imshow("3x3", blurred)
cv.waitKey()

blurred = cv.filter2D(image, -1, kernel_7x7)
cv.imshow("7x7", blurred)
cv.waitKey()

# Otros metodos
# Toma los pixeles en la caja del tamano designado y reemplaza el elemento central por el promedio
# El tamano de la caja debe ser impar positivo
blur = cv.blur(image, (3, 3))
cv.imshow("Average", blur)
cv.waitKey()

# Utiliza un kernel gaussiano
gaussian = cv.GaussianBlur(image, (7,7), 0)
cv.imshow("Gaussian Blur", gaussian)
cv.waitKey()

# Funciona como el promedio, pero utilliza la media
median = cv.medianBlur(image, 5)
cv.imshow("Median Blur", median)
cv.waitKey()

# Bilateral: Sirve para reducir el ruido y mantener los bordes definidos
# Solo aplica el filtro gaussiano a los pixeles  con intensidades similares al pixel central.
# mantiene los bordes porque en los bordes los pixeles tienen una variacion grande
bilateral = cv.bilateralFilter(image, 9, 75, 75)
cv.imshow("Bilateral Blur", bilateral)
cv.waitKey()

# De-noising - Non - Local Means Denoising
dst = cv.fastNlMeansDenoisingColored(image, 6, 6, 7, 21)
cv.imshow("Denoising", dst)
cv.waitKey()


cv.destroyAllWindows()
