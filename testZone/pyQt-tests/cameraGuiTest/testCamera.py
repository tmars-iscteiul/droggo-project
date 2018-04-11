import cv2
import numpy as np
from datetime import datetime
from PIL import Image

class Camera():

	width = 320
	height = 240
	grey = np.ones((height, width, 3), np.uint8)
	color_kernel = np.zeros((height, width,3), np.uint8)
	cap = None

	def __init__(self):

		width = self.width
		height = self.height

		self.grey[:,:,:] = (64,64,64)

		max_diagonal = np.power(np.power(np.absolute(width/2),2) + np.power(np.absolute(height/2),2),0.5)

		for i in range(width):
			for j in range(height):
					self.color_kernel[j, i, :] = 255 - 255 * np.power(np.power(np.absolute(i-width/2),2) + 
						np.power(np.absolute(j-height/2),2),0.5)/max_diagonal

		self.color_kernel = self.color_kernel/255
		self.grey = cv2.multiply(1-self.color_kernel, self.grey/255)

	
	def startCapture(self, cam):
		self.cap = cv2.VideoCapture(cam)
		self.cap.set(3,self.width)
		self.cap.set(4,self.height)


	def takeSnapshot(self):
		
		if (self.cap != None):
			if (self.cap.isOpened()):

				ret, img_ori = self.cap.read()

				if ret:

					img = cv2.multiply(img_ori/255, self.color_kernel)
					vision = cv2.add(img, self.grey)

					#visionBGR = vision[...,::-1]
					#visionRGB = cv2.transpose(visionBGR)

					#visionRGB = cv2.cvtColor(visionBGR, cv2.COLOR_BGR2RGB)

					#print(visionRGB[320,240,:])

					cv2.imshow('vision',vision)

					if cv2.waitKey(1) & 0xFF==ord('q'):
						return

					return vision, True
				else:
					return None, False
			return None, False
		return None, False


	def stopCamera(self):
		self.cap.release()



if __name__ == "__main__":
	window = Camera()
	window.startCapture(0)
	
	i = 0
	while i in range(50):
		window.takeSnapshot()
		i = i+1

	window.stopCamera()