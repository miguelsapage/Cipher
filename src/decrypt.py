class Decrypt:
	def __init__(self, encrypted_msg):
		self.encrypted_msg = encrypted_msg

	def output_msg(self):
		decrypted = ''
		for character in self.encrypted_msg:
			decrypted += self.decrypt_msg(character)
		return decrypted

	def decrypt_msg(self, character, shift = 3):
		if 97 <= ord(character) <= 122:
			return chr(- (ord(character) - 110) + 109)
		elif 65 <= ord(character) <= 90:
			return chr(- (ord(character) - 78) + 77)
		elif 48 <= ord(character) <= 57:
			return chr((ord(character) - shift - 48) % 10 + 48)
		elif 35 <= ord(character) <= 38:
			return chr(32)
		else:
			return character
