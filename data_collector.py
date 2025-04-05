from typing import List
from KeystrokeRecorder import KeystrokeRecorder
import pandas as pd
import numpy as np


def collect(class_type) -> []:
    recorder = KeystrokeRecorder()
    recorder.start()  # Collects keystrokes until the shift key is pressed (for example)
    recorder.samples.append(class_type)
    print(recorder.samples)

    return recorder  # Return the raw keystroke data


def collect_predict() -> []:
    recorder = KeystrokeRecorder()
    recorder.start()  # Collect keystrokes for prediction
    recorder_transformed = transform(recorder.samples)  # Transform data
    return recorder_transformed


def collect_training(class_type) -> []:
    training_data = []
    print("Keep repeating the password. Hit Enter to stop.")
    recorder = collect(class_type).samples
    training_data.append(recorder)
    print("TRAINING DATA:", training_data)# Collect multiple samples of the password
    return training_data


def combine_classifications(training_false, training_true):
    return training_false + training_true  # Combine the two sets of training data


def training_to_df(training_data, password):
    password_split = list(password)
    print("training data", training_data)
    print("password split:", password_split)# Split password into individual characters
    columns = password_split + ["target"]
    print("columns: ",columns)# Add 'target' column for labels
    df = pd.DataFrame(training_data, columns=columns)  # Create DataFrame
    return df


def get_password(recorder):
    password = ""
    count = 0
    print(len(recorder.samples))
    while count < len(recorder.samples)-1:  # Iterate over samples
        password += recorder.samples[count][1]  # Add the key pressed to password
        count += 2  # Skip to the next release
    return password


def transform_data(training_data):
    transformed_data = []
    print("TRAining: ", training_data)
    for i in range(len(training_data)):
        transformed_data.append(transform(training_data[i]))  # Apply transformation to each sample
    print("transformed data:", transformed_data)
    return transformed_data


def transform(recorder) -> []:
    i = 0
    numerical_recorder = []

    # Iterate through the recorder, skipping by 2 (press-release pairs)
    while i < len(recorder) - 1:  # Ensure there's a press-release pair to process
        press_time = recorder[i][2]
        release_time = recorder[i + 1][2]
        numerical_recorder.append(release_time - press_time)  # Calculate time between press-release
        i += 2  # Move to the next key press-release pair

    numerical_recorder.append(recorder[-1])  # Add the class label (0 or 1)

    return numerical_recorder