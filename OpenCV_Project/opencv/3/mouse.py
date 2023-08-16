#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# 定义鼠标回调函数
def mouse_callback(event,x,y,flags,underdata):
    # if event == cv2.EVENT_LBUTTONDBLCLK:
        # cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
    print(event,x,y,flags,underdata)


# 创建窗口
cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse',640,360)

# 设置回调函数
cv2.setMouseCallback('mouse',mouse_callback,'123')

#显示窗口和背景
img = np.zeros((360,640,3),np.uint8)
while True:
    cv2.imshow('mouse',img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()