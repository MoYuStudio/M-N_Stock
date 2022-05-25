1
此文档包含关于此项目的大纲以及实现其的子步骤
This file include the outline for this project and steps to achieve them

# 项目大纲 Project outline

	验证干支历法对记录星象的准确性和可靠性 Test Ganzhi astronomical timing system's reliability and accuracy on it's record abilities on planet patterns

	将干支历法中每个干支日代表的星象记录到数据库中 Construct database to store planet patterns correlate to each Ganzhi date

	计算出各种星象所发生的干支日期 Calculate the date for different patterns to occur

	根据各个星象计算其与股市回报波动率的相关性 Calculate the correlations between different planet patterns and stock return volatilities

	根据进一步假设计算干支组合与股市回报波动率的相关性 Calculate the correlations between Ganzhi combinations and stock return volatilities based on further hypothesis

	若干支纪法证为准确且可靠则可在无天文数据的情况下对历史事件进行分析 包括但不限于 If Ganzhi system can corectly record and represent planet patterns, then task can move on historical event analysis without detailed astronomical data, include but not limited to:
		异常事件 Abnormal events
		疾病事件（如天花，新冠） Disease events (e.g. Smallpox, Covid-19)

# 行星数据 Astronomical data:

	采集对象为七政行星：日月金木水火土 Sample targets: the Sun, Moon, Venus, Jupiter, Mercury, Mars, Saturn

	赤道坐标轴转换为地心黄道坐标轴(回归黄道) Convert raw coordinates system into earth centric ecliptic coordinate system (tropical)

	黄道三维坐标转换为二维坐标 Convert 3D coordinates into 2D coordinates

	二维星图 2D Planet/Stellar map
		十二宫划分 Divide the map into 12 equal parts
		二十四宫划分 Divide the map into 24 equal parts
			确定节气点 Determine coordinates for 'Jie' and 'Qi'

	星象计算（出现日期） Pattern calculate (occur date)
		星象表 Pattern list:
			土木相合/相对
			月相
			...

# 干支历准确性与可靠性测试 Reliability and accuracy test for the Ganzhi astronomical timing system

	创建参照点 Create reference point

	真太阳时纠正 True solar time correction
		根据经度纠正政策时间以获取当地天文时间 Convert local political time into astronomical time based on longitude
			当地与政策标准时间标记地的偏移度 Offset between target location and it's political time's landmark

	均时差纠正 Corrections of the equation of time
		根据太阳位置纠正天文时间 Adjust astronomical time base on the location of the Sun

	农历转换 Convert into lunisolar calendar
		#未完成

	干支历转换 Convert into Ganzhi astronomical timing system
	
		星象转换 Convert using planet patterns

			年由太阳位置进位 Year is carried by the Sun
				太阳在黄道经过'春分'点时进位 Indent when the Sun pass the spring equinox

			月由太阳位置进位 Month is carried by the Sun
				闰月 Leap month
					#等待农历转换
				无闰月
					太阳在黄道通过'节'点时进位 Indent when the Sun pass the point of 'Jie'
		
		推测/公式转换 Convert using estimated formula
			#等待理论公式
	
	干支天文历验证

		理论 Theory
			干支天文历六十年一小循环 Ganzhi astronomical calendar perform a small cycle every 60 years

		假设 Hypothesis
			故假设为相同干支日期行星星象相似 So hypothesis is the planet patterns will be similar for the same Ganzhi date
				容差 (度数） errors allowed (degree)：

		验证 Test
			计算重复干支日期的行星角度误差 Calculate planet coordinate errors for repeated Ganzhi date

# 干支天文历数据库建立 

	录入每个干支日所代表的星象 Correlate planet patterns to each Ganzhi date

# 股市数据 Stock data:

	计算股市回报波动率 长度：日和月 calculate stock return volatility. Length: Daily and monthly

# 相关性分析 Correlational analysis:
	
