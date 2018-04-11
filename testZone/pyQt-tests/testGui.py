import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QDesktopWidget, QFrame, QTextEdit, QLabel, QLineEdit, QListWidget
from PyQt5.QtGui import QIcon, QColor, QPixmap, QFont
from PyQt5.QtCore import QRunnable, QThreadPool
import time

class Worker(QRunnable):

	@pyqtSlot()
	def run(self):
        '''
        Your code goes in this function
        '''
		print("Thread start") 
		time.sleep(5)
		print("Thread complete")


class MainWindow(QMainWindow):
    
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.threadpool = QThreadPool()
		print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

		self.resize(1000, 650)
		self.move(100,10)
		self.setWindowTitle('Droggo')
		#self.setWindowIcon(QIcon('icon.png'))

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
		interactionLbl.move(660,165)

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
		objectListLbl.move(660,395)

		objectList = QListWidget(self)
		objectList.resize(330,220)
		objectList.move(660,420)

		thoughtsLbl = QLabel("Droggo thoughts console:",self)
		thoughtsLbl.setFont(QFont('Arial', 12))
		thoughtsLbl.move(10,495)

		thoughts = QListWidget(self)
		thoughts.resize(640,120)
		thoughts.move(10,520)

		self.show()

		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.updateImage)
		self.timer.start()

	def updateImage(self):
		print("teste")
		worker = Worker()
		self.threadpool.start(worker)
	

app = QApplication([])
window = MainWindow()
app.exec_()