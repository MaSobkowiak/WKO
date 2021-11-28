import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


kernel_ellipse5 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
kernel_ellipse6 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (6, 6))

coins = cv.imread("text_no_ocr.png", cv.IMREAD_GRAYSCALE)
_, coins_bin = cv.threshold(coins, 125, 255, cv.THRESH_BINARY)

# wykrycie kształtów
coins_dilated = cv.dilate(coins_bin, kernel_ellipse5, iterations=1)
# powiększenie ich do skali
coins_eroded = cv.erode(coins_dilated, kernel_ellipse6, iterations=1)
# zamiana na białe piksele
coins[coins_eroded == 0] = 255

plt.figure(figsize=[15, 5])
plt.subplot(121)
plt.imshow(coins_bin, cmap='gray')
plt.title("Orginal")
plt.subplot(122)
plt.imshow(coins, cmap='gray')
plt.title("Result")

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
