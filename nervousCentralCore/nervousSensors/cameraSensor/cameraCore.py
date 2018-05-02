import cv2
import numpy as np

class Camera():

	width = 640
	height = 480
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

	
	def startSight(self, cam):
		self.cap = cv2.VideoCapture(cam)
		self.cap.set(3,self.width)
		self.cap.set(4,self.height)


	def getSight(self, showVision):
		
		if (self.cap != None):
			if (self.cap.isOpened()):

				ret, img_ori = self.cap.read()

				if ret:

					img = cv2.multiply(img_ori/255, self.color_kernel)
					vision = cv2.add(img, self.grey)

					if showVision:
						cv2.imshow('vision',vision)

					if cv2.waitKey(10) & 0xFF==ord('q'):
						self.stopVision()
						return None, False

					return vision, True

		return None, False


	def stopVision(self):
		self.cap.release()



if __name__ == "__main__":
	vision = Camera()
	vision.startSight(0)
	
	active = True
	while active:
		_, active = vision.getSight(True)

	if (vision.cap.isOpened()):
		vision.stopCamera()