import cv2 as cv

print(cv.__version__)

# showing oroginal image
image = cv.imread('test.jpg', cv.IMREAD_COLOR)
cv.imshow('original image', image)
cv.waitKey(0)
cv.destroyAllWindows()

# showing image without blue
image[:, :, 0] = 0
cv.imshow('without blue image', image)
cv.waitKey(0)
cv.destroyAllWindows()

# showing gray scale image
grayImage = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('gray image', grayImage)
cv.waitKey(0)
cv.destroyAllWindows()

