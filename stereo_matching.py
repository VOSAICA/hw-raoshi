import cv2
import matplotlib.pyplot as plt

imgL = cv2.imread("kitty_left.png")
imgR = cv2.imread("kitty_right.png")

imgL_rgb = cv2.cvtColor(imgL, cv2.COLOR_BGR2RGB)
imgR_rgb = cv2.cvtColor(imgR, cv2.COLOR_BGR2RGB)
plt.imshow(imgL_rgb)
#plt.show()

imgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
imgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=5)
disparity = stereo.compute(imgL, imgR)

plt.imshow(disparity, 'gray')
plt.show()
