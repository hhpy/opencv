#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# From: https://zhuanlan.zhihu.com/p/24425116

# 存取图像

# 读图像用cv2.imread()，可以按照不同模式读取，一般最常用到的是读取单通道灰度图，或者直接默认读取多通道。
# 存图像用cv2.imwrite()，注意存的时候是没有单通道这一说的，根据保存文件名的后缀和当前的array维度，OpenCV自动判断存的通道，另外压缩格式还可以指定存储质

import numpy as np
import cv2
import matplotlib.pyplot as plt

# 图6-1中的矩阵
img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)

# 用matplotlib存储
plt.imsave('tmp/img_pyplot.jpg', img)

# 用OpenCV存储
cv2.imwrite('tmp/img_cv2.jpg', img)