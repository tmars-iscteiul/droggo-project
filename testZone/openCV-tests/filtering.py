import cv2
import numpy as np

x = 1280
y = 720

cap = cv2.VideoCapture(0)
cap.set(3,x)
cap.set(4,y)

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('muito_fixe.mp4',fourcc, 24.0, (x,y))

while(cap.isOpened()):

	ret, img = cap.read()

	if ret==True:
		imgbw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		th = cv2.adaptiveThreshold(imgbw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

		#kernel = np.ones((3,3),np.uint8)
		#dilation = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)

		cv2.imshow('frame',th)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
#out.release()
cv2.destroyAllWindows()