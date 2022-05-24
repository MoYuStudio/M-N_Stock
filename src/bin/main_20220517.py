
# import socket
import datetime
# import geoip2.database

import module.day_convert as day_convert

# ip = socket.gethostbyname(socket.gethostname())
# reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
# response = reader.city(ip)
# # 有多种语言，我们这里主要输出英文和中文
# print("你查询的IP的地理位置是:")

# print("地区：{}({})".format(response.continent.names["es"],
#                                        response.continent.names["zh-CN"]))

# print("国家：{}({}) ，简称:{}".format(response.country.name,
#                                                         response.country.names["zh-CN"],
#                                                         response.country.iso_code))

# print("洲／省：{}({})".format(response.subdivisions.most_specific.name,
#                                           response.subdivisions.most_specific.names["zh-CN"]))

# print("城市：{}({})".format(response.city.name, 
#                                           response.city.names["zh-CN"]))

# print("经度：{}，纬度{}".format(response.location.longitude,
#                                             response.location.latitude))

# print("时区：{}".format(response.location.time_zone))

# print("邮编:{}".format(response.postal.code))


DC = day_convert.DayConvert(datetime.datetime(2020, 5, 1, 0, 0, 0))
DC.print()
DC = day_convert.DayConvert(datetime.datetime(2020, 6, 1, 0, 0, 0))
DC.print()
DC = day_convert.DayConvert(datetime.datetime(2020, 7, 1, 0, 0, 0))
DC.print()

def dt_change():
    for year in range(2000,2022,1):
        for month in range(1,12,1):
            for day in range(1,31,1):
                for hour in range(0,23,2):

                    try:
                        print(datetime.datetime(year, month, day, hour, 0, 0))
                        DC = day_convert.DayConvert(datetime.datetime(year, month, day, hour, 0, 0))
                        a = DC.set()
                        print(a)
                    except:
                        pass
