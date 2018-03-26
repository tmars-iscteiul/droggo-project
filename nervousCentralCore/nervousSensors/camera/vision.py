import cv2
import numpy as np

width = 320
height = 240
interrupted = False

def __init__(self, debug = False):
	inicialSettings()
	self.debug = debug
	start()

def __inicialSettings():
	cap = cv2.VideoCapture(0)

	cap.set(3,width)
	cap.set(4,height)

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
	print("Camera: inicial settings defined with sucess")


def start():
	interrupted = true

	while (cap.isOpened() and not interrupted):

		ret, img_ori = cap.read()

		if ret==True:
			if debug:
				t1 = datetime.now()

			img = cv2.multiply(img_ori/256, color_kernel)
			vision = cv2.add(img, grey)

			cv2.imshow('vision',vision)

			if debug:
				dt = datetime.now() - t1
				print(dt)

def interrupt():
	interrupted = True
	
def stop():
	cap.release()
	cv2.destroyAllWindows()