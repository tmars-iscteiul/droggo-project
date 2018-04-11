import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QDesktopWidget, QFrame, QTextEdit, QLabel, QLineEdit, QListWidget, QMainWindow
from PyQt5.QtGui import QIcon, QColor, QPixmap, QFont
from PyQt5.QtCore import QTimer
import time

class MainWindow(QMainWindow):
    
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.resize(1000, 650)
		self.move(100,10)
		self.setWindowTitle('Droggo')
		self.setWindowIcon(QIcon('../zbrand/icon.png'))

		actionLbl = QLabel("Action status:",self)
		actionLbl.setFont(QFont('Arial', 12))
		actionLbl.move(660,10)

		searchingActionBtn = QPushButton('Searching for objects',self)
		searchingActionBtn.setFont(QFont('Arial', 12))
		searchingActionBtn.resize(165,40)
		searchingActionBtn.move(660,50)
		searchingActionBtn.setEnabled(True)

		checkingActionBtn = QPushButton('Checking the object',self)
		checkingActionBtn.setFont(QFont('Arial', 12))
		checkingActionBtn.resize(165,40)
		checkingActionBtn.move(660,100)
		checkingActionBtn.setEnabled(False)

		learningActionBtn = QPushButton('Learning the object',self)
		learningActionBtn.setFont(QFont('Arial', 12))
		learningActionBtn.resize(165,40)
		learningActionBtn.move(830,50)
		learningActionBtn.setEnabled(False)

		confirmingActionBtn = QPushButton('Confirming the object',self)
		confirmingActionBtn.setFont(QFont('Arial', 12))
		confirmingActionBtn.resize(165,40)
		confirmingActionBtn.move(830,100)
		confirmingActionBtn.setEnabled(False)

		interactionLbl = QLabel("Interaction console:",self)
		interactionLbl.setFont(QFont('Arial', 12))
		interactionLbl.resize(200,30)
		interactionLbl.move(660,160)

		interaction = QListWidget(self)
		interaction.resize(330,150)
		interaction.move(660,190)

		inputDialog = QLineEdit(self)
		inputDialog.setFont(QFont('Arial', 11))
		inputDialog.resize(230,30)
		inputDialog.move(660,350)

		sendBtn = QPushButton('Send',self)
		sendBtn.setFont(QFont('Arial', 12))
		sendBtn.resize(90,30)
		sendBtn.move(900,350)

		objectListLbl = QLabel("Learn objects tree:",self)
		objectListLbl.setFont(QFont('Arial', 12))
		objectListLbl.resize(200,30)
		objectListLbl.move(660,390)

		objectList = QListWidget(self)
		objectList.resize(330,220)
		objectList.move(660,420)

		thoughtsLbl = QLabel("Droggo thoughts console:",self)
		thoughtsLbl.setFont(QFont('Arial', 12))
		thoughtsLbl.resize(200,30)
		thoughtsLbl.move(10,490)

		thoughts = QListWidget(self)
		thoughts.resize(640,120)
		thoughts.move(10,520)

		self.show()

		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.updateState)
		self.timer.start()

	def updateState(self):
		pass


class App():

	def __init__(self):

		app = QApplication([])
		self.window = MainWindow()
		app.exec_()

	def getWindow(self):
		return self.window

if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	sys.exit(app.exec_())