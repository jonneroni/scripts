
"""Open a console terminal showing cursor position
   Pressing Enter will copy the current position to clipboard
   Ctrl+C will exit the program
"""

#! python3
import os
import keyboard
import pyautogui
import pyperclip

cmd = 'mode 23,5'
os.system(cmd)
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        if keyboard.is_pressed('enter'):
            print("\nCOPIED")
            pyperclip.copy(str(x) + "," + str(y))
            spam = pyperclip.paste()
except KeyboardInterrupt:
    print('\n')
