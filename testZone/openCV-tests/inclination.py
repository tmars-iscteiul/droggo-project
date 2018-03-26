import cv2
import numpy as np

cap = cv2.VideoCapture(1)
x = 10
y = 100

while(cap.isOpened()):

    # Take each frame
	_, img = cap.read()

	pts1 = np.float32([[50,50],[200,50],[50,200]])
	pts2 = np.float32([[x,y],[200,50],[100,250]])

	M = cv2.getAffineTransform(pts1,pts2)

	dst = cv2.warpAffine(img,M,(800,500))

	cv2.imshow('img',dst)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	if k == ord('d'):
		x = x + 10
	if k == ord('a'):
		x = x - 10
	if k == ord('w'):
		y = y - 10
	if k == ord('s'):
		y = y + 10

cv2.destroyAllWindows()
