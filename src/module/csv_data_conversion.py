
#-*-coding:utf-8-*-

import pandas

from . import equation_of_time
from . import day_convert

class CSVDataConversion:
    def __init__(self, folder_path = 'src/module/data/transferred.csv'):
        
        self.folder_path = folder_path
        
        self.run()
        
    def run(self):
        self.csv_data = pandas.read_csv(self.folder_path)
        for i in self.csv_data['Date__UT__HR:MN']:
            
            # print(i[0]+i[1]+i[2]+i[3])
            # print(i[5]+i[6]+i[7])
            # print(i[9]+i[10])
            
            mouth_dict = {'Jan':1,'Feb':2,'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
            
            self.eot = equation_of_time.EquationOfTime(int(i[0]+i[1]+i[2]+i[3]),mouth_dict[i[5]+i[6]+i[7]],int(i[9]+i[10]),0,0,0,timezone='Europe/London')
            self.dc = day_convert.DayConvert(self.eot.true_solar_time)
            
            self.ymd = self.dc.year_gan + self.dc.month_gan + self.dc.day_gan
        
            self.csv_data['year_gz'] = self.dc.year_gan
            self.csv_data['month_gz'] = self.dc.month_gan
            self.csv_data['day_gz'] = self.dc.day_gan
            self.csv_data['ymd_gz'] = self.ymd
            
            self.csv_data.to_csv(self.folder_path, index=False)
            
if __name__ == '__main__':
    csv_dc = CSVDataConversion()
    