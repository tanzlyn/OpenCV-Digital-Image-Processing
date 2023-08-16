#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 图片显示与保存
import cv2
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',640,480)
img = cv2.imread("E:/images/51d415129c45d12c9fb4e01880ebc3e3.jpg")

while True:

    cv2.imshow('img',img)

    key = cv2.waitKey(0)

    if (key & 0xFF == ord('q')):
        break
    elif(key & 0xFF == ord('s')):
        cv2.imwrite("E:/images/123.png",img)
    else:
        print(key)

cv2.destroyAllWindows()