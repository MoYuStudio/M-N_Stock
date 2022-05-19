
#-*-coding:utf-8-*-

import  sxtwl

class DayConvert:
    def __init__(self,YEAR = 2000, MONTH = 1, DAY = 1, HOUR = 0, MINUTE = 0, SECOND = 0):

        self.YEAR = YEAR
        self.MONTH = MONTH
        self.DAY = DAY
        self.HOUR = HOUR
        self.MINUTE = MINUTE
        self.SECOND = SECOND

        self.Gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        self.Zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

    def run(self):
        self.DAY = sxtwl.fromSolar(int(self.YEAR), int(self.MONTH), int(self.DAY))

        self.Y_TG = self.DAY.getYearGZ()
        self.M_TG = self.DAY.getMonthGZ()
        self.D_TG = self.DAY.getDayGZ()
        self.H_TG = self.DAY.getHourGZ(int(self.HOUR))

        self.Year_Gan = self.Gan[self.Y_TG.tg] + self.Zhi[self.M_TG.dz]
        self.Month_Gan = self.Gan[self.M_TG.tg] + self.Zhi[self.D_TG.dz]
        self.Day_Gan = self.Gan[self.D_TG.tg] + self.Zhi[self.H_TG.dz]
        self.HOUR_Gan = self.Gan[self.H_TG.tg] + self.Zhi[self.H_TG.dz]

if __name__ == '__main__':
    pass
