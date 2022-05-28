#-*-coding:utf-8-*-

import time
import datetime

import tzlocal

LMT = datetime.datetime.now() # local mean time
print(LMT)

UTC = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
print(UTC)

utc_offset = time.localtime().tm_gmtoff
print(utc_offset)

tz = tzlocal.get_localzone()
print(tz)
d = datetime.datetime.now(tz)
print(d)
utc_f = d.utcoffset().total_seconds()
print(utc_f)

a = UTC - datetime.timedelta(seconds=utc_f)
print(a)

tzi = datetime.tzinfo()
print(tzi)