import cv2 as cv
import numpy as np
input = cv.imread("./images/input.png")

# Valores BGR para el primer pixel
B,G,R = input[10,50]
print B, G, R
print input.shape

gray_img = cv.cvtColor(input, cv.COLOR_BGR2GRAY)
print gray_img[10,50]
print gray_img.shape


# Cambiando de BGR a HSV
# H: 0 - 180, S: 0 -255, v: 0 - 255
hsv_image = cv.cvtColor(input, cv.COLOR_BGR2HSV)
cv.imshow('HSV IMAGE', hsv_image)

cv.imshow('Hue channel', hsv_image[:,:,0])
cv.imshow('Saturation channel', hsv_image[:,:,1])
cv.imshow('Value channel', hsv_image[:,:,2])
cv.imshow('ORIGINAL', input)
cv.waitKey()
cv.destroyAllWindows()


# Separando los canales RGB
B, G, R = cv.split(input)
print B.shape
cv.imshow('RED', R)
cv.imshow('Green', G)
cv.imshow('Blue', B)
cv.waitKey()
cv.destroyAllWindows()

# Solo muestra escala de grises porque son arreglos bidimensionales (solo un canal)
# Reuniendo los canales
merged = cv.merge([B, G, R])
cv.imshow("Merged", merged)
cv.waitKey()
cv.destroyAllWindows()

merged = cv.merge([B+50, G , R])
cv.imshow("Merged with blue amplified", merged)
cv.waitKey()
cv.destroyAllWindows()

# Para ver los canales RGB individuales utilizaremos una matriz de ceros con las dimensiones de input
zeros = np.zeros(input.shape[:2], dtype = "uint8")
cv.imshow('RED', cv.merge([zeros, zeros, R]))
cv.imshow('Green', cv.merge([zeros, G, zeros]))
cv.imshow('Blue', cv.merge([B, zeros, zeros]))
cv.waitKey()
cv.destroyAllWindows()
