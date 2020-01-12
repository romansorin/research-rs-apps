import cv2

image = cv2.imread('./screenshots/airbnb.png')
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Grey image', grey)
print("Showing color/grey images. Press 0 to exit..")

cv2.waitKey(0)
cv2.destroyAllWindows()