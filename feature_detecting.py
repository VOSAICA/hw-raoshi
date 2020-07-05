import cv2
import numpy as np
import matplotlib.pyplot as plt

def feature_detecting_harris(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    harrisDetector = cv2.cornerHarris(img_gray, 2, 3, 0.04)

    img[harrisDetector > 0.01*harrisDetector.max()] = [0, 0, 255]
    cv2.imshow('dst', img)
    cv2.waitKey(0)

def feature_matching_orb(img1, img2):
    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key = lambda x:x.distance)

    img_match = cv2.drawMatches(img1, kp1, img2, kp2, matches[0:100], None)

    img_match_rgb = cv2.cvtColor(img_match, cv2.COLOR_BGR2RGB)
    plt.imshow(img_match_rgb)
    plt.show()

if __name__ == "__main__":
    img1 = cv2.imread("kitty_left.png")
    img2 = cv2.imread("kitty_right.png")
    #feature_detecting_harris(img1)
    feature_matching_orb(img1, img2)