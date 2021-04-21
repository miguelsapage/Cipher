"""
This program is a simple encryption tool

Author: Miguel Sapage
"""

from save import Save

def main():
	msg = input('Message to encrypt: ')

	save = Save()
	save_choice = save.interact()

main()