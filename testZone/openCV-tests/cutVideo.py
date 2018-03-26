import cv2
import numpy as np

cap = cv2.VideoCapture(1)
x = 10
y = 10

while(cap.isOpened()):

    # Take each frame
	_, frame = cap.read()

	M = np.float32([[1,0,x],[0,1,y]])
	dst = cv2.warpAffine(frame,M,(500,500))

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

