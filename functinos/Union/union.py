#Logical Operations AND
import cv2

image1 = cv2.imread('union1.jpg')  
image2 = cv2.imread('union2.jpg') 

dest_and = cv2.max(image1, image2) 

cv2.imshow('Bitwise And', dest_and) 

#out whit del key 
if cv2.waitKey(3014656) :  
    cv2.destroyAllWindows() 