
#-*-coding:utf-8-*-

import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot

import pytz

class EquationOfTime:
    def __init__(self,year,month,day,hour,minute,second,timezone='Asia/Shanghai'):
        self.leap_year_info = None
        self.year_days = None
        self.day_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.time_datetime = datetime.datetime(year,month,day,hour,minute,second)

        self.timezone = pytz.timezone(str(timezone))
        self.timezone_datetime = datetime.datetime.now(self.timezone)
        self.timezone_hour_offset = self.timezone_datetime.utcoffset().total_seconds()/60/60

        self.leap_year()
        #self.dst_offset() #TODO：夏令时开关
        self.true_solar_offset()

    def leap_year(self):
        if self.year %4 == 0:
            if self.year %100 == 0:
                if self.year %400 == 0:
                    self.leap_year_info = True
                else:
                    self.leap_year_info = False
            else:
                self.leap_year_info = True
        else:
            self.leap_year_info = False

        if self.leap_year_info == True:
            self.year_days = 366
            self.day_per_month[1] = 29
        elif self.leap_year_info == False:
            self.year_days = 365
            self.day_per_month[1] = 28

    def dst_offset(self):
        self.is_dst = pytz.utc.localize(self.time_datetime).astimezone(self.timezone).dst() != datetime.timedelta(0)
        self.dst_offset_time = self.timezone.dst(self.time_datetime, is_dst=self.is_dst)
        self.time_datetime = self.time_datetime + self.dst_offset_time

    def true_solar_offset(self):
        self.offset_day = np.linspace(0,self.year_days,self.year_days)
        B = 2*np.pi*(self.offset_day-81)/364
        self.offset_offset = 9.87*np.sin(2*B)-7.53*np.cos(B)-1.5*np.sin(B)

        self.true_solar_second_offset = self.offset_offset[sum(self.day_per_month[:self.month-1])+self.day]

        self.true_solar_time = self.time_datetime + datetime.timedelta(seconds = self.true_solar_second_offset)

    def true_solar_offset_display(self):
        matplotlib.pyplot.plot(self.offset_day,self.offset_offset)
        matplotlib.pyplot.show()
        
if __name__ == '__main__':
    eot = EquationOfTime(2000,7,1,0,0,0,timezone='Europe/London')