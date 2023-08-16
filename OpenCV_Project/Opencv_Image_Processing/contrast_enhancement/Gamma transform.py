#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
图像归一化后得到图像I(r,c),伽马变换就是O(r,c)=I(r,c)^γ,0<=r<H,0<=c<W,
γ=1，图像不变，。如果图像整体或者感兴趣区域较暗，令0<γ<1可以增强对比度；如果较亮，则令γ>1,降低对比度。
实质上是对图像矩阵中的每一个值进行幂运算。
"""
import numpy as np
I=np.array([[1,2],[3,4]])
# O = np.power(I,2)
# print(O)

import cv2
# image = cv2.imread('../Img/1685800379512.jpg')  # gamma=0.5
image = cv2.imread('../Img/1685795920851.jpg')  # gamma=0.3
# image = cv2.imread('../Img/26.jpg')
# image = cv2.imread('../Img/001.jpg')
# image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 图像归一化
f1 = image/255.0
# 伽马变换
gamma = 0.3
O= np.power(f1,gamma)
cv2.imshow('I',image)
cv2.imshow('O',O)
cv2.waitKey(0)
cv2.destroyAllWindows()
