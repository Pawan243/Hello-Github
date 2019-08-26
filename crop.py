import cv2
 
img = cv2.imread("air.jpeg")
 
height, width = img.shape[0:2]
startRow = int(height*.25)
 
startCol = int(width*.25)
 
endRow = int(height*.65)
 
endCol = int(width*.65)

croppedImage = img[startRow:endRow, startCol:endCol]

cv2.imshow('Original Image', img)
 
cv2.imshow('Cropped Image', croppedImage)
 
cv2.waitKey(0)
