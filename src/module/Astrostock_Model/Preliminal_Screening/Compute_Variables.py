import pandas as pd
import csv
from datetime import datetime
import tempfile
import shutil
import math

CSV_tf = ".\Transformed_Data\Transferred.csv"

#! Convert date

def parse_date(old_date):
    date_obj = datetime.strptime(old_date, '%Y-%b-%d %H:%M')
    new_date = date_obj.strftime('%m/%d/%Y')
    return new_date

def rewrite_dates():
    with open(CSV_tf, 'r') as original_file:
        reader = csv.reader(original_file)
        next(reader)
        rows = [[parse_date(row[0])] + row[1:] for row in reader]

    with open(CSV_tf, 'w', newline='') as original_file:
        writer = csv.writer(original_file)
        writer.writerow(['Date', 'R.A._ICRF', 'DEC_ICRF', 'delta', 'deldot'])

        for row in rows:
            writer.writerow(row)

rewrite_dates()

#! Opposition

def compute_oppositions():
    data = pd.read_csv(CSV_tf)

    data['delta'] = pd.to_numeric(data['delta'])

    data['Opposition'] = data['delta'].diff()
    data['Opposition'] = data['Opposition'].apply(lambda x: 2 if x < 0 else 1)

    data['Opposition'] = data['Opposition'].mask((data['Opposition'] == 2) & (data['Opposition'].shift() == 1), 3)
    data['Opposition'] = data['Opposition'].mask((data['Opposition'] == 1) & (data['Opposition'].shift() == 2), 4)

    data.to_csv(CSV_tf, index=False)

compute_oppositions()

#! Cartesian coordinates

def rewrite_dates_and_add_cartesian():
    filename = CSV_tf

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, newline='') as temp_file, open(filename, 'r', newline='') as original_file:
        reader = csv.DictReader(original_file)
        fieldnames = reader.fieldnames + ['x_ICRF', 'y_ICRF', 'z_ICRF']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            RA = float(row['R.A._ICRF'])
            DEC = float(row['DEC_ICRF'])
            r = float(row['delta'])

            RA_rad = math.radians(RA)
            DEC_rad = math.radians(DEC)

            x = r * math.cos(DEC_rad) * math.cos(RA_rad)
            y = r * math.cos(DEC_rad) * math.sin(RA_rad)
            z = r * math.sin(DEC_rad)

            row['x_ICRF'] = x
            row['y_ICRF'] = y
            row['z_ICRF'] = z

            writer.writerow(row)

    shutil.move(temp_file.name, filename)

rewrite_dates_and_add_cartesian()

#! Ecliptic coordinates

def add_ecliptic_coordinates():
    filename = CSV_tf
    
    epsilon = math.radians(-23.439281)

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, newline='') as temp_file, open(filename, 'r', newline='') as original_file:
        reader = csv.DictReader(original_file)
        fieldnames = reader.fieldnames + ['x_Ecl', 'y_Ecl', 'z_Ecl']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:

            x_ICRF = float(row['x_ICRF'])
            y_ICRF = float(row['y_ICRF'])
            z_ICRF = float(row['z_ICRF'])

            x_Ecl = x_ICRF
            y_Ecl = y_ICRF * math.cos(epsilon) - z_ICRF * math.sin(epsilon)
            z_Ecl = y_ICRF * math.sin(epsilon) + z_ICRF * math.cos(epsilon)

            row['x_Ecl'] = x_Ecl
            row['y_Ecl'] = y_Ecl
            row['z_Ecl'] = z_Ecl

            writer.writerow(row)

    shutil.move(temp_file.name, filename)

add_ecliptic_coordinates()

#! Polar coordinates

def add_polar_coordinates():
    filename = CSV_tf

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, newline='') as temp_file, open(filename, 'r', newline='') as original_file:
        reader = csv.DictReader(original_file)
        fieldnames = reader.fieldnames + ['x_Pol', 'y_Pol']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:

            x_Ecliptic = float(row['x_Ecl'])
            y_Ecliptic = float(row['y_Ecl'])

            x_Polar = math.sqrt(x_Ecliptic**2 + y_Ecliptic**2)  # r = sqrt(x^2 + y^2)
            y_Polar = math.atan2(y_Ecliptic, x_Ecliptic)  # theta = atan(y / x)

            row['x_Pol'] = x_Polar
            row['y_Pol'] = y_Polar

            writer.writerow(row)

    shutil.move(temp_file.name, filename)

add_polar_coordinates()




























