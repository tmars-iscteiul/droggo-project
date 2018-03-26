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

		#blur = cv2.GaussianBlur(imgbw,(3,3),0)
		#ret3,th = cv2.threshold(blur,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

		th = cv2.adaptiveThreshold(imgbw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)
		#thc = cv2.cvtColor(th, cv2.COLOR_GRAY2BGR)

		#blur = cv2.medianBlur(th,3)
		#out.write(thc)

		cv2.imshow('frame',blur)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
#out.release()
cv2.destroyAllWindows()