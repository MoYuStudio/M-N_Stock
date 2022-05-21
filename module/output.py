
import utc_offset
import day_convert

UO = utc_offset.UTCOffset()
UTC = UO.UTC
LMT = UO.LMT
UTC_OFFSET = UO.UTC_OFFSET
TURE_SOLAR_TIME = UO.TRUE_SOLAR_TIME
Y = UO.TST_YEAR
M = UO.TST_MONTH
D = UO.TST_DAY
H = UO.TST_HOUR
M = UO.TST_MINUTE
S = UO.TST_SECOND

DC = day_convert.DayConvert(Y, M, D, H, M, S)
DC.run()
YG = DC.Year_Gan
MG = DC.Month_Gan
DG = DC.Day_Gan
HG = DC.HOUR_Gan

print('国际标准时间 UTC: '+str(UTC))
print('当地标准时间 LMT: '+str(LMT))
print('UTC偏移量 UTC_OFFSET: '+str(UTC_OFFSET))
print('真太阳时 TRUE SOLAR TIME: '+str(TURE_SOLAR_TIME))
print('干支历 Gan Zhi: ' + YG + MG + DG + HG)
