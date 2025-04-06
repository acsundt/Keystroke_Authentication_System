import numpy as np
import pandas as pd

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
