
import pandas_datareader as pdr

data = pdr.get_data_yahoo('NVDA')
print(data.info())