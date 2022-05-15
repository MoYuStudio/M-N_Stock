
import requests
import datetime

import module.day_convert as day_convert

for year in range(2000,2022,1):
    for month in range(1,12,1):
        for day in range(1,31,1):
            for hour in range(0,23,2):

                try:
                    print(datetime.datetime(year, month, day, hour, 0, 0))
                    DC = day_convert.DayConvert(datetime.datetime(year, month, day, hour, 0, 0))
                    a = DC.set()
                    print(a)
                except:
                    pass
