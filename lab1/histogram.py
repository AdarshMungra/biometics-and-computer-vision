import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('/home/adarsh/PycharmProjects/pythonProject/test1/lab1/face1.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
