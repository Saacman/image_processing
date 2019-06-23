import cv2 as cv
import numpy as np
# Affine : scaling, rotation, translation
# Non-Affine: DOes not preserve parallelism, length, and angle, but collinearity and incidence

# TRANSLATION
image = cv.imread("images/input.png")
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4
#      |1 0 Tx|
# T =  |0 1 Ty|
# T es la matriz de translation
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

# warpAffine
translated = cv.warpAffine(image, T, (width, height))
print T
# cv.imshow("original", image)
# cv.imshow("Translation", translated)
# cv.waitKey()
# cv.destroyAllWindows()

# SCALE AND ROTATION
# M = |cosA -sinA|
#     |sinA  cosA| A es el angulo de rotacion
# getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)
# Rotacion sobre el centro
scale_matrix = cv.getRotationMatrix2D((width/2, height/2), 0, .5)
rotation_matrix = cv.getRotationMatrix2D((width/2, height/2), 180, 1)
rotated = cv.warpAffine(image, rotation_matrix, (width, height))
scaled = cv.warpAffine(image, scale_matrix, (width, height))
# cv.imshow("original", image)
# cv.imshow("Rotation", rotated)
# cv.imshow("Scale", scaled)
# cv.waitKey()
# cv.destroyAllWindows()

# TRANSPOSE
#
# transposed = cv.transpose(image)
# cv.imshow("Transpose", transposed)
# cv.waitKey()
