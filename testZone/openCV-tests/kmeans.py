import numpy as np
import cv2

import cv2
import numpy as np

x = 640
y = 480

cap = cv2.VideoCapture(1)
cap.set(3,x)
cap.set(4,y)

while(cap.isOpened()):

	ret, img = cap.read()

	if ret==True:
		Z = img.reshape((-1,3))
		# convert to np.float32
		Z = np.float32(Z)

		# define criteria, number of clusters(K) and apply kmeans()
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 8, 1.0)
		K = 4
		ret,label,center=cv2.kmeans(Z,K,None,criteria,8,cv2.KMEANS_RANDOM_CENTERS)

		# Now convert back into uint8, and make original image
		center = np.uint8(center)
		res = center[label.flatten()]
		res2 = res.reshape((img.shape))

		cv2.imshow('res2',res2)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
#out.release()
cv2.destroyAllWindows()