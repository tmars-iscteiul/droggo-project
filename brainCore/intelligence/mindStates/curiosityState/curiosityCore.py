import stateEnum as state
import stateCycle

class CuriousState():

	currentState=None
	active=None
	nervousSensor=None

	def __init__(self, intelligenceObject):
		self.currentState = state.SEARCHING
		self.active = True
		self.nervousSensor=intelligenceObject.getCameraSensor()


	def run(self):
		while(active):
			pass

	def setState(self,state):
		self.currentState = state

	def getState(self):
		return self.currentState

	def isActive():
		return self.active;

	def activate():
		self.active = True

	def desactivate():
		self.active = False