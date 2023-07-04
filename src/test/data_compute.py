

import pandas as pd
import numpy as np
import itertools
import tkinter as tk
from tkinter import filedialog

# File selector
root = tk.Tk()
root.withdraw()

def_dir = "data/transformed_data"
data_file = filedialog.askopenfilename(initialdir = def_dir, title = "Select data file", filetypes=[("Excel files", "*.xlsx *.csv")]) 

# Read the data
df = pd.read_csv(data_file)

# Step 2: Generate all possible numbers from the current observation to the next for all variables
for i in range(len(df) - 1):
    values = {}
    for column in df.columns[1:]:  # Exclude date column
        start = df.loc[i, column]
        end = df.loc[i+1, column]
        if start < end:
            values = np.arange(start, end, 0.001)
        elif start > end:
            values = np.arange(start, end, -0.001)
        else:
            values = np.array([start])
        print(f"Generated values for {column} from row {i} to {i+1}: {values}")

