
#-*-coding:utf-8-*-

from . import equation_of_time
from . import day_convert

class Output:
    def __init__(self):
        self.eot = equation_of_time.EquationOfTime(2000,7,1,0,0,0,timezone='Europe/London')
        self.dc = day_convert.DayConvert(self.eot.true_solar_time)

    def run(self):

        print('时间 TIME : '+str(self.eot.time_datetime))
        print('夏令时 DST : '+str(self.eot.dst_offset_time))
        print('夏令时 UTC : '+str(self.eot.time_datetime + self.eot.dst_offset_time))
        print('偏移量 OFFSET : '+str(self.eot.true_solar_second_offset))
        print('真太阳时 TRUE SOLAR TIME : '+str(self.eot.true_solar_time))
        print('干支历 Gan Zhi: ' + str(self.dc.year_gan) + ' ' + str(self.dc.month_gan) + ' ' + str(self.dc.day_gan) + ' ' + str(self.dc.hour_gan))

if __name__ == '__main__':
    op = Output()
    op.run()