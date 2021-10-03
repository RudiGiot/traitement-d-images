import cv2 as cv
img = cv.imread('/Users/RudiGiot 1/Dropbox/Programmes/Python/ImageProcessing/testImages/lena.png')
cv.imshow('Lena', img)
cv.waitKey(0)