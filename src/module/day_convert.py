
#-*-coding:utf-8-*-

import datetime

import  sxtwl

class DayConvert:
    def __init__(self,true_solar_time):
        self.true_solar_time = true_solar_time

        self.gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        self.zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        
        # self.gan = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        # self.zhi = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
        
        # 1：甲子年 甲子月 甲子日 2：甲子年 甲子月 甲子日
        # a = [[1151,1151,1151],[1151,1151,1151]]
        # a[0] == [1151,1151,1151]

        self.run()

    def run(self):
        self.day = sxtwl.fromSolar(self.true_solar_time.year, self.true_solar_time.month, self.true_solar_time.day)

        self.y_tg = self.day.getYearGZ()
        self.m_tg = self.day.getMonthGZ()
        self.d_tg = self.day.getDayGZ()
        self.h_tg = self.day.getHourGZ(self.true_solar_time.hour)

        self.year_gan = self.gan[self.y_tg.tg] + self.zhi[self.m_tg.dz]
        self.month_gan = self.gan[self.m_tg.tg] + self.zhi[self.d_tg.dz]
        self.day_gan = self.gan[self.d_tg.tg] + self.zhi[self.h_tg.dz]
        self.hour_gan = self.gan[self.h_tg.tg] + self.zhi[self.h_tg.dz]

if __name__ == '__main__':
    dc = DayConvert(datetime.datetime.utcnow().replace(tzinfo = datetime.timezone.utc))