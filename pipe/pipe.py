import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib

# read image as rgba
pipe = cv.imread("pipe.png", cv.IMREAD_UNCHANGED)
pipe = cv.cvtColor(pipe, cv.COLOR_RGB2RGBA)

# read image of man as rgba
man = cv.imread("man-without-pipe.png", cv.IMREAD_UNCHANGED)
man = cv.cvtColor(man, cv.COLOR_RGB2RGBA)

print(man.shape)
print(pipe.shape)

# resize pipe
pipe_small = cv.resize(pipe, None, fx=0.55, fy=0.55,
                       interpolation=cv.INTER_CUBIC)
# flip horizontaly
pipe_flip = cv.flip(pipe_small, 1)

# blank image of parent size with pipe in specific place
x_offset = 70
y_offset = 280

pipe_shape_empty = 0*np.ones_like(man)

pipe_shape_empty[y_offset:y_offset+pipe_flip.shape[0],
                 x_offset:x_offset+pipe_flip.shape[1]] = pipe_flip

pipe_gray_overlay = cv.cvtColor(pipe_shape_empty, cv.COLOR_BGR2GRAY)
pipe_overlay_mask = cv.threshold(
    pipe_gray_overlay, 1, 255, cv.THRESH_BINARY)[1]

# blure for better blend
pipe_overlay_mask = cv.blur(pipe_overlay_mask, (5, 5))

# inverse mask, that covers all the black pixels
pipe_background_mask = 255 - pipe_overlay_mask

# reverse to color
pipe_overlay_mask = cv.cvtColor(pipe_overlay_mask, cv.COLOR_GRAY2BGRA)
pipe_background_mask = cv.cvtColor(pipe_background_mask, cv.COLOR_GRAY2BGRA)

# convert the images to floating point in range 0.0 - 1.0
man = (man * (1 / 255.0)) * (pipe_background_mask * (1 / 255.0))
pipe = (pipe_shape_empty * (1 / 255.0)) * (pipe_overlay_mask * (1 / 255.0))

res = np.uint8(cv.addWeighted(man, 255.0, pipe, 255.0, 0.0))


plt.imshow(res)
cv.imshow('image', res)
cv.waitKey(0)
cv.destroyAllWindows()
