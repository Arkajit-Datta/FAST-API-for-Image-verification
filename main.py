import cv2
import numpy as np

def main(path):
    original_image = cv2.imread("images\original_golden_bridge.jpg")
    image_for_checking = cv2.imread(path)

    #checking if the images are equal
    if original_image.shape == image_for_checking.shape:
        print("Images have equal shapes !!!......")
        print("Checking further.....")

        #finding out the difference in the image
        #If the images are the exact same then we should get a black image through which we can conclude that the images are same
        difference = cv2.subtract(original_image,image_for_checking)
        b, g, r = cv2.split(difference) #as the images are coloured it has three levels, blue,green and red

        blue_colour_difference = cv2.countNonZero(b)
        green_colour_difference = cv2.countNonZero(g)
        red_colour_difference = cv2.countNonZero(r)

        if blue_colour_difference==0 and green_colour_difference==0 and red_colour_difference==0:
            print("Images are SAME!!......")
            return True
        else:
            print("Images are NOT SAME!!......")
            return False
    else:
        print("Images are NOT SAME!!......")
        return False