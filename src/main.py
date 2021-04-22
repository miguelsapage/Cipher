"""
This program is a simple encryption tool

Author: Miguel Sapage
"""

from save import Save
from encrypt import Encrypt

def main():
	msg = input('Message to encrypt: ')

	save = Save()
	save_choice = save.interact()

	encrypt = Encrypt(msg)
	result = encrypt.output_msg()

	if save_choice == 'copy':
		save.copy_to_clipboar(result)
	elif save_choice == 'file':
		save.save_to_file(result)
	elif save_choice == 'both':
		save.copy_to_clipboar(result)
		save.save_to_file(result)

main()