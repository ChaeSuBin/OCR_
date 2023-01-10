import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
##    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        print("cursor: ", x, y)
        print(img[y, x])
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), 3)
            
img = cv2.imread('../Arrow_/src_Arrow/left2.jpg')
cv2.imshow('imgA', img)
cv2.setMouseCallback('imgA', onMouse, [img])

cv2.waitKey()
cv2.destroyAllWindows()
