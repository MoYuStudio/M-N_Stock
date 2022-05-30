
import datetime

import pytz

pacific_now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
a = pacific_now.utcoffset().total_seconds()/60/60
print(a)

def is_dst(zonename):
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(datetime.datetime(2002, 10, 27, 6, 0, 0))
    return now.astimezone(tz).dst() != datetime.timedelta(0)

print(is_dst('Asia/Shanghai'))

# utc = pytz.utc
# print(utc)
# print(utc.zone)
# tz = pytz.timezone('Asia/Shanghai')
# print(tz.zone)
# fmt = '%Y-%m-%d %H:%M:%S %Z% z'
# loc_dt = tz.localize(datetime.datetime(2002, 10, 27, 6, 0, 0)) 
# # print(loc_dt.strftime(fmt))
# print(loc_dt)
# print(tz.utcoffset(normal, is_dst=True)) 

# print(pytz.all_timezones)
# print(len(pytz.all_timezones))
# print('='*30)
# print(pytz.common_timezones)
# print(len(pytz.common_timezones))