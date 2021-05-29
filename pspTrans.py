### this doesn't work yet... -> done
### cv2.drawingContours' 2nd argument should be [ cont ]!!!

import cv2
import numpy as np
import horizontalFit as hF
#from matplotlib import pyplot as plt

img = hF.src1
im = hF.bImage
'''
img = cv2.imread('./data/collapsedSquare.png')
im = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret,thresh = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
'''
mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
#contours, _ = cv2.findContours(im, mode, method)

cnt = hF.cnt
epsilon = 0.1*cv2.arcLength(cnt,True)

# print([cv2.arcLength(x,True) for x in contours])

approx = cv2.approxPolyDP(cnt, epsilon = 1, closed = True)

imR = np.zeros(img.shape, dtype='uint8')
imR=cv2.drawContours(imR, [approx], -1, (0,255,0), 4)
cv2.imshow('Epsilon1', imR)
cv2.imshow('Original', im)

epsilon2 = 0.01*cv2.arcLength(cnt,True)
approx2 = cv2.approxPolyDP(cnt, epsilon = 30, closed = True)
imC = np.zeros(img.shape, dtype='uint8')
imC=cv2.drawContours(imC, [approx2], -1, (0,255,0), 4)
#cv2.imshow('Epsilon50', imC)
'''
plt.subplot(131),plt.imshow(im)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(imR)
plt.title('EPSILON(1)'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(imC)
plt.title('EPSILON(10)'), plt.xticks([]), plt.yticks([])

plt.show()
'''
#detectConerPoint
gray = cv2.cvtColor(imC, cv2.COLOR_BGR2GRAY)
K = 4
corners = cv2.goodFeaturesToTrack(gray, maxCorners=K,
              qualityLevel=0.05, minDistance=10)
print('corners.shape=',corners.shape)
#tempSort = sorted(corners)
print('corners=',corners)

corners = corners.reshape(-1, 2)
for x, y in corners:
    cv2.circle(imC, (x, y), 5, (0,0,255), -1)
cv2.imshow('Epsilon30-Corners', imC)
cv2.imshow('Original', img)

#PerspectiveTransformation
sortedCorn = sorted(corners, key=lambda x: (x[0], x[1]))
tempCorn= sorted(sortedCorn[:2], key=lambda x: x[1])
leftUpX = tempCorn[0][0]
leftUpY = tempCorn[0][1]
leftDwX= tempCorn[1][0]
leftDwY= tempCorn[1][1]
tempCorn= sorted(sortedCorn[2:4], key=lambda x: x[1])
rightUpX = tempCorn[0][0]
rightUpY = tempCorn[0][1]
rightDwX= tempCorn[1][0]
rightDwY= tempCorn[1][1]

pts1 = np.float32([[leftUpX, leftUpY],
                   [leftDwX, leftDwY],
                   [rightUpX, rightUpY],
                   [rightDwX, rightDwY]])
pts2 = np.float32([[10,10],[10,130],[1150,10],[1150,130]])
M = cv2.getPerspectiveTransform(pts1, pts2)

Result = cv2.warpPerspective(img, M, (1150,130))
cv2.imshow('perspective', Result)

cv2.waitKey()
cv2.destroyAllWindows()

