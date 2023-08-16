#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import matplotlib as plot
import matplotlib.pyplot as plt


image = cv2.imread('./melonseed.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray],[0],None,[255],[0,256])
_,thresh_img = cv2.threshold(gray,230,250,cv2.THRESH_BINARY_INV)
contours, o = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = contours[0]
contour_img = image
# 遍历所有轮廓线，找到面积最大的轮廓线
max_area = 0
max_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_contour = contour

contour_img = cv2.drawContours(contour_img, [max_contour], 0, (255, 0, 0), 5)
cv2.imshow('seed',image)
cv2.imshow('gray',gray)
cv2.imshow('thresh_img',thresh_img)
cv2.imshow('contours',contour_img)
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()