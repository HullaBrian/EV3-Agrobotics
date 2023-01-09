#Still a WIP

from pathfinding.objects import findFile

import os
import sys

import cv2
from loguru import logger

hex_mat = findFile("Hex-Mat.jpg")

img = cv2.imread(hex_mat, 1)


if __name__ == '__main__':
    img = cv2.resize(img, (1920, 929))
    cv2.imshow('Image', img)

    #Will destroy window after any key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()