#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 构建高斯卷积算子：1.计算高斯矩阵 2.计算高斯矩阵的和 3.高斯矩阵除以其本身的和，即归一化，得到的便是高斯卷积算子
import math

import cv2
import numpy as np
def getGuassKernel(sigma,H,W):
    # 第一步：构建高斯矩阵
    # guassMatrix = np.zeros([H,W],np.float32)
    # # 得到中心点的位置
    # cH = (H-1)/2
    # cW = (W-1)/2
    # # 计算guass(sigma,r,c)
    # for r in range(H):
    #     for c in range(W):
    #         norm2 = math.pow(r-cH,2) + math.pow(c-cW,2)
    #         guassMatrix[r][c] = math.exp(-norm2/(2*math.pow(sigma,2)))
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    guassMatrix = np.exp(-0.5 * (np.power(r, 2) + np.power(c, 2)) / math.pow(sigma, 2))
    # 第二步：计算高斯矩阵的和
    sumGM = np.sum(guassMatrix)
    # 第三步：归一化
    guassKernel = guassMatrix/sumGM
    return guassKernel

#
gk1 = getGuassKernel(2,3,3)
print(gk1)
gk = cv2.getGaussianKernel(3,2,cv2.CV_64F)
print(gk)



from scipy import signal
# 通过定义guassBlur来实现图像的高斯平滑，首先进行水平方向高斯卷积，然后进行垂直方向高斯卷积
def gaussBlur(image,sigma,H,W,_boundary='full',_fillvalue=0):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 将灰度图像转换为二维数组
    gray_array = np.reshape(gray, (gray.shape[0], gray.shape[1]))
    # 构建水平方向上的高斯卷积核
    gaussKernel_x = cv2.getGaussianKernel(W,sigma,cv2.CV_64F)
    print(gaussKernel_x)
    # 转置
    gaussKernel_x = np.transpose(gaussKernel_x)
    print(gaussKernel_x)
    # 图像矩阵与水平高斯核卷积
    gaussBlur_x = signal.convolve2d(gray_array,gaussKernel_x,mode='same',boundary=_boundary,
                                    fillvalue=_fillvalue)
    # 构建垂直方向上的高斯卷积核
    gaussBlur_y = cv2.getGaussianKernel(H,sigma,cv2.CV_64F)
    # 与垂直方向上的高斯核卷积核
    gaussBlur_xy = signal.convolve2d(gaussBlur_x,gaussBlur_y,mode='same',boundary=_boundary,
                                     fillvalue=_fillvalue)
    return gaussBlur_xy

image = cv2.imread('../Img/0230610170721.png')
cv2.imshow('image',image)
# 高斯平滑(使用自定义函数）
blurImage = gaussBlur(image,3,11,11,'symm')
# 对blurImage进行灰度级显示
blurImage = np.round(blurImage)
blurImage = blurImage.astype(np.uint8)
# 使用opencv提供的函数
blurImage1 = cv2.GaussianBlur(image,(11,11),3)
cv2.imshow('guassblur',blurImage)
cv2.imshow('guassblur1',blurImage1)
cv2.waitKey(0)
cv2.destroyAllWindows()

