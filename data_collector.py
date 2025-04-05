from typing import List
from KeystrokeRecorder import KeystrokeRecorder
import pandas as pd
import numpy as np

def collect() -> []:
    recorder = KeystrokeRecorder()
    recorder.start()
    # Collects keystroke data until enter key is pressed
    # Returns said data
    return recorder


def collect_training() -> []:
    training_data = []
    print("Keep repeating your password until you want to stop. Simply don't type anything to stop.")
    print("The more times you repeat it the stronger the security.")
    training_data.append(collect())
    # Collects many samples and returns 2D list
    return training_data


def training_to_df(training_data, password):
    # Training_data is transformed_data
    password_split = list(password)
    df = pd.DataFrame(training_data, columns=password_split)
    # Fills the data frame with the numerical data in each row
    # Uses each letter of the password as a column
    return df


def get_password(recorder: List[str]) -> str:
    password = ""
    count = 0
    while count <= len(recorder):
        password += recorder[count][1]
        count += 2
    # Finds password that was collected
    # Returns password
    return password


def transform_data(training_data):
    transformed_data = []
    for ls in training_data:
        transformed_data.append(transform(ls))
    return transformed_data


def transform(recorder: List[str]) -> []:
    i = 0
    numerical_recorder = []
    while i < len(recorder):
        numerical_recorder.append(recorder[i+1][2]-recorder[i][2])
        i += 2
    # Converts recorder into a list of ints
    # Ints are the time the key is pressed/held
    return numerical_recorder






