import cv2
import numpy as np

x = 640
y = 480

cap = cv2.VideoCapture(0)
cap.set(3,x)
cap.set(4,y)

while(cap.isOpened()):

	ret, img = cap.read()

	if ret==True:
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		gray2 = gray
		
		# Initiate STAR detector
		orb = cv2.ORB_create()

		# find the keypoints with ORB
		kp = orb.detect(gray,None)

		# compute the descriptors with ORB
		kp, des = orb.compute(gray, kp)

		# draw only keypoints location,not size and orientation
		gray2 = cv2.drawKeypoints(gray,kp,gray2[(0,255,0), 1])

		cv2.imshow('imagem',gray2)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
#out.release()
cv2.destroyAllWindows()