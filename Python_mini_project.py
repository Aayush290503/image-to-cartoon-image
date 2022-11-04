import cv2
import numpy as numpy
from tkinter.filedialog import *

photo = askopenfilename()
img = cv2.imread(photo)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)#The Bilateral Filter operation applies a bilateral image to a filter
cartoon = cv2.bitwise_and(color, color, mask = edges)
''' Whenever we are dealing with images while
 solving computer vision problems, there arises a necessity to manipulate
 the given image or extract parts of the given image based on the requirement,
 in such cases we make use of bitwise operators'''

cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)

#save
cv2.imwrite("hd_wallpaper.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows
