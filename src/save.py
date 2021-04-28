from graphics import *
from button import Button
from pyperclip import copy
from easygui import diropenbox
from pathlib import Path
from datetime import datetime
from os import system

class SaveEncryption:
	def __init__(self):
		#GUI to choose how to save the encrypted text
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
		#The user choose where to save the file
		if Path('path.txt').is_file():
			with open('path.txt', 'r') as path_file:
				path = path_file.read()
			path_file.close()
			with open(path + '/Messages.txt', 'a') as file:
				file.write(result + '\n') #Each new message will be written to new line
			file.close()
		else:
			path = diropenbox()
			with open('path.txt', 'w') as path_file:
				path_file.write(path)
			with open(path + '/Messages.txt', 'a') as file:
				file.write(result + '\n')

class SaveDecryption:
	def __init__(self, result):
		self.result = result

	def save_to_hidden_file(self):
		#Save to hidden file in location of users choice
		path = diropenbox()
		now = self.now_time()
		with open(path + '\\' + now + '.txt', 'w') as file:
			file.write(self.result)
		system('attrib +h ' + '"' + file.name + '"')

	def now_time(self):
		#Formats the file name
		now_str = str(datetime.now())[:19]
		date_list = list(now_str.replace(':', ""))
		date_list.insert(13, 'h')
		date_list.insert(16, 'm')
		date_list.insert(19, 's')
		now = ''.join(date_list)
		return now