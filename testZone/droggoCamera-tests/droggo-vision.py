import cv2
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

width = int(cap.get(3))
height = int(cap.get(4))

grey = np.ones((height, width, 3), np.uint8)
grey[:,:,:] = (64,64,64)

color_kernel = np.zeros((height, width,3), np.uint8)

max_diagonal = np.power(np.power(np.absolute(width/2),2) + np.power(np.absolute(height/2),2),0.5)
border = int(max_diagonal / 10)

for i in range(width):
	for j in range(height):
			color_kernel[j, i, :] = 255 * (max_diagonal - np.power(np.power(np.absolute(i-width/2),2) + 
				np.power(np.absolute(j-height/2),2),0.5))/max_diagonal

color_kernel = color_kernel/255
grey = cv2.multiply(1-color_kernel, grey/256)

while (cap.isOpened()):

	ret, img_ori = cap.read()

	if ret==True:
		t1 = datetime.now()
		
		img = cv2.multiply(img_ori/256, color_kernel)
		vision = cv2.add(img, grey)

		cv2.imshow('vision',vision)

		t2 = datetime.now()

		dt = t2 - t1
		print(dt)

		if cv2.waitKey(1) & 0xFF==ord('q'):
			break

	else:
		break

cap.release()
cv2.destroyAllWindows()