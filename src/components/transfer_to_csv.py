
import csv
import re
import tkinter as tk
from tkinter import filedialog

# File selector 
root = tk.Tk()
root.withdraw()

default_dir = "data/raw_data/horizons"
input_path = filedialog.askopenfilename(initialdir = default_dir, title = "Select Horizons coordinate file", filetypes=[("Text files", "*.txt")])

# Output_path
csv_tf = 'data/transformed_data/transferred.csv'

# Define the headers
headers = [
    "Date__UT__HR:MN",
    "R.A._ICRF",
    "DEC_ICRF",
    "delta",
    "deldot"
]

# Import file
with open(input_path, 'r') as input_file:
    lines = input_file.readlines()

# Extract data
data = []
recording = False
for line in lines:
    if line.startswith("$$SOE"):
        recording = True
        continue
    elif line.startswith("$$EOE"):
        recording = False
        continue
    elif recording:
        # Split the line into its constituent parts using regex
        parts = re.split(r',\s*|\s\s+', line.strip())
        
        if len(parts) < 8:
            continue
        
        # Dictionary for data line
        data_line = {
            "Date__UT__HR:MN": parts[0],
            "R.A._ICRF": parts[3],
            "DEC_ICRF": parts[4],
            "delta": parts[5],
            "deldot": parts[6]
        }
        
        # Fill in data line
        data.append(data_line)

# Export to CSV
with open(csv_tf, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
