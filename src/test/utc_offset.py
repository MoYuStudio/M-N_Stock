
import datetime

import pytz


utc = pytz.utc
print(utc.zone)
eastern = pytz.timezone('Asia/Shanghai')
print(eastern.zone)
fmt = '%Y-%m-%d %H:%M:%S %Z% z'
loc_dt = eastern.localize(datetime.datetime(2002, 10, 27, 6, 0, 0)) 
# print(loc_dt.strftime(fmt))
print(loc_dt)

# print(pytz.all_timezones)
# print(len(pytz.all_timezones))
# print('='*30)
# print(pytz.common_timezones)
# print(len(pytz.common_timezones))