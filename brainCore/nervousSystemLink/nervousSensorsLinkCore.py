class NervousSensorsLink():

	eyes = None
	battery = None
	motion = None
	upperLaser = None
	downLaser = None
	leftLaser = None
	rightLaser = None
	backLaser = None
	leftEar = None
	rightEar = None

	def __init__ (self, nervousSystem):
		eyes = nervousSystem.getEyes()
		#battery = nervousSystem.getBattery()
		#motion = nervousSystem.getMotion()
		#upperLaser = nervousSystem.getUpperLaser()
		#downLaser = nervousSystem.getDownLaser()
		#leftLaser = nervousSystem.getLeftLaser()
		#rightLaser = nervousSystem.getRightLaser()
		#backLaser = nervousSystem.getBackLaser()
		#leftEar = nervousSystem.getLeftEar()
		#rightEar = nervousSystem.getRightEar()


	def getEyes(self):
		return eyes.getSight()
