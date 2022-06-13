# 19d787342be3882132942d8d113dbf7078cf7a9b287edaae1d2bbdb9

import tushare

tushare.set_token('dce74e113985d5da2a8dffe05cccdba7c72aa1e0c34601dbb8d2cbc0')
pro = tushare.pro_api()

df = pro.daily(ts_code='03690.HK',
                start_date='20200101', 
                end_date='20220101')
print(df)
