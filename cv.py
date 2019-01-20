import cv2 as cv

print(cv.__version__)

image = cv.imread('test.jpg', cv.IMREAD_COLOR)
cv.imshow('original image', image)
cv.waitKey(0)
cv.destroyAllWindows()
grayImage = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('gray image', grayImage)
cv.waitKey(0)
