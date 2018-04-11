import cv2
import numpy as np
from datetime import datetime

class Camera():
	cap = None
	width = 640
	height = 480

	grey = np.ones((height, width, 3), np.uint8)
	color_kernel = np.zeros((height, width,3), np.uint8)

	def __init__(self):
		width = self.width
		height = self.height

		#grey = np.ones((height, width, 3), np.uint8)
		#color_kernel = np.zeros((height, width,3), np.uint8)
		
		self.grey[:,:,:] = (64,64,64)

		max_diagonal = np.power(np.power(np.absolute(width/2),2) + np.power(np.absolute(height/2),2),0.5)

		for i in range(width):
			for j in range(height):
					self.color_kernel[j, i, :] = 255 * (max_diagonal - np.power(np.power(np.absolute(i-width/2),2) + 
						np.power(np.absolute(j-height/2),2),0.5))/max_diagonal

		self.color_kernel = self.color_kernel/255
		self.grey = cv2.multiply(1-self.color_kernel, self.grey/256)

	
	def startCapture(self):
		self.cap = cv2.VideoCapture(1)

		self.cap.set(3,self.width)
		self.cap.set(4,self.height)


	def capture(self):
		while (self.cap.isOpened()):

			self.takePic()

			if cv2.waitKey(1) & 0xFF==ord('q'):
				break

		self.cap.release()
		cv2.destroyAllWindows()


	def takePic(self):
		ret, img_ori = self.cap.read()

		if ret==True:
			t1 = datetime.now()

			img = cv2.multiply(img_ori/256, self.color_kernel)
			vision = cv2.add(img, self.grey)

			cv2.imshow("image", vision)

			t2 = datetime.now()

			dt = t2 - t1
			print(dt)


cam = Camera()
cam.startCapture()
cam.capture()

