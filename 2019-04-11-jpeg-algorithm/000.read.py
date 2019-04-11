#!/usr/bin/env python3
import cv2
if __name__ == '__main__':
    dec = cv2.imread("IMG_0108.JPG")
    cv2.imwrite("IMG_0108_recompressed.png", dec)
    