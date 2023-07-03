

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

# Get column names
columns = df.columns[1:]  # Exclude date column

# Initialize empty dictionary to store overlaps
overlaps = {f'{col1}{col2}': [] for col1, col2 in itertools.combinations(columns, 2)}

# Iterate over rows
for i in range(len(df) - 1):
    # Generate all possible numbers for each variable
    ranges = {col: np.arange(df.loc[i, col], df.loc[i+1, col], 0.01) for col in columns}
    
    # Compare generated values and identify overlapped value between variables
    for col1, col2 in itertools.combinations(columns, 2):
        overlap = np.intersect1d(ranges[col1], ranges[col2])
        overlaps[f'{col1}{col2}'].append(overlap)

# Save the overlapped values to the current dataset
for pair, overlap in overlaps.items():
    df[pair] = pd.Series(overlap)

# Save the updated dataframe to a new CSV file
df.to_csv('data/transformed_data/overlaps.csv', index=False)








