import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('data/transformed_data/transferred.csv')

# Compute the R.A in the Ecliptic plane
data['RA_Ecl'] = np.arctan2(data['y_Ecl'], data['x_Ecl'])

# Convert the R.A to degrees from radians
data['RA_Ecl'] = np.degrees(data['RA_Ecl'])

# Adjust the values to be within 0-360 degrees
data['RA_Ecl'] = data['RA_Ecl'].apply(lambda x: x if x > 0 else x + 360)

# Save the updated DataFrame back to the csv
data.to_csv('data/transformed_data/transferred.csv', index=False)

