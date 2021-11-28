import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib

# read img
img = cv.imread("soyjaks.jpg", cv.IMREAD_COLOR)

# crop img
img = np.delete(img, np.s_[0:60], axis=1)
img = np.delete(img, np.s_[-80:-1], axis=1)
img = np.delete(img, np.s_[-200:-1], axis=0)

# add text
cv.putText(img, 'OMG not chikenz!', (10, 80), cv.FONT_HERSHEY_SIMPLEX,
           1.5, (0, 0, 2550), 4, cv.LINE_AA)

# add circle
cv.circle(img, (268, 224), 52, (255, 51, 204), 12)

plt.imshow(img)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
