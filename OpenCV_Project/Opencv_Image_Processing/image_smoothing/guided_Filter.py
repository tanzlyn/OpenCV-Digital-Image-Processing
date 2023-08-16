#!/user/bin/env python3
# -*- coding: utf-8 -*-
import math
import cv2 as cv
import numpy as np


def guidedFilter(I, p, winSize, eps):
    # 输入图像的高，宽
    rows, cols = I.shape
    # I的均值平滑
    mean_I = cv.blur(I, winSize, borderType=cv.BORDER_DEFAULT)
    # p的均值平滑
    mean_p = cv.blur(p, winSize, borderType=cv.BORDER_DEFAULT)
    # I .* p 的均值平滑
    Ip = I * p
    mean_Ip = cv.blur(Ip, winSize, borderType=cv.BORDER_DEFAULT)
    # 协方差
    cov_Ip = mean_Ip - mean_I * mean_p
    mean_II = cv.blur(I * I, winSize, borderType=cv.BORDER_DEFAULT)
    # 方差
    var_I = mean_II - mean_I * mean_I
    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I
    # 对a和b进行均值平滑
    mean_a = cv.blur(a, winSize, borderType=cv.BORDER_DEFAULT)
    mean_b = cv.blur(b, winSize, borderType=cv.BORDER_DEFAULT)
    q = mean_a * I + mean_b
    return q


if __name__ == '__main__':
    image = cv.imread('../Img/1686489684079.jpg', 0)
    # 将图像进行归一化
    image_0_1 = image / 255.0
    # 显示原图
    cv.imshow('image', image)
    # 导向滤波
    result = guidedFilter(image_0_1, image_0_1, (9, 9), math.pow(0.2, 2.0))
    cv.imshow('guidedFilter', result)
    # 细节增强
    result_enhanced = (image_0_1 - result) * 5 + result
    result_enhanced = cv.normalize(result_enhanced, result_enhanced, 1, 0, cv.NORM_MINMAX)
    cv.imshow('result_enhanced', result_enhanced)
    # 保存导向滤波的结果
    result = result * 255
    result[result > 255] = 255
    result = np.round(result)
    result = result.astype(np.uint8)
    cv.imwrite('guidedFilter.jpg', result)
    cv.waitKey(0)
    cv.destroyAllWindows()
