
import datetime
import sys

import module.day_convert_data as D

class DayConvert:

    def __init__(self, dt=None):
        """ 初始化：参数为datetime.datetime类实例，默认当前时间  """
        self.localtime = dt if dt else datetime.datetime.today()
        self.gz_year_value = ""
        self.ln_month_value = ""
        self.wu_xing = ""

        self.START_YEAR = D.START_YEAR

        self.g_lunar_month = D.g_lunar_month
        self.g_lunar_month_day = D.g_lunar_month_day

        self.gan = D.gan
        self.zhi = D.zhi
        self.jie = D.jie

        self.jie_qi_odd = D.jie_qi_odd
        self.jie_qi_month = D.jie_qi_month

    def gz_year(self):  # 返回干支纪年
        ct = self.localtime  # 取当前时间
        year = self.ln_year() - 3 - 1  # 农历年份减3 （说明：补减1）
        G = year % 10  # 模10，得到天干数
        Z = year % 12  # 模12，得到地支数
        self.gz_year_value = self.gan[G] + self.zhi[Z]
        return self.gz_year_value

    def gz_month(self):  # 返回干支纪月（原作者未实现）
        """
        干支纪月的计算规则较为复杂，是本人在前人的基础上实现的，填补了空白。
        1、首先判断当前日期所处的节气范围，
        2、特别要考虑年数是否需要增减，以立春为界，如正月尚未立春的日子年数减一，
        3、月的天干公式 （年干序号 * 2 + 月数） % 10 ，其中 0 表示最后一个天干，
        4、月的地支是固定的，查表可得。
        :return:
        """
        ct = self.localtime  # 取当前时间
        jie_qi = self.ln_jie()
        nl_month_val = self.ln_month()
        if len(jie_qi) > 0 and jie_qi in self.jie_qi_odd:   # 如果恰好是节气当日
            if self.jie_qi_month[jie_qi][0] == 0 and nl_month_val == 12:  #
                year = self.ln_year() - 3  # 虽然农历已经是腊月，但是已经立春， 所以年加一
                G = year % 10  # 模10，得到天干数
                Z = year % 12  # 模12，得到地支数
                nl_year = self.gan[G] + self.zhi[Z]
                nl_month = 0
            else:
                nl_year = self.gz_year_value  # 干支纪年
                nl_month = self.jie_qi_month[jie_qi][0]  # 计算出干支纪月
        else:      # 如果不是节气日，则循环判断后一个分月节气是什么
            nl_year = self.gz_year_value
            nl_month = 0
            for i in range(-1, -40, -1):
                var_days = ct + datetime.timedelta(days=i)
                jie_qi = self.nl_jie(var_days)
                if len(jie_qi) > 0 and jie_qi in self.jie_qi_odd:
                    if self.jie_qi_month[jie_qi][0] > 0:
                        nl_month = self.jie_qi_month[jie_qi][0]
                    elif self.jie_qi_month[jie_qi][0] == 0 and nl_month_val == 12:   #
                        year = self.ln_year() - 3    # 虽然农历已经是腊月，但是已经立春， 所以年加一
                        G = year % 10  # 模10，得到天干数
                        Z = year % 12  # 模12，得到地支数
                        nl_year = self.gan[G] + self.zhi[Z]
                        nl_month = 0
                    else:
                        nl_month = 0
                    break
        gan_str = self.gan
        # print(nl_year[0])
        month_num = (gan_str.find(nl_year[0])+1) * 2 + nl_month + 1
        M = month_num % 10
        if M == 0:
            M = 10
        gz_month = self.gan[M-1] + self.jie_qi_month[jie_qi][1]
        return gz_month

    def gz_day(self):  # 返回干支纪日
        ct = self.localtime  # 取当前时间
        C = ct.year // 100  # 取世纪数，减一
        y = ct.year % 100  # 取年份后两位（若为1月、2月则当前年份减一）
        y = y - 1 if ct.month == 1 or ct.month == 2 else y
        M = ct.month  # 取月份（若为1月、2月则分别按13、14来计算）
        M = M + 12 if ct.month == 1 or ct.month == 2 else M
        d = ct.day  # 取日数
        i = 0 if ct.month % 2 == 1 else 6  # 取i （奇数月i=0，偶数月i=6）

        # 下面两个是网上的公式
        # http://baike.baidu.com/link?url=MbTKmhrTHTOAz735gi37tEtwd29zqE9GJ92cZQZd0X8uFO5XgmyMKQru6aetzcGadqekzKd3nZHVS99rewya6q
        # 计算干（说明：补减1）
        G = 4 * C + C // 4 + 5 * y + y // 4 + 3 * (M + 1) // 5 + d - 3 - 1
        G = G % 10
        # 计算支（说明：补减1）
        Z = 8 * C + C // 4 + 5 * y + y // 4 + 3 * (M + 1) // 5 + d + 7 + i - 1
        Z = Z % 12

        # 返回 干支纪日
        return self.gan[G] + self.zhi[Z]

    def gz_hour(self):  # 返回干支纪时（时辰）
        """
        原作者计算的时干支，实际上只返回了时辰的地支，缺少天干；
        我补充了天干的计算，公式皆为原创
        时干数 = ((日干 % 5)*2 + 时辰 -2) % 10
        :return:
        """
        ct = self.localtime  # 取当前时间
        # 计算支
        Z = round((ct.hour / 2) + 0.1) % 12  # 之所以加0.1是因为round的bug!!
        gz_day_value = self.gz_day()
        gz_day_num = self.gan.find(gz_day_value[0]) + 1
        gz_day_yu = gz_day_num % 5
        hour_num = Z + 1
        if gz_day_yu == 0:
            gz_day_yu = 5
        gz_hour_num = (gz_day_yu * 2 - 1 + hour_num-1) % 10
        if gz_hour_num == 0:
            gz_hour_num = 10
        # 返回 干支纪时（时辰）
        return self.gan[gz_hour_num-1] + self.zhi[Z]

    def ln_year(self):  # 返回农历年
        year, _, _ = self.ln_date()
        return year

    def ln_month(self):  # 返回农历月
        _, month, _ = self.ln_date()
        self.ln_month_value = month
        return month

    def ln_day(self):  # 返回农历日
        _, _, day = self.ln_date()
        return day

    def ln_date(self):  # 返回农历日期整数元组（年、月、日）（查表法）
        delta_days = self._date_diff()

        # 阳历1901年2月19日为阴历1901年正月初一
        # 阳历1901年1月1日到2月19日共有49天
        if delta_days < 49:
            year = self.START_YEAR - 1
            if delta_days < 19:
                month = 11
                day = 11 + delta_days
            else:
                month = 12
                day = delta_days - 18
            return year, month, day

        # 下面从阴历1901年正月初一算起
        delta_days -= 49
        year, month, day = D.START_YEAR, 1, 1
        # 计算年
        tmp = self._lunar_year_days(year)
        while delta_days >= tmp:
            delta_days -= tmp
            year += 1
            tmp = self._lunar_year_days(year)

        # 计算月
        (foo, tmp) = self._lunar_month_days(year, month)
        while delta_days >= tmp:
            delta_days -= tmp
            if month == self._get_leap_month(year):
                (tmp, foo) = self._lunar_month_days(year, month)
                if delta_days < tmp:
                    return 0, 0, 0
                delta_days -= tmp
            month += 1
            (foo, tmp) = self._lunar_month_days(year, month)

        # 计算日
        day += delta_days
        return year, month, day



    def ln_jie(self):  # 返回农历节气
        ct = self.localtime  # 取当前时间
        year = ct.year
        for i in range(24):
            # 因为两个都是浮点数，不能用相等表示
            delta = self._julian_day() - self._julian_day_of_ln_jie(year, i)
            if -.5 <= delta <= .5:
                return self.jie[i * 2:(i + 1) * 2]
        return ''

    def nl_jie(self,dt):
        year = dt.year
        for i in range(24):
            # 因为两个都是浮点数，不能用相等表示
            delta = self.rulian_day(dt) - self._julian_day_of_ln_jie(year, i)
            if -.5 <= delta <= .5:
                return self.jie[i * 2:(i + 1) * 2]
        return ''

    # 显示日历
    def calendar(self):
        pass

    #######################################################
    #            下面皆为私有函数
    #######################################################

    def _date_diff(self):
        """ 返回基于1901/01/01日差数 """
        return (self.localtime - datetime.datetime(1901, 1, 1)).days

    def _get_leap_month(self, lunar_year):
        flag = self.g_lunar_month[(lunar_year - self.START_YEAR) // 2]
        if (lunar_year - self.START_YEAR) % 2:
            return flag & 0x0f
        else:
            return flag >> 4

    def _lunar_month_days(self, lunar_year, lunar_month):
        if lunar_year < self.START_YEAR:
            return 30

        high, low = 0, 29
        iBit = 16 - lunar_month

        if lunar_month > self._get_leap_month(lunar_year) and self._get_leap_month(lunar_year):
            iBit -= 1

        if self.g_lunar_month_day[lunar_year - self.START_YEAR] & (1 << iBit):
            low += 1

        if lunar_month == self._get_leap_month(lunar_year):
            if self.g_lunar_month_day[lunar_year - self.START_YEAR] & (1 << (iBit - 1)):
                high = 30
            else:
                high = 29

        return high, low

    def _lunar_year_days(self, year):
        days = 0
        for i in range(1, 13):
            (high, low) = self._lunar_month_days(year, i)
            days += high
            days += low
        return days

    # 返回指定公历日期的儒略日（http://blog.csdn.net/orbit/article/details/9210413）
    def _julian_day(self):
        ct = self.localtime  # 取当前时间
        year = ct.year
        month = ct.month
        day = ct.day

        if month <= 2:
            month += 12
            year -= 1

        B = year / 100
        B = 2 - B + year / 400

        dd = day + 0.5000115740  # 本日12:00后才是儒略日的开始(过一秒钟)*/
        return int(365.25 * (year + 4716) + 0.01) + int(30.60001 * (month + 1)) + dd + B - 1524.5

    def rulian_day(self, dt):   # 重写_julian_day 函数，变成可以传参的函数
        year = dt.year
        month = dt.month
        day = dt.day
        if month <= 2:
            month += 12
            year -= 1

        B = year / 100
        B = 2 - B + year / 400

        dd = day + 0.5000115740  # 本日12:00后才是儒略日的开始(过一秒钟)*/
        return int(365.25 * (year + 4716) + 0.01) + int(30.60001 * (month + 1)) + dd + B - 1524.5

        # 返回指定年份的节气的儒略日数（http://blog.csdn.net/orbit/article/details/9210413）
    def _julian_day_of_ln_jie(self, year, st):
        s_stAccInfo = [
            0.00, 1272494.40, 2548020.60, 3830143.80, 5120226.60, 6420865.80,
            7732018.80, 9055272.60, 10388958.00, 11733065.40, 13084292.40, 14441592.00,
            15800560.80, 17159347.20, 18513766.20, 19862002.20, 21201005.40, 22529659.80,
            23846845.20, 25152606.00, 26447687.40, 27733451.40, 29011921.20, 30285477.60]

        # 已知1900年小寒时刻为1月6日02:05:00
        base1900_SlightColdJD = 2415025.5868055555

        if (st < 0) or (st > 24):
            return 0.0

        stJd = 365.24219878 * (year - 1900) + s_stAccInfo[st] / 86400.0

        return base1900_SlightColdJD + stJd

    def print(self):

        ln = DayConvert(self.localtime)

        print('公历 {}  北京时间 {}'.format(ln.localtime.date(), ln.localtime.time()))

        print('{} {} {} {}'.format(ln.gz_year(), ln.gz_month(), ln.gz_day(), ln.gz_hour()))

    def set(self):

        ln = DayConvert(self.localtime)

        return ln.gz_year(), ln.gz_month(), ln.gz_day(), ln.gz_hour()


if __name__ == '__main__':

    ln = DayConvert(datetime.datetime(2022, 5, 15, 0, 30, 15))

    print('公历 {}  北京时间 {}'.format(ln.localtime.date(), ln.localtime.time()))

    print('{} {} {} {}'.format(ln.gz_year(), ln.gz_month(), ln.gz_day(), ln.gz_hour()))
