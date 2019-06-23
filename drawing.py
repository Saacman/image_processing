import cv2 as cv
import numpy as np

# Rectangulo negro con 3 canales
image = np.zeros((512, 512, 3), np.uint8)
# Rectangulo negro en b&w
image_bw = np.zeros((512, 512), np.uint8)

cv.imshow("Black Rect (Color)", image)
cv.imshow("Black Rect (B&W)", image_bw)
cv.waitKey()
cv.destroyAllWindows()

# Una diagonal
# line(imagen, p_inicial, p_final, color, grosor (pixeles))
cv.line(image, (0,0), (511, 511), (255, 127, 0), 5)
# Un Rectangulo. -1 rellena toda la figura
cv.rectangle(image, (100, 100), (300, 250), (165, 98, 171), 5)
# Un circulo
cv.circle(image, (350,350), 100, (66, 171, 96), -1)

# Un poligono
pts = np.array([[10, 50], [400,50], [90, 200], [50, 500]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(image, [pts], True, (255, 127, 0), 3)

# Texto
cv.putText(image, "Hello World", (75,290), cv.FONT_HERSHEY_COMPLEX, 2, (150,170,0), 3)
cv.imshow("Blue line", image)
cv.waitKey()
cv.destroyAllWindows()
