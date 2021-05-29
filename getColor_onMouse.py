#0311.py
import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
##    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        print("cursor: ", x, y)
        print(img[y, x])
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), 3)
            
img = cv2.imread('./result_subway/subf.jpg')
cv2.imshow('imgA', img)
cv2.setMouseCallback('imgA', onMouse, [img])

pts1 = np.float32([[18,59],[10,107],[986,20],[992,76]])

# 좌표 이동점
pts2 = np.float32([[10,10],[10,150],[1100,10],[1100,150]])
'''
# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
cv2.circle(img, (504,1003), 20, (255,0,0),-1)
cv2.circle(img, (243,1524), 20, (0,255,0),-1)
cv2.circle(img, (1000,1000), 20, (0,0,255),-1)
cv2.circle(img, (1280,1685), 20, (0,0,0),-1)
'''
M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1100,150))
cv2.imshow('perspective', dst)

cv2.waitKey()
cv2.destroyAllWindows()
