from graphics import *
from button import Button

class Choice:
	def __init__(self):
		self.win = GraphWin('Choice', 150, 100)

		self.encrypt = Button(self.win, Point(75, 32), 75, 25, 'Encrypt')
		self.decrypt = Button(self.win, Point(75, 68), 75, 25, 'Decrypt')
		self.encrypt.activate()
		self.decrypt.activate()

	def interact(self):
		while True:
			click = self.win.getMouse()
			if self.encrypt.clicked(click):
				self.win.close()
				return 'encrypt'
			elif self.decrypt.clicked(click):
				self.win.close()
				return 'decrypt'