import cv2 as cv

print(cv.__version__)

# showing oroginal image
image = cv.imread('test.jpg')
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

# blurring gray scale image with guassian blur
blurImage = cv.GaussianBlur(grayImage, (9, 9), 5)
cv.imshow('gray blur image', blurImage)
cv.waitKey(0)
cv.destroyAllWindows()

# scaling image
image = cv.imread('test.jpg')
height, width = image.shape[:2]
resizedImage = cv.resize(image, (width / 2, height), interpolation=cv.INTER_CUBIC)
cv.imshow('resized image', resizedImage)
cv.waitKey(0)
cv.destroyAllWindows()