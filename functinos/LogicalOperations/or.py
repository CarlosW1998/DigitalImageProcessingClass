#Logical Operations OR
import cv2  
import numpy as np  

image1 = cv2.imread('1bit1.png')  
image2 = cv2.imread('2bit2.png') 

dest_or = cv2.bitwise_or(image2, image1, mask = None) 

cv2.imshow('Bitwise OR', dest_or) 

#out whit del key 
if cv2.waitKey(3014656) :  
    cv2.destroyAllWindows() 