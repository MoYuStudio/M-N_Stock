
import tkinter as tk
from tkinter import filedialog

import pandas as pd

csv_tf = 'data/transformed_data/transferred.csv'
merged_file = 'data/transformed_data/merged.csv'
dropped_file = 'data/transformed_data/dropped.csv'

#! Merge stock data to tf
def file_merge():

    # File selector
    root = tk.Tk()
    root.withdraw()

    default_dir = "data/raw_data/stock"
    Stock_file = filedialog.askopenfilename(initialdir = default_dir, title = "Select stock data file", filetypes=[("Excel files", "*.xlsx *.csv")]) #NOTE

    # Merge according to date
    Stock_df = pd.read_excel(Stock_file)
    Original_df = pd.read_csv(csv_tf)

    Original_df['Date'] = pd.to_datetime(Original_df['Date'], format='%m/%d/%Y')
    Stock_df['Date'] = pd.to_datetime(Stock_df['Date'], format='%m/%d/%Y')

    Merged_df = Original_df.merge(Stock_df, on='Date', how='left')

    Merged_df.to_csv(merged_file, index=False)

file_merge()

#! Drop rows with missing data
def drop_empty_rows():

    Merged_df = pd.read_csv(merged_file)

    Dropped_df = Merged_df.dropna()

    Dropped_df.to_csv(dropped_file, index=False)

drop_empty_rows()

#>> Read file

Dropped_df = pd.read_csv(dropped_file)

#! Compute changed
def compute_changed():

    Dropped_df['Changed'] = Dropped_df['Close'] - Dropped_df['Open']

    Dropped_df.to_csv(dropped_file, index=False)

compute_changed()

#! Compute percentage changed
def compute_percentage_changed():

    Dropped_df['%_Changed'] = Dropped_df['Changed'] / Dropped_df['Open'] * 100

    Dropped_df.to_csv(dropped_file, index=False)

compute_percentage_changed()

#! Compute percentage range
def compute_percentage_range():

    Dropped_df['%_Range'] = (Dropped_df['High'] - Dropped_df['Low']) / Dropped_df['Low'] * 100

    Dropped_df.to_csv(dropped_file, index=False)

compute_percentage_range()























