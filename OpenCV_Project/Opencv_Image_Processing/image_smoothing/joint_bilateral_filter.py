#!/user/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import math

def getClosenessWeight(sigma_g, H, W):
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    closeWeight = np.exp(-0.5*np.power(r, 2) + np.power(c, 2) / math.pow(sigma_g, 2))
    return closeWeight

def joinBLF(I, H, W, sigma_g, sigma_d, borderType=cv2.BORDER_DEFAULT):
    # 构建空间距离权重模板
    closenessWeight = getClosenessWeight(sigma_g, H, W)
    # 对I进行高斯平滑
    Ig = cv2.GaussianBlur(I, (H, W), sigma_g)
    # 模板的中心点位置
    cH = (H - 1) // 2
    cW = (W - 1) // 2
    # 对原图和高斯平滑的结果扩充边界
    Ip = cv2.copyMakeBorder(I, cH, cH, cW, cW, borderType)
    Igp = cv2.copyMakeBorder(Ig, cH, cH, cW, cW, borderType)
    # 图像矩阵的行和列
    rows, cols = I.shape
    i, j = 0, 0
    # 联合双边滤波的结果
    jblf = np.zeros(I.shape, np.float64)
    for r in range(cH, cH+rows, 1):
        for c in range(cW, cW+cols, 1):
            # 当前位置的值
            pixels = Igp[r][c]
            # 当前位置的邻域
            rTop, rBottom = r-cH, r+cH
            cLeft, cRight = c-cW, c+cW
            # 从Igp中截取该邻域，用于构建相似性权重模板
            region = Igp[rTop:rBottom+1, cLeft:cRight+1]
            # 通过上述邻域，构建该位置的相似性权重模板
            similarityWeight = np.exp(-0.5 * np.power(region-pixels, 2.0) / math.pow(sigma_d, 2.0))
            # 相似性权重模板和空间距离权重模板相乘
            weight = closenessWeight * similarityWeight
            # 将权重模板归一化
            weight = weight / np.sum(weight)
            # 权重模板和邻域对应位置相乘并相加
            jblf[i][j] = np.sum(Ip[rTop:rBottom+1, cLeft:cRight+1] * weight)
            j += 1
        j = 0
        i += 1
    return jblf

if __name__ == '__main__':
    img = cv2.imread('../Img/0230610170721.png', 0)
    cv2.imshow('src', img)
    # 将8位图转换为浮点型
    fI = img.astype(np.float64)
    # 联合双边滤波，返回值的数据类型为浮点型
    jblf = joinBLF(img, 31, 31, 7, 2)
    # 转换为8位图
    jblf = np.round(jblf)
    jblf = jblf.astype(np.uint8)
    cv2.imshow('jblf', jblf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('../Img/0230610170721.png', 0)
cv2.imshow('src', img)
# 均值平滑
img_mean = cv2.blur(img, (27, 27), borderType=cv2.BORDER_DEFAULT)
cv2.imshow('mean', img_mean)
# 双边滤波
img_bilateral = cv2.bilateralFilter(img, 27, 80, 5, borderType=cv2.BORDER_DEFAULT)
cv2.imshow('bilateral', img_bilateral)
# 联合双边滤波
img_gaussian = cv2.GaussianBlur(img, (27, 27), 80, borderType=cv2.BORDER_DEFAULT)
img_joint = cv2.ximgproc.jointBilateralFilter(img_gaussian, img, 27, 80, 5, borderType=cv2.BORDER_DEFAULT)
cv2.imshow('joint', img_joint)

cv2.waitKey(0)
cv2.destroyAllWindows()
