import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('all.jpg')
edge = cv2.Canny(img, 100, 200)

file=open('all.txt','w')


ans = []
for y in range(0, edge.shape[0]):
    for x in range(0, edge.shape[1]):
        if edge[y, x] != 0:
            file.write(str(x)+"\t"+str(y)+"\n")
            ans = ans + [[x, y]]
file.close()
