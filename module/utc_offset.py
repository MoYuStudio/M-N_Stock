
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

        is_dst = time.daylight and time.localtime().tm_isdst > 0
        utc_offset = - (time.altzone if is_dst else time.timezone)
        self.UTC_offset = utc_offset 

        self.LMT = datetime.datetime.now()
        self.UTC = datetime.datetime.utcnow().replace(tzinfo = datetime.timezone.utc)
        self.true_solar_time = self.LMT - datetime.timedelta(seconds = self.UTC_offset)

if __name__ == '__main__':
    uo = UTCOffset()
