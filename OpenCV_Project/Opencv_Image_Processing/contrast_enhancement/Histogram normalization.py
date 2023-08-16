#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
直方图正规化的原理：
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
I = cv2.imread('../Img/1685850324771.jpg')
# I= cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
histI = cv2.calcHist(I,[0],None,[255],[0,256])
# 求I的最小值和最大值
Imax = np.max(I)
Imin = np.min(I)
# 要输出的最小灰度级和最大灰度级
Omin,Omax = 0,255
# 计算a和b的值
a = float(Omax-Omin)/(Imax-Imin)
b = Omin-a*Imax
# 矩阵的线性变换
O = a*I + b
# 数据类型转换
O = O.astype(np.uint8)
histO = cv2.calcHist(O,[0],None,[255],[0,256])
cv2.imshow('I',I)
cv2.imshow('O',O)
plt.subplot(1,2,1)
plt.plot(histI)
plt.subplot(1,2,2)
plt.plot(histO)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


# 调用opencv的直方图正规化函数normalize
img = cv2.imread('../Img/1685850324771.jpg',cv2.IMREAD_ANYCOLOR)
# 直方图正规化
dst = cv2.normalize(img,255,0,cv2.NORM_MINMAX,cv2.CV_8U)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()