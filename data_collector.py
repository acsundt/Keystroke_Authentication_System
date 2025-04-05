from typing import List
from KeystrokeRecorder import KeystrokeRecorder
import pandas as pd
import numpy as np

def collect(class_type) -> []:
    recorder = KeystrokeRecorder()
    recorder.start()
    # Collects keystroke data until enter key is pressed
    # Returns said data
    return recorder.append(class_type)


def collect_training(class_type) -> []:
    training_data = []
    print("Keep repeating the password. Hit Enter to stop.")
    # print("The more times you repeat it the stronger the security.")
    # Class_type is either 1 or 0, 0 for false, 1 for true
    # 1 means that the password is inputted by the correct user, 0 for otherwise
    training_data.append(collect(class_type))
    # Collects many samples and returns 2D list
    return training_data


def combine_classifications(training_false,training_true):
    training = training_false + training_true
    return training


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
    # Returns a 2D array of numerical data
    return transformed_data


def transform(recorder: List[str]) -> []:
    i = 0
    numerical_recorder = []
    while i < len(recorder):
        numerical_recorder.append(recorder[i+1][2]-recorder[i][2])
        numerical_recorder.append(recorder[3])
        i += 2
    # Converts recorder into a list of ints
    # Ints are the time the key is pressed/held
    return numerical_recorder






