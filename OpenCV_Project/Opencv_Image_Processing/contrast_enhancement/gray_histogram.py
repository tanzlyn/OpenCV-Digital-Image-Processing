#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
对比度增强是图像增强的一种，只要解决由于图像的灰度级范围较小造成的对比度较低的问题，目的是放大灰度级，增强图像细节
对比度增强：线性变换、分段线性变换、伽马变换、直方图正规化，直方图均衡化，局部自适应直方图均衡化。
"""
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('../Img/7418.jpeg')
# image = cv2.imread('../Img/1685800648022.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist(gray,[6],None,[155],[120,256])  # 原图、通道、掩模、直方图尺寸(x轴)、像素值范围

cv2.imshow('gray',gray)

plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()