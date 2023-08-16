#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 使用均值平滑
def adaptive_thresh(image, win_size, ratio=0.15):
    # 对图像矩阵进行均值平滑
    image_mean = cv2.blur(image, win_size)
    # 原图像矩阵与平滑结果做差
    out = image - (1.0-ratio) * image_mean
    # 当差值大于或等于0时，输出值为255，反之输出值为0
    out[out >= 0] = 255
    out[out < 0] = 0
    out = out.astype(np.uint8)
    return out

if __name__ == '__main__':
    img = cv2.imread("../Img/1686814093274.png", 0)
    # 自定义函数
    threshImg = adaptive_thresh(img, (7,7))
    # cv2.imwrite('./images/image3_adaptive.jpg', threshImg)
    # opencv自带函数
    threshImage = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,10)
    cv2.imshow('thresh', threshImg)
    cv2.imshow('threshImage',threshImage)
    cv2.waitKey()
