import numpy as np
import pandas as pd


def generate_synthetic_data(password, base_values):

    # Makes sure that the lengths are equal
    if isinstance(base_values, list) and len(base_values) == 1 and isinstance(base_values[0], list):
        values = base_values[0]
    else:
        raise ValueError("base_values must be a list containing a single list of float values")

    if len(values) != len(password) + 1:
        raise ValueError(f"Base values list length ({len(values)}) must be password length ({len(password)}) plus 1")

    # Set a seed based on the hash of the password for reproducibility
    seed = sum(ord(char) for char in password)
    np.random.seed(seed)

    # Number of rows
    n_rows = 500

    # Create ranges for each character (±0.3 around base value)
    ranges = []
    for i, char in enumerate(password):
        base_value = values[i]
        min_val = max(0, base_value - 0.03)  # Ensure non-negative
        max_val = min(1, base_value + 0.03)  # Ensure not over 1.0
        ranges.append((min_val, max_val))

    # Target base value (last value in the list)
    target_base = values[-1]

    # Generate features based on password characters and corresponding base values
    features = {}

    # Generate different columns based on available password characters
    column_names = []

    # Create at least 1 column (or password length if greater)
    num_columns = max(1, len(password))

    # Reuse password characters if needed
    for i in range(num_columns):
        char_idx = i % len(password)  # Cycle through password chars if needed
        char = password[char_idx]
        column_name = f"feature_{char}_{i}"
        column_names.append(column_name)

        # Get range for this character
        min_val, max_val = ranges[char_idx]

        # Generate half class 0 and half class 1 with slight variation
        if i < 2:
            class_0_min = min_val
            class_0_max = (min_val + max_val) / 2
            class_1_min = (min_val + max_val) / 2
            class_1_max = max_val
        else:
            class_0_min, class_0_max = min_val, max_val
            class_1_min, class_1_max = min_val, max_val

        values_class_0 = np.random.uniform(class_0_min, class_0_max, size=n_rows // 2)
        values_class_1 = np.random.uniform(class_1_min, class_1_max, size=n_rows // 2)

        values = np.concatenate([values_class_0, values_class_1])
        features[column_name] = values

    # Create target values (last element in base_values list)
    target_min = max(0, target_base - 0.3)
    target_max = min(1, target_base + 0.3)

    # Generate target values
    if target_base < 0.5:
        # More 0s than 1s
        num_zeros = int(n_rows * (0.5 + target_base / 2))
        num_ones = n_rows - num_zeros
    else:
        # More 1s than 0s
        num_ones = int(n_rows * (target_base))
        num_zeros = n_rows - num_ones

    target = np.array([0] * num_zeros + [1] * num_ones)

    # Create DataFrame
    df = pd.DataFrame(features)
    df['target'] = target

    return df

