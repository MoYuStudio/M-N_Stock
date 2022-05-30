
# Man and Nature Stock

## About

    天人合一 玄学炒股 永远满仓 永远热泪盈眶 awe

项目大纲: [Outline](https://github.com/MoYuStudio/M-N_Stock/blob/main/note/outline)<br/>
项目笔记: [Note](https://github.com/MoYuStudio/M-N_Stock/blob/main/note/note)<br/>

## 引索

>
> [`Official Documentation`](#OfficialDocumentation) 官方文档<br/>
>
>> [`Data`](#Data) 数据<br/>
>>
>>> [`Data Timezones`](#DataTimezones) 数据<br/>
>>>> [`Africa`](#DataTimezones_Africa) Africa<br/>
>>>> [`America`](#DataTimezones_America) America<br/>
>>>> [`Antarctica`](#DataTimezones_Antarctica) Asia<br/>
>>>> [`Arctic`](#DataTimezones_Asia) Arctic<br/>
>>>> [`Asia`](#DataTimezones_Asia) Asia<br/>
>>>> [`Atlantic`](#DataTimezones_Atlantic) Atlantic<br/>
>>>> [`Australia`](#DataTimezones_Australia) Australia<br/>
>>>> [`Brazil`](#DataTimezones_Brazil) Brazil<br/>
>>>> [`Canada`](#DataTimezones_Canada) Canada<br/>
>>>> [`Europe`](#DataTimezones_Europe) Europe<br/>
>>>> [`Indian`](#DataTimezones_Indian) Indian<br/>
>>>> [`Pacific`](#DataTimezones_Pacific) Pacific<br/>
>>>> [`UTC`](#DataTimezones_UTC) UTC<br/>
>>>> [`Other`](#DataTimezones_Other) Other<br/>
>>
>> [`API`](#API) 接口<br/>
>>
>>> [`Module`](#APIModule) 模块<br/>
>>>
>>>> [`equation_of_time`](#APIModule_equation_of_time) 均时差计算 <br/>
>>>> [`day_convert`](#APIModule_day_convert) 公历转换干支历 <br/>
>>>> [`output`](#APIModule_output) 输出 <br/>
>>>> [`stock_info`](#APIModule_stock_info) 股票信息获取 <br/>
>
> [`Rule`](#Rule) 格式规范<br/>
> 
>> [`MoYuStudio Python Code Rule`](#MoYuStudio_Python_Code_Rule) MoYuStudio Python代码编写格式规范<br/>
>> [`MoYuStudio Name Rule`](#MoYuStudio_Name_Rule) MoYuStudio 命名格式规范<br/>
>> [`MoYuStudio Git Commit Message Rule`](#MoYuStudio_Git_Commit_Message_Rule) MoYuStudio Git提交备注格式规范 (借鉴 Angular 团队的 Commit 规范)<br/>


## <span id = 'OfficialDocumentation'>`Official Documentation`</span> 官方文档

### <span id = 'Data'>`data`</span> 数据

#### <span id = 'DataTimezones'>`Data Timezones`</span> 时区数据

##### <span id = 'DataTimezones_Africa'>`Data Timezones : Africa`</span> Africa

    'Africa/Abidjan',
    'Africa/Accra',
    'Africa/Addis_Ababa',
    'Africa/Algiers',
    'Africa/Asmara',
    'Africa/Asmera',
    'Africa/Bamako',
    'Africa/Bangui',
    'Africa/Banjul',
    'Africa/Bissau',
    'Africa/Blantyre',
    'Africa/Brazzaville',
    'Africa/Bujumbura',
    'Africa/Cairo',
    'Africa/Casablanca',
    'Africa/Ceuta',
    'Africa/Conakry',
    'Africa/Dakar',
    'Africa/Dar_es_Salaam',
    'Africa/Djibouti',
    'Africa/Douala',
    'Africa/El_Aaiun',
    'Africa/Freetown',
    'Africa/Gaborone',
    'Africa/Harare',
    'Africa/Johannesburg',
    'Africa/Juba',
    'Africa/Kampala',
    'Africa/Khartoum',
    'Africa/Kigali',
    'Africa/Kinshasa',
    'Africa/Lagos',
    'Africa/Libreville',
    'Africa/Lome',
    'Africa/Luanda',
    'Africa/Lubumbashi',
    'Africa/Lusaka',
    'Africa/Malabo',
    'Africa/Maputo',
    'Africa/Maseru',
    'Africa/Mbabane',
    'Africa/Mogadishu',
    'Africa/Monrovia',
    'Africa/Nairobi',
    'Africa/Ndjamena',
    'Africa/Niamey',
    'Africa/Nouakchott',
    'Africa/Ouagadougou',
    'Africa/Porto-Novo',
    'Africa/Sao_Tome',
    'Africa/Timbuktu',
    'Africa/Tripoli',
    'Africa/Tunis',
    'Africa/Windhoek',
    'Egypt',
    'Libya',
    'Zulu'

##### <span id = 'DataTimezones_America'>`Data Timezones : America`</span> America

    'America/Adak',
    'America/Anchorage',
    'America/Anguilla',
    'America/Antigua',
    'America/Araguaina',
    'America/Argentina/Buenos_Aires',
    'America/Argentina/Catamarca',
    'America/Argentina/ComodRivadavia',
    'America/Argentina/Cordoba',
    'America/Argentina/Jujuy',
    'America/Argentina/La_Rioja',
    'America/Argentina/Mendoza',
    'America/Argentina/Rio_Gallegos',
    'America/Argentina/Salta',
    'America/Argentina/San_Juan',
    'America/Argentina/San_Luis',
    'America/Argentina/Tucuman',
    'America/Argentina/Ushuaia',
    'America/Aruba',
    'America/Asuncion',
    'America/Atikokan',
    'America/Atka',
    'America/Bahia',
    'America/Bahia_Banderas',
    'America/Barbados',
    'America/Belem',
    'America/Belize',
    'America/Blanc-Sablon',
    'America/Boa_Vista',
    'America/Bogota',
    'America/Boise',
    'America/Buenos_Aires',
    'America/Cambridge_Bay',
    'America/Campo_Grande',
    'America/Cancun',
    'America/Caracas',
    'America/Catamarca',
    'America/Cayenne',
    'America/Cayman',
    'America/Chicago',
    'America/Chihuahua',
    'America/Coral_Harbour',
    'America/Cordoba',
    'America/Costa_Rica',
    'America/Creston',
    'America/Cuiaba',
    'America/Curacao',
    'America/Danmarkshavn',
    'America/Dawson',
    'America/Dawson_Creek',
    'America/Denver',
    'America/Detroit',
    'America/Dominica',
    'America/Edmonton',
    'America/Eirunepe',
    'America/El_Salvador',
    'America/Ensenada',
    'America/Fort_Nelson',
    'America/Fort_Wayne',
    'America/Fortaleza',
    'America/Glace_Bay',
    'America/Godthab',
    'America/Goose_Bay',
    'America/Grand_Turk',
    'America/Grenada',
    'America/Guadeloupe',
    'America/Guatemala',
    'America/Guayaquil',
    'America/Guyana',
    'America/Halifax',
    'America/Havana',
    'America/Hermosillo',
    'America/Indiana/Indianapolis',
    'America/Indiana/Knox',
    'America/Indiana/Marengo',
    'America/Indiana/Petersburg',
    'America/Indiana/Tell_City',
    'America/Indiana/Vevay',
    'America/Indiana/Vincennes',
    'America/Indiana/Winamac',
    'America/Indianapolis',
    'America/Inuvik',
    'America/Iqaluit',
    'America/Jamaica',
    'America/Jujuy',
    'America/Juneau',
    'America/Kentucky/Louisville',
    'America/Kentucky/Monticello',
    'America/Knox_IN',
    'America/Kralendijk',
    'America/La_Paz',
    'America/Lima',
    'America/Los_Angeles',
    'America/Louisville',
    'America/Lower_Princes',
    'America/Maceio',
    'America/Managua',
    'America/Manaus',
    'America/Marigot',
    'America/Martinique',
    'America/Matamoros',
    'America/Mazatlan',
    'America/Mendoza',
    'America/Menominee',
    'America/Merida',
    'America/Metlakatla',
    'America/Mexico_City',
    'America/Miquelon',
    'America/Moncton',
    'America/Monterrey',
    'America/Montevideo',
    'America/Montreal',
    'America/Montserrat',
    'America/Nassau',
    'America/New_York',
    'America/Nipigon',
    'America/Nome',
    'America/Noronha',
    'America/North_Dakota/Beulah',
    'America/North_Dakota/Center',
    'America/North_Dakota/New_Salem',
    'America/Nuuk',
    'America/Ojinaga',
    'America/Panama',
    'America/Pangnirtung',
    'America/Paramaribo',
    'America/Phoenix',
    'America/Port-au-Prince',
    'America/Port_of_Spain',
    'America/Porto_Acre',
    'America/Porto_Velho',
    'America/Puerto_Rico',
    'America/Punta_Arenas',
    'America/Rainy_River',
    'America/Rankin_Inlet',
    'America/Recife',
    'America/Regina',
    'America/Resolute',
    'America/Rio_Branco',
    'America/Rosario',
    'America/Santa_Isabel',
    'America/Santarem',
    'America/Santiago',
    'America/Santo_Domingo',
    'America/Sao_Paulo',
    'America/Scoresbysund',
    'America/Shiprock',
    'America/Sitka',
    'America/St_Barthelemy',
    'America/St_Johns',
    'America/St_Kitts',
    'America/St_Lucia',
    'America/St_Thomas',
    'America/St_Vincent',
    'America/Swift_Current',
    'America/Tegucigalpa',
    'America/Thule',
    'America/Thunder_Bay',
    'America/Tijuana',
    'America/Toronto',
    'America/Tortola',
    'America/Vancouver',
    'America/Virgin',
    'America/Whitehorse',
    'America/Winnipeg',
    'America/Yakutat',
    'America/Yellowknife',

##### <span id = 'DataTimezones_Antarctica'>`Data Timezones : Antarctica`</span> Antarctica

    'Antarctica/Casey',
    'Antarctica/Davis',
    'Antarctica/DumontDUrville',
    'Antarctica/Macquarie',
    'Antarctica/Mawson',
    'Antarctica/McMurdo',
    'Antarctica/Palmer',
    'Antarctica/Rothera',
    'Antarctica/South_Pole',
    'Antarctica/Syowa',
    'Antarctica/Troll',
    'Antarctica/Vostok',

##### <span id = 'DataTimezones_Arctic'>`Data Timezones : Arctic`</span> Arctic

    'Arctic/Longyearbyen',

##### <span id = 'DataTimezones_Asia'>`Data Timezones : Asia`</span> Asia

    'Asia/Aden',
    'Asia/Almaty',
    'Asia/Amman',
    'Asia/Anadyr',
    'Asia/Aqtau',
    'Asia/Aqtobe',
    'Asia/Ashgabat',
    'Asia/Ashkhabad',
    'Asia/Atyrau',
    'Asia/Baghdad',
    'Asia/Bahrain',
    'Asia/Baku',
    'Asia/Bangkok',
    'Asia/Barnaul',
    'Asia/Beirut',
    'Asia/Bishkek',
    'Asia/Brunei',
    'Asia/Calcutta',
    'Asia/Chita',
    'Asia/Choibalsan',
    'Asia/Chongqing',
    'Asia/Chungking',
    'Asia/Colombo',
    'Asia/Dacca',
    'Asia/Damascus',
    'Asia/Dhaka',
    'Asia/Dili',
    'Asia/Dubai',
    'Asia/Dushanbe',
    'Asia/Famagusta',
    'Asia/Gaza',
    'Asia/Harbin',
    'Asia/Hebron',
    'Asia/Ho_Chi_Minh',
    'Asia/Hong_Kong',
    'Asia/Hovd',
    'Asia/Irkutsk',
    'Asia/Istanbul',
    'Asia/Jakarta',
    'Asia/Jayapura',
    'Asia/Jerusalem',
    'Asia/Kabul',
    'Asia/Kamchatka',
    'Asia/Karachi',
    'Asia/Kashgar',
    'Asia/Kathmandu',
    'Asia/Katmandu',
    'Asia/Khandyga',
    'Asia/Kolkata',
    'Asia/Krasnoyarsk',
    'Asia/Kuala_Lumpur',
    'Asia/Kuching',
    'Asia/Kuwait',
    'Asia/Macao',
    'Asia/Macau',
    'Asia/Magadan',
    'Asia/Makassar',
    'Asia/Manila',
    'Asia/Muscat',
    'Asia/Nicosia',
    'Asia/Novokuznetsk',
    'Asia/Novosibirsk',
    'Asia/Omsk',
    'Asia/Oral',
    'Asia/Phnom_Penh',
    'Asia/Pontianak',
    'Asia/Pyongyang',
    'Asia/Qatar',
    'Asia/Qostanay',
    'Asia/Qyzylorda',
    'Asia/Rangoon',
    'Asia/Riyadh',
    'Asia/Saigon',
    'Asia/Sakhalin',
    'Asia/Samarkand',
    'Asia/Seoul',
    'Asia/Shanghai',
    'Asia/Singapore',
    'Asia/Srednekolymsk',
    'Asia/Taipei',
    'Asia/Tashkent',
    'Asia/Tbilisi',
    'Asia/Tehran',
    'Asia/Tel_Aviv',
    'Asia/Thimbu',
    'Asia/Thimphu',
    'Asia/Tokyo',
    'Asia/Tomsk',
    'Asia/Ujung_Pandang',
    'Asia/Ulaanbaatar',
    'Asia/Ulan_Bator',
    'Asia/Urumqi',
    'Asia/Ust-Nera',
    'Asia/Vientiane',
    'Asia/Vladivostok',
    'Asia/Yakutsk',
    'Asia/Yangon',
    'Asia/Yekaterinburg',
    'Asia/Yerevan',
    'Hongkong',
    'Iran',
    'Japan',
    'Israel',
    'Singapore',

##### <span id = 'DataTimezones_Atlantic'>`Data Timezones : Atlantic`</span> Atlantic

    'Atlantic/Azores',
    'Atlantic/Bermuda',
    'Atlantic/Canary',
    'Atlantic/Cape_Verde',
    'Atlantic/Faeroe',
    'Atlantic/Faroe',
    'Atlantic/Jan_Mayen',
    'Atlantic/Madeira',
    'Atlantic/Reykjavik',
    'Atlantic/South_Georgia',
    'Atlantic/St_Helena',
    'Atlantic/Stanley',

##### <span id = 'DataTimezones_Australia'>`Data Timezones : Australia`</span> Australia

    'Australia/ACT',
    'Australia/Adelaide',
    'Australia/Brisbane',
    'Australia/Broken_Hill',
    'Australia/Canberra',
    'Australia/Currie',
    'Australia/Darwin',
    'Australia/Eucla',
    'Australia/Hobart',
    'Australia/LHI',
    'Australia/Lindeman',
    'Australia/Lord_Howe',
    'Australia/Melbourne',
    'Australia/NSW',
    'Australia/North',
    'Australia/Perth',
    'Australia/Queensland',
    'Australia/South',
    'Australia/Sydney',
    'Australia/Tasmania',
    'Australia/Victoria',
    'Australia/West',
    'Australia/Yancowinna',

##### <span id = 'DataTimezones_Brazil'>`Data Timezones : Brazil`</span> Brazil

    'Brazil/Acre',
    'Brazil/DeNoronha',
    'Brazil/East',
    'Brazil/West',

##### <span id = 'DataTimezones_Canada'>`Data Timezones : Canada`</span> Canada

    'Canada/Atlantic',
    'Canada/Central',
    'Canada/Eastern',
    'Canada/Mountain',
    'Canada/Newfoundland',
    'Canada/Pacific',
    'Canada/Saskatchewan',
    'Canada/Yukon',

##### <span id = 'DataTimezones_Chile'>`Data Timezones : Chile`</span> Chile

    'Chile/Continental',
    'Chile/EasterIsland',

##### <span id = 'DataTimezones_Etc'>`Data Timezones : Etc`</span> Etc

    'Etc/GMT',
    'Etc/GMT+0',
    'Etc/GMT+1',
    'Etc/GMT+10',
    'Etc/GMT+11',
    'Etc/GMT+12',
    'Etc/GMT+2',
    'Etc/GMT+3',
    'Etc/GMT+4',
    'Etc/GMT+5',
    'Etc/GMT+6',
    'Etc/GMT+7',
    'Etc/GMT+8',
    'Etc/GMT+9',
    'Etc/GMT-0',
    'Etc/GMT-1',
    'Etc/GMT-10',
    'Etc/GMT-11',
    'Etc/GMT-12',
    'Etc/GMT-13',
    'Etc/GMT-14',
    'Etc/GMT-2',
    'Etc/GMT-3',
    'Etc/GMT-4',
    'Etc/GMT-5',
    'Etc/GMT-6',
    'Etc/GMT-7',
    'Etc/GMT-8',
    'Etc/GMT-9',
    'Etc/GMT0',
    'Etc/Greenwich',
    'Etc/UCT',
    'Etc/UTC',
    'Etc/Universal',
    'Etc/Zulu',

##### <span id = 'DataTimezones_Europe'>`Data Timezones : Europe`</span> Europe

    'Europe/Amsterdam',
    'Europe/Andorra',
    'Europe/Astrakhan',
    'Europe/Athens',
    'Europe/Belfast',
    'Europe/Belgrade',
    'Europe/Berlin',
    'Europe/Bratislava',
    'Europe/Brussels',
    'Europe/Bucharest',
    'Europe/Budapest',
    'Europe/Busingen',
    'Europe/Chisinau',
    'Europe/Copenhagen',
    'Europe/Dublin',
    'Europe/Gibraltar',
    'Europe/Guernsey',
    'Europe/Helsinki',
    'Europe/Isle_of_Man',
    'Europe/Istanbul',
    'Europe/Jersey',
    'Europe/Kaliningrad',
    'Europe/Kiev',
    'Europe/Kirov',
    'Europe/Lisbon',
    'Europe/Ljubljana',
    'Europe/London',
    'Europe/Luxembourg',
    'Europe/Madrid',
    'Europe/Malta',
    'Europe/Mariehamn',
    'Europe/Minsk',
    'Europe/Monaco',
    'Europe/Moscow',
    'Europe/Nicosia',
    'Europe/Oslo',
    'Europe/Paris',
    'Europe/Podgorica',
    'Europe/Prague',
    'Europe/Riga',
    'Europe/Rome',
    'Europe/Samara',
    'Europe/San_Marino',
    'Europe/Sarajevo',
    'Europe/Saratov',
    'Europe/Simferopol',
    'Europe/Skopje',
    'Europe/Sofia',
    'Europe/Stockholm',
    'Europe/Tallinn',
    'Europe/Tirane',
    'Europe/Tiraspol',
    'Europe/Ulyanovsk',
    'Europe/Uzhgorod',
    'Europe/Vaduz',
    'Europe/Vatican',
    'Europe/Vienna',
    'Europe/Vilnius',
    'Europe/Volgograd',
    'Europe/Warsaw',
    'Europe/Zagreb',
    'Europe/Zaporozhye',
    'Europe/Zurich',
    'Poland',
    'Portugal',
    'Turkey',

##### <span id = 'DataTimezones_GB'>`Data Timezones : GB`</span> GB

    'GB',
    'GB-Eire',

##### <span id = 'DataTimezones_GMT'>`Data Timezones : GMT`</span> GMT

    'GMT',
    'GMT+0',
    'GMT-0',
    'GMT0',
    'Greenwich',

##### <span id = 'DataTimezones_Iceland'>`Data Timezones : Iceland`</span> Iceland

    'Iceland',

##### <span id = 'DataTimezones_Indian'>`Data Timezones : Indian`</span> Indian

    'Indian/Antananarivo',
    'Indian/Chagos',
    'Indian/Christmas',
    'Indian/Cocos',
    'Indian/Comoro',
    'Indian/Kerguelen',
    'Indian/Mahe',
    'Indian/Maldives',
    'Indian/Mauritius',
    'Indian/Mayotte',
    'Indian/Reunion',

##### <span id = 'DataTimezones_Jamaica'>`Data Timezones : Jamaica`</span> Jamaica

    'Jamaica',

##### <span id = 'DataTimezones_Mexico'>`Data Timezones : Mexico`</span> Mexico

    'Mexico/BajaNorte',
    'Mexico/BajaSur',
    'Mexico/General',

##### <span id = 'DataTimezones_Pacific'>`Data Timezones : Pacific`</span> Pacific

    'Pacific/Apia',
    'Pacific/Auckland',
    'Pacific/Bougainville',
    'Pacific/Chatham',
    'Pacific/Chuuk',
    'Pacific/Easter',
    'Pacific/Efate',
    'Pacific/Enderbury',
    'Pacific/Fakaofo',
    'Pacific/Fiji',
    'Pacific/Funafuti',
    'Pacific/Galapagos',
    'Pacific/Gambier',
    'Pacific/Guadalcanal',
    'Pacific/Guam',
    'Pacific/Honolulu',
    'Pacific/Johnston',
    'Pacific/Kanton',
    'Pacific/Kiritimati',
    'Pacific/Kosrae',
    'Pacific/Kwajalein',
    'Pacific/Majuro',
    'Pacific/Marquesas',
    'Pacific/Midway',
    'Pacific/Nauru',
    'Pacific/Niue',
    'Pacific/Norfolk',
    'Pacific/Noumea',
    'Pacific/Pago_Pago',
    'Pacific/Palau',
    'Pacific/Pitcairn',
    'Pacific/Pohnpei',
    'Pacific/Ponape',
    'Pacific/Port_Moresby',
    'Pacific/Rarotonga',
    'Pacific/Saipan',
    'Pacific/Samoa',
    'Pacific/Tahiti',
    'Pacific/Tarawa',
    'Pacific/Tongatapu',
    'Pacific/Truk',
    'Pacific/Wake',
    'Pacific/Wallis',
    'Pacific/Yap',
    'Kwajalein',

##### <span id = 'DataTimezones_US'>`Data Timezones : US`</span> US

    'US/Alaska',
    'US/Aleutian',
    'US/Arizona',
    'US/Central',
    'US/East-Indiana',
    'US/Eastern',
    'US/Hawaii',
    'US/Indiana-Starke',
    'US/Michigan',
    'US/Mountain',
    'US/Pacific',
    'US/Samoa',
    'Navajo',

##### <span id = 'DataTimezones_UTC'>`Data Timezones : UTC`</span> US

    'UTC',
    'UCT',

##### <span id = 'DataTimezones_Other'>`Data Timezones : Other`</span> Other

    'CET',
    'CST6CDT',
    'Cuba',
    'EET',
    'EST',
    'EST5EDT',
    'Eire',
    'HST',
    'NZ',
    'NZ-CHAT',
    'MET',
    'MST',
    'MST7MDT',
    'PRC',
    'PST8PDT',
    'ROC',
    'ROK',
    'Universal',
    'W-SU',
    'WET',
    
### <span id = 'API'>`API`</span> 接口

#### <span id = 'APIModule'>`Module`</span> 模块

#### <span id = 'APIModule_equation_of_time'>`equation_of_time`</span> 均时差计算

    功能:  均时差计算

    实例化:
        eot = equation_of_time.EquationOfTime(year,month,day,hour,minute,second,timezone='Asia/Shanghai')

    变量: 
        self.leap_year_info [Boolean] 是否闰年

        self.year [Integer] 年
        self.month [Integer] 月
        self.day [Integer] 日
        self.hour [Integer] 时
        self.minute [Integer] 分
        self.second [Integer] 秒

        self.timezone [String] 时区

    调用: 
        self.true_solar_offset_display() # 输出均时差公式图表

#### <span id = 'APIModule_day_convert'>`day_convert`</span> 公历转换干支历

    功能:  公历转换干支历

    实例化:
        dc = day_convert.DayConvert(true_solar_time)

        true_solar_time [datetime.datetime] # 真太阳时

    变量: 
        self.year_gan [str] # 年干
        self.month_gan [str] # 月干
        self.day_gan [str] # 日干
        self.hour_gan [str] # 时干

    调用: 
        None

#### <span id = 'APIModule_output'>`output`</span> 输出

    功能:  输出

    实例化:
        op = output.Output()

    变量:
        None

    调用:
        self.run() # 输出

#### <span id = 'APIModule_stock_info'>`stock_info`</span> 股票信息获取

    功能:  股票信息获取

    实例化:
        si = stock_info.StockInfo(stock_symbol, start_date, end_date)

        stock_symbol [str] # 股票代码
        start_date [str] # 开始日期
        end_date [str] # 结束日期

        eg:
            si = stock_info.StockInfo('000001.SZ', '2019-01-01', '2019-01-31')
                or
            stock_info = stock_info.StockInfo('AAPL', '2000-01-01', '2022-01-31')

    变量: 
        self.stock_symbol [str] # 股票代码
        self.start_date [str] # 开始日期
        self.end_date [str] # 结束日期
        self.stock_data_pd [pandas.DataFrame] # 股票信息 pandas.DataFrame 格式
        self.data_dict [dict] # 股票信息 dict 格式
        self.data_dict_keys [list] # 股票信息 dict 格式的 keys

    调用: 
        self.print_all() # 打印该股票的所有信息

##  <span id = 'Rule'>`Rule`</span> 格式规范

### <span id = 'MoYuStudio_Python_Code_Rule'>`MoYuStudio Python Code Rule`</span> MoYuStudio Python代码编写格式规范

#### 编码

    如无特殊情况, 文件一律使用 UTF-8 编码
    如无特殊情况, 文件头部必须加入#-*-coding:utf-8-*-标识

#### 代码格式

##### 缩进

    统一使用 4 个空格进行缩进

##### 行宽

    每行代码尽量不超过 80 个字符(在特殊情况下可以略微超过 80 ，但最长不得超过 120)

    理由: 
        这在查看 side-by-side 的 diff 时很有帮助
        方便在控制台下查看代码
        太长可能是设计有缺陷

##### 引号

    简单说，自然语言使用双引号，机器标示使用单引号，因此 代码里 多数应该使用 单引号

    自然语言 使用双引号 "..."
        例如错误信息；很多情况还是 unicode，使用u"你好世界"

    机器标识 使用单引号 '...' 例如 dict 里的 key
        正则表达式 使用原生的双引号 r'...'

    文档字符串 (docstring) 使用三个双引号 """......"""

##### 空行

    模块级函数和类定义之间空两行；

    类成员函数之间空一行；

    class A:
    """class A docstring"""
        def __init__(self):
            pass

        def hello(self):
            pass

        def main():
            pass

    可以使用多个空行分隔多组相关的函数

    函数中可以使用空行分隔出逻辑相关的代码

##### import 语句

    import 语句应该分行书写

        # 正确的写法

            import os
            import sys

        # 不推荐的写法

            import sys,os

        # 正确的写法

            from subprocess import Popen, PIPE

    import语句应该使用 absolute import

        # 正确的写法

            from foo.bar import Bar

        # 不推荐的写法

            from ..bar import Bar

    import语句应该放在文件头部，置于模块说明及docstring之后，于全局变量之前；

    import语句应该按照顺序排列，库分三组: 第一组是标准库，第二组是第三方库，第三组是自定义库，每组之间用一个空行分隔 

        import os
        import sys
        import time

        import ptgame

        import moyu_core
        import moyu_engine

    导入其他模块的类定义时，可以使用相对导入

        from myclass import MyClass

    如果发生命名冲突，则可使用命名空间

        import bar
        import foo.bar

        bar.Bar()
        foo.bar.Bar()

##### 空格

    在二元运算符两边各空一格[=,-,+=,==,>,in,is not, and]:

        # 正确的写法

            i = i + 1
            submitted += 1
            x = x * 2 - 1
            hypot2 = x * x + y * y
            c = (a + b) * (a - b)

        # 不推荐的写法

            i=i+1
            submitted +=1
            x = x*2 - 1
            hypot2 = x*x + y*y
            c = (a+b) * (a-b)

    函数的参数列表中，,之后要有空格

        # 正确的写法

            def complex(real, imag):

                pass

        # 不推荐的写法

            def complex(real,imag):

                pass

    函数的参数列表中，默认值等号两边不要添加空格

        # 正确的写法

            def complex(real, imag=0.0):

                pass

        # 不推荐的写法

            def complex(real, imag = 0.0):

                pass

    左括号之后，右括号之前不要加多余的空格

        # 正确的写法

            spam(ham[1], {eggs: 2})

        # 不推荐的写法

            spam( ham[1], { eggs : 2 } )

    字典对象的左括号之前不要多余的空格

        # 正确的写法

            dict["key"] = list[index]

        # 不推荐的写法

            dict ["key"] = list [index]

    不要为对齐赋值语句而使用的额外空格

        # 正确的写法

            x = 1

            y = 2

            long_variable = 3

        # 不推荐的写法

            x             = 1

            y             = 2

            long_variable = 3

##### 换行

    Python 支持括号内的换行。这时有两种情况。

        1) 第二行缩进到括号的起始处

            foo = long_function_name(var_one, var_two,

            var_three, var_four)

        2) 第二行缩进 4 个空格，适用于起始括号就换行的情形

            def long_function_name(

            var_one, var_two, var_three,

            var_four):

            print(var_one)

    使用反斜杠换行，二元运算符+ .等应出现在行末；长字符串也可以用此法换行

        session.query(MyTable).
        filter_by(id=1).
        one()
        print "Hello, "
        "%s %s!" %
        ("Harry", "Potter")

    禁止复合语句，即一行中包含多个语句: 

        # 正确的写法

            do_first()
            do_second()
            do_third()

        # 不推荐的写法

            do_first();do_second();do_third();

    if/for/while一定要换行: 

        # 正确的写法

            if foo == "blah":
            do_blah_thing()

        # 不推荐的写法

            if foo == "blah": do_blash_thing()

##### docstring

    docstring 的规范中最其本的两点: 

        所有的公共模块、函数、类、方法，都应该写 docstring 。私有方法不一定需要，但应该在 def 后提供一个块注释来说明。

    docstring 的结束"""应该独占一行，除非此 docstring 只有一行。

        """Return a foobar

        Optional plotz says to frobnicate the bizbaz first.

        """

        """Oneline docstring"""

### <span id = 'MoYuStudio_Name_Rule'>`MoYuStudio Name Rule`</span> MoYuStudio 命名格式规范

#### 常量

    字母全部大写 使用下划线命名法

#### 变量

    字母全部小写 使用下划线命名法

#### 类名

    首字母大写 使用大驼峰式命名法


### <span id = 'MoYuStudio_Git_Commit_Message_Rule'>`MoYuStudio Git Commit Message Rule`</span> MoYuStudio Git提交备注格式规范 (借鉴 Angular 团队的 Commit 规范)

    每次提交，Commit message 都包括三个部分: Header，Body 和 Footer。

    其中，Header 是必需的，Body 和 Footer 可以省略。

    不管是哪一个部分，任何一行都不得超过72个字符（或100个字符-自定义）。这是为了避免自动换行影响美观。

#### Header

        Header部分只有一行，包括三个字段: type（必需）、scope（可选）和subject（必需）。

    type 用于说明commit的类型，主要包括一下几种

        feat: 新功能（feature）
        fix: 修补bug
        docs: 文档（documentation）
        style: 格式（不影响代码运行的变动）
        refactor: 重构（即不是新增功能，也不是修改bug的代码变动）
        test: 增加测试
        chore: 构建过程或辅助工具的变动

    scope用于说明commit的影响范围，可以随便填写任何东西，commitizen也给出了几个 如: location 、browser、compile；或者可以约定为: 

        [all] 表示影响面大 ，如修改了网络框架  会对真个程序产生影响
        [loation] 表示影响小，某个小小的功能
        [module: xxx] 表示会影响某个模块 如登录模块、首页模块 、用户管理模块等等

    subject是commit的简短描述
        
#### Body

    Body 部分是对本次 commit 的详细描述，可以分成多行。

    注意: 
        使用第一人称现在时，比如使用change而不是changed或changes。
        应该说明代码变动的动机，以及与以前行为的对比。

#### Footer

    可以描写备注；如果是 bug ，可以把bug id放入

    不兼容变动
        如果当前代码与上一个版本不兼容，则 Footer 部分以BREAKING CHANGE开头，后面是对变动的描述、以及变动理由和迁移方法。
    Revert
        如果当前 commit 用于撤销以前的 commit，则必须以revert:开头，后面跟着被撤销 Commit 的 Header。
