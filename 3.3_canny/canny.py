import numpy as np
import cv2 as cv


def make_slid(a_min: int, a_max: int, curr: int, slider_id: str, root_win_name: str, on_change_callback=lambda x: x):
    cv.createTrackbar(slider_id, root_win_name, a_min,
                      a_max, on_change_callback)
    cv.setTrackbarPos(slider_id, root_win_name, curr)
    return slider_id


def getslid(*ids, root_wind: str):
    try:
        results = [cv.getTrackbarPos(idd, root_wind) for idd in ids]
        return results[0] if len(results) == 1 else results
    except Exception as e:
        print(f'Error in getting slider value - {str(e)}')
        return None


def setslid(id_: str, value: int, root_wind: str):
    cv.setTrackbarPos(id_, root_wind, value)


# Name your window
root_wind = 'Canny edge detector'
cv.namedWindow(root_wind)


img = cv.imread("lena.png", cv.IMREAD_COLOR)
scale_percent = 90  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv.resize(img, dim)

sliders = [
    make_slid(0, 500, 50,  'Low threshold', root_wind),
    make_slid(0, 500, 100,  'High threshold', root_wind),
    make_slid(3, 7, 3, 'Aperture size', root_wind),
    make_slid(1, 20, 1, 'Blur', root_wind),
    make_slid(0, 1, 0, 'Color', root_wind)
]


while True:

    values = getslid('Low threshold', 'High threshold',
                     'Aperture size', 'Blur', 'Color', root_wind=root_wind)

    if(values[3] != 0):
        img_blur = cv.blur(img, (values[3], values[3]))
    else:
        img_blur = img

    if(values[2] < 3):
        setslid('Aperture size', 3, root_wind=root_wind)
        values[2] = 3
    elif(values[2] > 7):
        setslid('Aperture size', 7, root_wind=root_wind)
        values[2] = 7
    elif(values[2] == 4 or values[2] == 6):
        values[2] = 5

    if(values[4] == 0):
        img_gray = cv.cvtColor(img_blur, cv.COLOR_RGB2GRAY)
        img_canny = cv.Canny(image=img_gray,
                             threshold1=values[0], threshold2=values[1], apertureSize=values[2])

        cv.imshow(root_wind, img_canny)
    else:
        cv.imshow(root_wind, img_blur)
    code = cv.waitKey(1)
    if code == ord('q'):
        break

cv.destroyAllWindows()
