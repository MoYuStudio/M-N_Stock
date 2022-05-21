
#-*-coding:utf-8-*-

import time
import datetime

import tzlocal

class UTCOffset:
    """
    the year of the true solar time.

    :return: the year of the true solar time.
    :rtype: int
    
    """
    def __init__(self):

        self.UTC = datetime.datetime.utcnow().replace(tzinfo = datetime.timezone.utc)
        self.LMT = datetime.datetime.now() # local mean time

        self.tz_info = tzlocal.get_localzone()
        self.date = datetime.datetime.now(self.tz_info)
        self.UTC_OFFSET = self.date.utcoffset().total_seconds()
        utc_offset = time.localtime().tm_gmtoff

        self.TRUE_SOLAR_TIME = self.UTC - datetime.timedelta(seconds = utc_offset) # BUG: utc_offset 减不进去

        self.TRUE_SOLAR_TIME = str(self.TRUE_SOLAR_TIME)

        self.TST_YEAR = self.TRUE_SOLAR_TIME[0:4]
        self.TST_MONTH = self.TRUE_SOLAR_TIME[5:7]
        self.TST_DAY = self.TRUE_SOLAR_TIME[8:10]
        self.TST_HOUR = self.TRUE_SOLAR_TIME[11:13]
        self.TST_MINUTE = self.TRUE_SOLAR_TIME[14:16]
        self.TST_SECOND = self.TRUE_SOLAR_TIME[17:19]
        self.TST_SECOND_FLOAT = self.TRUE_SOLAR_TIME[17:26]

        print(self.TRUE_SOLAR_TIME)
