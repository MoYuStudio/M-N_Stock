
#-*-coding:utf-8-*-

import baostock as bs
import pandas as pd
import datetime

code = "NASDAQ:AAPL"

datestart = '2000-01-01'

datetoday = datetime.datetime.today().strftime("%Y-%m-%d")

# 返回数据说明
# 参数名称	参数描述	算法说明
# date	交易所行情日期	
# code	证券代码	
# open	开盘价	
# high	最高价	
# low	最低价	
# close	收盘价	
# preclose	前收盘价	见表格下方详细说明
# volume	成交量（累计 单位：股）	
# amount	成交额（单位：人民币元）	
# adjustflag	复权状态(1：后复权， 2：前复权，3：不复权）	
# turn	换手率	[指定交易日的成交量(股)/指定交易日的股票的流通股总股数(股)]*100%
# tradestatus	交易状态(1：正常交易 0：停牌）	
# pctChg	涨跌幅（百分比）	日涨跌幅=[(指定交易日的收盘价-指定交易日前收盘价)/指定交易日前收盘价]*100%
# peTTM	滚动市盈率	(指定交易日的股票收盘价/指定交易日的每股盈余TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/归属母公司股东净利润TTM
# pbMRQ	市净率	(指定交易日的股票收盘价/指定交易日的每股净资产)=总市值/(最近披露的归属母公司股东的权益-其他权益工具)
# psTTM	滚动市销率	(指定交易日的股票收盘价/指定交易日的每股销售额)=(指定交易日的股票收盘价*截至当日公司总股本)/营业总收入TTM
# pcfNcfTTM	滚动市现率	(指定交易日的股票收盘价/指定交易日的每股现金流TTM)=(指定交易日的股票收盘价*截至当日公司总股本)/现金以及现金等价物净增加额TTM
# isST	是否ST股，1是，0否	
"date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST"
ShowList ="date,close,pctChg"

def ListToDf(rs):

    data_list = []

    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        
    return result

lg = bs.login()
print('login respond error_msg:'+lg.error_msg)

rs = bs.query_history_k_data_plus(code,ShowList,start_date=datestart, end_date=datetoday,frequency="d", adjustflag="3")
result = ListToDf(rs)
print('query_history_k_data_plus respond error_msg:'+rs.error_msg)

print(result)
print(type(result))

result.to_excel('src/module/data/'+'history_A_stock_k_' + code + '.xls', index=False)

bs.logout()
