import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

input = cv.imread("./images/input.png")
# cv.calcHist([image], [channels], mask, [histSize], ranges[, hist[,accumuate]])
# Esta solo muestra el canal azul
histogram = cv.calcHist([input], [0], None, [256],[0, 256])

# Plot el histograma
plt.hist(input.ravel(), 256, [0, 256])
plt.show()
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histogram2 = cv.calcHist([input], [i], None, [256], [0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])

plt.show()
