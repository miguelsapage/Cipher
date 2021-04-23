from random import randrange

class Encrypt:
	def __init__(self, msg):
		self.msg = msg

	def output_msg(self):
		encrypted = ''
		for character in self.msg:
			encrypted += self.encrypt_msg(character)
		return encrypted

	def encrypt_msg(self, character, shift = 3):
		if 97 <= ord(character) <= 122:
			return chr(- (ord(character) - 110) + 109)
		elif 65 <= ord(character) <= 90:
			return chr(- (ord(character) - 78) + 77)
		elif 48 <= ord(character) <= 57:
			return chr((ord(character) + shift - 48) % 10 + 48)
		elif ord(character) == 32:
			return chr(randrange(35, 39))
		else:
			return character