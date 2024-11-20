import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread("image.jpg")
cv.imshow("Imagen Original",image)

imgGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Imagen Gray",imgGray)

LTresh = 50
UTresh = 150

imgCanny = cv.Canny(imgGray, LTresh, UTresh)
cv.imshow("Imagen Canny",imgCanny)

cv.imwrite('Imagen Canny.jpg', imgCanny)

cv.waitKey(0)
cv.destroyAllWindows()