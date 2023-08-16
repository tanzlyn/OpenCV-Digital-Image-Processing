#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
def threshold_two_peak(image):
    # 计算灰度直方图
    histogram = calcGrayHist(image)
    # 找到灰度直方图的最大峰值对应的灰度值
    maxLoc = np.where(histogram == np.max(histogram))
    firstPeak = maxLoc[0][0]
    # 寻找灰度直方图的第二个峰值对应的灰度值
    measureDists = np.zeros([256], np.float32)
    for k in range(256):
        measureDists[k] = pow(k - firstPeak, 2) * histogram[k]
    maxLoc2 = np.where(measureDists == np.max(measureDists))
    secondPeak = maxLoc2[0][0]
    # 找到两个峰值之间的最小值对应的灰度值，作为阈值
    thresh = 0
    if firstPeak > secondPeak:  # 第一个峰值在第二个峰值的右侧
        temp = histogram[int(secondPeak):int(firstPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = secondPeak + minLoc[0][0] + 1
    else:  # 第一个峰值在第二个峰值的右侧
        temp = histogram[int(firstPeak):int(secondPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = firstPeak + minLoc[0][0] + 1
    # 找到阈值后进行阈值处理，得到二值图
    threshImage = image.copy()
    threshImage[threshImage > thresh] = 255
    threshImage[threshImage <= thresh] = 0
    print(firstPeak, secondPeak, thresh)
    return thresh, threshImage


def calcGrayHist(I):
    # 计算灰度直方图
    h, w = I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
    return grayHist

I = cv2.imread('../Img/1686798492231.jpg')
thresh, threshImage = threshold_two_peak(I)
print(thresh)
cv2.imshow('I',threshImage)
cv2.waitKey(0)
cv2.destroyAllWindows()