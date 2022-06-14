
import tushare # 股票数据库 https://tushare.pro/

import seaborn # 数据可视化库
import matplotlib.pyplot # 可视化库

# import pandas # 数据分析库
# import sklearn # 数据分析库
# from sklearn import SomeRegressor
# from sklearn.linear_model import SomeRegressor
# from sklearn.ensemble import SomeRegressor

tushare.set_token('dce74e113985d5da2a8dffe05cccdba7c72aa1e0c34601dbb8d2cbc0')
pro = tushare.pro_api()

df = pro.daily(ts_code='600519.SH',
                start_date='20220101', 
                end_date='20220301')

shibor = pro.shibor(start_date='20220101', 
                end_date='20220301')

seaborn.lineplot(x='trade_date',
                    y='close',
                    data=df,
                    hue='ts_code',
                    color='blue')

seaborn.lineplot(x='date',
                    y='on',
                    data=shibor,
                    color='red')

matplotlib.pyplot.show()

