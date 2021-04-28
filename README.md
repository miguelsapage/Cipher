# Cipher
This is a simple encryption and decryption tool

## How does the encryption works?
The alphabet is mirrored and the numbers are shifted by some quantity (3 by default).
The spaces translates to #, $, % or &.
Every other character remains the same.

## Save encrypted text
The user can save the encrypted text to the clipboard, to a file or both, to be sent later if needed.

## Save decrypted text
The decrypted text will be saved to a hidden file named with the date and time.
The location to save is chosen by the user.

## External modules
The program uses **graphics.py** and **button.py** from John M. Zelle. (Function added to button.py). In addition it uses the module **pyperclip** from Al Sweigart and the module **easygui**.