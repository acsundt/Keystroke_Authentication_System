import numpy as np
import pandas as pd


def generate_synthetic_data(password, base_values):
    """
    Generate synthetic data based on characters in the password and a list of base values.
    Each character gets a random range of ±0.3 around the corresponding base value.

    Args:
        password (str): Password string that will determine the random distributions
        base_values (list): List of float values used as centers for uniform distributions
                           The last value is used for the target distribution
    """
    if isinstance(base_values, list) and len(base_values) == 1 and isinstance(base_values[0], list):
        values = base_values[0]
    else:
        raise ValueError("base_values must be a list containing a single list of float values")

        # Validate inputs
    if len(values) != len(password) + 1:
        raise ValueError(f"Base values list length ({len(values)}) must be password length ({len(password)}) plus 1")

        # Set a seed based on the hash of the password for reproducibility
    seed = sum(ord(char) for char in password)
    np.random.seed(seed)

    # Number of rows
    # n_rows = max(50, len(password) * 10)  # At least 50 rows
    n_rows = 200

    # Create ranges for each character (±0.3 around base value)
    ranges = []
    for i, char in enumerate(password):
        base_value = values[i]
        min_val = max(0, base_value - 0.3)  # Ensure non-negative
        max_val = min(1, base_value + 0.3)  # Ensure not over 1.0
        ranges.append((min_val, max_val))

    # Target base value (last value in the list)
    target_base = values[-1]

    # Generate features based on password characters and corresponding base values
    features = {}

    # Generate different columns based on available password characters
    column_names = []

    # Create at least 4 columns (or password length if greater)
    num_columns = max(4, len(password))

    # Reuse password characters if needed
    for i in range(num_columns):
        char_idx = i % len(password)  # Cycle through password chars if needed
        char = password[char_idx]
        column_name = f"feature_{char}_{i}"
        column_names.append(column_name)

        # Get range for this character
        min_val, max_val = ranges[char_idx]

        # Generate half class 0 and half class 1 with slight variation
        if i < 2:  # First two columns have more separation between classes
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

    # Generate target values - ensuring we have binary classification
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


def main():
    np.random.seed(42)

    n_rows = 50  # Number of rows

    p_class_0 = np.random.uniform(0.06, 0.9, size=n_rows // 2)  # Lower range for class 0
    p_class_1 = np.random.uniform(0.06, 0.11, size=n_rows // 2)  # Higher range for class 1

    p = np.concatenate([p_class_0, p_class_1])

    a_class_0 = np.random.uniform(0.12, 0.2, size=n_rows)
    a_class_1 = np.random.uniform(0.1, 0.2, size=n_rows)

    a = np.concatenate([a_class_0, a_class_1])

    s = np.random.uniform(0.05, 0.15, size=n_rows)
    s2 = np.random.uniform(0.1, 0.2, size=n_rows)

    # Assign target values in a pattern
    target = np.array([0] * (n_rows // 2) + [1] * (n_rows // 2))

    indices = np.random.permutation(n_rows)
    p = p[indices]
    a = a[indices]
    s = s[indices]
    s2 = s2[indices]
    target = target[indices]

    df = pd.DataFrame({
        'p': p,
        'a': a,
        's': s,
        's2': s2,
        'target': target
    })

    df.to_csv("test.csv",index=False)
