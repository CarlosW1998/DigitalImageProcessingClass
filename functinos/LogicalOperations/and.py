#Logical Operations AND
import cv2

image1 = cv2.imread('1bit1.png')  
image2 = cv2.imread('2bit2.png') 

dest_and = cv2.bitwise_and(image1, image2, mask = None) 

cv2.imshow('Bitwise And', dest_and) 

#out whit del key 
if cv2.waitKey(3014656) :  
    cv2.destroyAllWindows() 