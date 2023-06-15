

import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord, BarycentricMeanEcliptic

# Load the dataset
df = pd.read_csv('data/transformed_data/transferred.csv')

# Function to convert coordinates
def convert_to_ecliptic(row):
    icrf_coord = SkyCoord(ra=row['R.A._ICRF']*u.deg, dec=row['DEC_ICRF']*u.deg, frame='icrs')
    ecl_coord = icrf_coord.transform_to(BarycentricMeanEcliptic)
    return pd.Series({'R.A._Ecl': ecl_coord.lon.deg, 'DEC_Ecl': ecl_coord.lat.deg})

# Apply the function to every row in the dataframe
df[['R.A._Ecl', 'DEC_Ecl']] = df.apply(convert_to_ecliptic, axis=1)

# Save the updated dataset
df.to_csv('data/transformed_data/transferred.csv', index=False)

exit()














