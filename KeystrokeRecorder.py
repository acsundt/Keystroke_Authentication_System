from pynput import keyboard
import time


class KeystrokeRecorder:
    def __init__(self):
        self.samples = []

    def on_press(self, key):
        try:
            # Skip Shift and Enter keys
            if key != keyboard.Key.shift and key != keyboard.Key.shift_l and key != keyboard.Key.shift_r and key != keyboard.Key.enter:
                press_time = time.time()
                self.samples.append(('press', key.char, press_time))
        except AttributeError:
            pass  # Ignore non-character keys (like Shift, Enter, etc.)

    def on_release(self, key):
        try:
            release_time = time.time()
            # Skip Shift and Enter keys
            if key != keyboard.Key.shift and key != keyboard.Key.shift_l and key != keyboard.Key.shift_r and key != keyboard.Key.enter:
                key_name = key.char
            else:
                return False  # Stop the listener if Shift or Enter is pressed/released
        except AttributeError:
            key_name = str(key)  # For special keys

        self.samples.append(('release', key_name, release_time))

        # Stop the listener when Shift or Enter is pressed/released
        if key == keyboard.Key.shift or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r or key == keyboard.Key.backspace:
            return False

    def start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def append(self, class_type):
        self.samples.append(class_type)
