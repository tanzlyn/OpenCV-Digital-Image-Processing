#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
O=a*I+b
当a=1,b=0时，O是I的一个副本
当a>1,增大对比度
当a<1，对比的减小
b的值影响亮度：b>0,亮度增加，当b<0,亮度减小
"""
import cv2
import numpy as np

# 不同数据类型的常数对结果的影响

I=np.array([[0,200],[23,4]],np.uint8)
O=2*I  # 400超出了uint8的数据范围，所以400%256=144
P=2.0*I  # 这里数据类型是float64
# print(O)
# print(P)

# O[O>255]=255的作用是将数组O中大于255的值均设置为255，成员函数astype的作用是改变ndarray的数据类型
import cv2
import matplotlib.pyplot as plt
I = cv2.imread('../Img/1685795920851.jpg')
# I = cv2.imread('../Img/1685850324771.jpg')
histI = cv2.calcHist(I,[0],None,[255],[0,256])
# 线性变换
a = 2
O = float(a)*I
# 进行数据截断，大于255的值要截断为255
O[O>255] = 240
# 数据类型转换
O = np.round(O)
O = O.astype(np.uint8)
histO = cv2.calcHist(O,[0],None,[255],[0,255])
cv2.imshow('I',I)
cv2.imshow('O',O)
plt.subplot(1,2,1)
plt.plot(histI)
plt.subplot(1,2,2)
plt.plot(histO)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

