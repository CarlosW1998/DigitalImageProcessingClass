# Computes the subtraction between the two images to 
# locate differences between them, such as finding a dislocated coin.
import cv2  
import numpy as np  

image1 = cv2.imread('star-1-300x168.jpg')  
image2 = cv2.imread('dot-300x168.jpg') 
  
sub = cv2.subtract(image1, image2) 
  
cv2.imshow('Subtracted Image', sub) 

#out whit del key 
if cv2.waitKey(3014656) :  
    cv2.destroyAllWindows() 