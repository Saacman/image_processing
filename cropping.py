import cv2 as cv
import numpy as np
image = cv.imread("images/input.png")
height, width = image.shape[:2]

start_row, start_col = int(height * .25), int(width * .25)

end_row, end_col = int(height * .75), int(width * .75)

cropped = image[start_row:end_row, start_col:end_col]

cv.imshow("Original", image)
cv.imshow("Cropped", cropped)
cv.waitKey()
cv.destroyAllWindows()
