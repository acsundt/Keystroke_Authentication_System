# keystroke_capture.py

import time
from pynput import keyboard


class KeystrokeRecorder:
    def __init__(self):
        self.samples = []

    def on_press(self, key):
        try:
            press_time = time.time()
            self.samples.append(('press', key.char, press_time))
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            release_time = time.time()
            self.samples.append(('release', key.char, release_time))
            if key.char == '\r':
                return False
        except AttributeError:
            pass

    def start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
