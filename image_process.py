import cv2
import numpy as np
import matplotlib.pyplot as plt

def drawRectangle(img):
    upperLeft_point = (294, 183)
    lowerRight_point = (412, 228)
    color = (0, 255, 0)
    width = 2
    img_rectangle = cv2.rectangle(img, upperLeft_point, lowerRight_point, color, width)
    img_rectangle = cv2.rectangle(img_rectangle, (754, 186), (986, 318),(255, 0, 0), 2)
    cv2.imshow('draw rectangle', img_rectangle)
    cv2.waitKey(0)

def writeText(img):
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (0, 100)
    fontScale = 2
    fontColor = (0, 0, 255)
    lineType = 2
    img_text = cv2.putText(img, 'Hello World!', position, font, fontScale, fontColor, lineType)
    cv2.imshow("write text", img_text)
    cv2.waitKey(0)

def get_image_gradient(img_RGB):
    img_gray = cv2.cvtColor(img_RGB, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize = 5)
    sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize = 5)

    plt.subplot(1, 3, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.subplot(1, 3, 2)
    plt.imshow(sobelx, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.imshow(sobely, cmap='gray')
    plt.show()

def canny_edge_detector(img_RGB):
    img_gray = cv2.cvtColor(img_RGB, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img_gray, 100, 200)

    plt.subplot(121)
    plt.imshow(img_gray,cmap='gray')
    plt.subplot(122)
    plt.imshow(edges, cmap='gray')
    plt.show()

def blur_image(img_RGB):
    img_blured = cv2.GaussianBlur(img_RGB, (7, 7), 0)
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img_RGB, cv2.COLOR_BGR2GRAY))
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img_blured, cv2.COLOR_BGR2GRAY))
    plt.show()

if __name__ == "__main__":
    img = cv2.imread("kitty_left.png")
    #drawRectangle(img)
    #writeText(img)
    #get_image_gradient(img)
    #canny_edge_detector(img)
    blur_image(img)
