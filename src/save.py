from graphics import *
from button import Button
from pyperclip import copy

class Save:
	def __init__(self):
		self.win = GraphWin('Save', 200, 200)
		Text(Point(100, 30), 'How do you want to').draw(self.win)
		Text(Point(100, 45), 'save the message?').draw(self.win)

		self.copy = Button(self.win, Point(100, 95), 130, 25, 'Copy to clipboard')
		self.file = Button(self.win, Point(100, 125), 130, 25, 'Save to text file')
		self.both = Button(self.win, Point(100, 155), 55, 25, 'Both')
		self.copy.activate()
		self.file.activate()
		self.both.activate()

	def interact(self):
		while True:
			click = self.win.getMouse()
			if self.copy.clicked(click):
				self.win.close()
				return 'copy'
			elif self.file.clicked(click):
				self.win.close()
				return 'file'
			elif self.both.clicked(click):
				self.win.close()
				return 'both'

	def copy_to_clipboar(self, result):
		copy(result)

	def save_to_file(self, result):
		with open('Messages.txt', 'a') as file:
			file.write(result + '\n')