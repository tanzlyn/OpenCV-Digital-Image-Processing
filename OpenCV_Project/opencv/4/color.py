#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2

# 步骤
# 1.创建窗口
# 2.读取图片
# 3.创建一个TrackBar
# 4.循环：色彩空间转换API，通过数组索引，读取不同的值
# 5.显示不同的图像


def callback():
    pass

cv2.namedWindow('color',cv2.WINDOW_NORMAL)

img = cv2.imread('../Guangzhou.jfif')

colorspaces = [cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HSV_FULL,cv2.COLOR_BGR2YUV]
cv2.createTrackbar('curcolor','color',0,len(colorspaces),callback)
while True:
    index = cv2.getTrackbarPos('curcolor','color')
    # 颜色空间转换
    cvt_img = cv2.cvtColor(img,colorspaces[index])
    cv2.imshow('color',cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

