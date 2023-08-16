#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from copy import deepcopy
from PIL import Image
from matplotlib import pyplot as plt


#添加椒盐噪声图像
def add_peppersalt_noise(image, n):
    saltImg = image.copy()
    # 测量图片的长和宽
    w, h = image.shape[:2]
    # 生成n个椒盐噪声
    for i in range(n):
        x = np.random.randint(1, w)
        y = np.random.randint(1, h)
        if np.random.randint(0, 2) == 0:
            saltImg[x, y] = 0
        else:
            saltImg[x, y] = 255
    return saltImg

# 输出灰度图像
def medianBlur(image,winSize):
    # 图像的高、宽
    rows,cols,_ = image.shape
    # 窗口的高、宽，均为奇数
    winH,winW = winSize
    halfWinH = (winH-1)//2
    halfWinW = (winW-2)//2
    # 中值滤波后的输出图像
    medianBlurImg = np.zeros(image.shape,image.dtype)
    for r in range(rows):
        for c in range(cols):
            # 判断边界
            rTop = 0 if r-halfWinH<0 else r-halfWinH
            rBottom = rows-1 if r+halfWinH > rows-1 else r+halfWinH
            cLeft = 0 if c-halfWinW < 0 else c-halfWinW
            cRight = cols-1 if c+halfWinW > cols-1 else c+halfWinW+1 # 切片操作是左闭右开区间，所以右边界要加 1。
            # print(rTop,rBottom,cLeft,cRight)
            # 取邻域
            region = image[rTop:rBottom,cLeft:cRight]
            # 求中值
            medianBlurImg[r][c] = np.median(region)
    return medianBlurImg

img = cv2.imread('../Img/1686448914684.jpg')
#添加椒盐噪声
img1 = add_peppersalt_noise(img,1000)
# 调用opencv函数
img2 = cv2.medianBlur(img1,3)
# 调用自定义函数
img3 = medianBlur(img,(3,3))
cv2.imshow('img',img)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()



