
#-*-coding:utf-8-*-

import pandas
import pandas_datareader

class StockInfo:
    def __init__(self, stock_symbol, start_date, end_date):
        self.stock_symbol = stock_symbol
        self.stock_data_pd = pandas_datareader.get_data_yahoo(stock_symbol, start_date, end_date)
        self.data_dict = self.stock_data_pd.to_dict('index')
        self.data_dict_keys = list(self.data_dict.keys())

if __name__ == '__main__':
    stock_info = StockInfo('AAPL', '2000-01-01', '2022-01-31')
    print(stock_info.data_dict_keys[0], stock_info.data_dict[stock_info.data_dict_keys[0]])