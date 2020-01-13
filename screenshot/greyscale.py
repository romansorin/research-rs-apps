import cv2
import os

def convert_to_greyscale(filename):
    print("Reading: ", filename)
    image = cv2.imread(fr'screenshots/{filename}')
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    status = cv2.imwrite(fr'screenshots/greyscale/{filename}', grey)
    print("Wrote greyscale image to directory: ", status)


for file in os.listdir('screenshots'):
    if file.endswith('.png'):
        convert_to_greyscale(file)
