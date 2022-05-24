
#-*-coding:utf-8-*-

from . import utc_offset
from . import day_convert

class Output:
    def __init__(self):
        self.uo = utc_offset.UTCOffset()
        self.dc = day_convert.DayConvert(self.uo.true_solar_time)
        self.dc.run()

    def run(self):

        print('国际标准时间 UTC: '+str(self.uo.UTC))
        print('当地标准时间 LMT: '+str(self.uo.LMT))
        print('UTC偏移量 UTC_OFFSET: '+str(self.uo.UTC_offset))
        print('真太阳时 TRUE SOLAR TIME: '+str(self.uo.true_solar_time))
        print('干支历 Gan Zhi: ' + str(self.dc.year_gan) + ' ' + str(self.dc.month_gan) + ' ' + str(self.dc.day_gan) + ' ' + str(self.dc.hour_gan))

if __name__ == '__main__':
    op = Output()
    op.run()