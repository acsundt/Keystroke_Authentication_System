from typing import List
from KeystrokeRecorder import KeystrokeRecorder


def collect() -> []:
    recorder = KeystrokeRecorder()
    recorder.start()
    # Collects keystroke data until enter key is pressed
    # Returns said data
    return recorder


def get_password(recorder: List[str]) -> str:
    password = ""
    count = 0
    while count <= len(recorder):
        password += recorder[count][1]
        count += 2
    # Finds password that was collected
    # Returns password
    return password


def transform(recorder: List[str]) -> []:
    i = 0
    numerical_recorder = []
    while i < len(recorder):
        numerical_recorder.append(recorder[i+1][2]-recorder[i][2])
        i += 2
    # Converts recorder into a list of ints
    # Ints are the time the key is pressed/held
    return numerical_recorder






