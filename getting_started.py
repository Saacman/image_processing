import cv2 as cv
import numpy as np
# Guardar la imagen en una variable de python
input = cv.imread("./images/input.jpg")
# Primer argumento es el titulo de la ventana, el segundo la imagen a mostrar
cv.imshow('Hello world', input)

cv.waitKey()

cv.destroyAllWindows()
# imprime las dimensiones de la imagen x, y y sus componentes (RGB)
print input.shape

# guardando imagenes

cv.imwrite('output.jpg', input)
cv.imwrite('output.png', input)
