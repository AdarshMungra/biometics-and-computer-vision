import cv2
import matplotlib.pyplot as plt
 

im = cv2.imread('plate.jpg')

edges = cv2.Canny(im,25,255,L2gradient=False)

plt.imshow(edges,cmap='gray')

plt.show()