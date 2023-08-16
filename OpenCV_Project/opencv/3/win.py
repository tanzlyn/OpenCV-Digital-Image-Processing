#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 创建显示窗口
import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',640,480)
cv2.imshow('new',0)
key = cv2.waitKey(0)
if (key == 'q'):
    exit()
cv2.destroyAllWindows()