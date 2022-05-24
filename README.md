
# Man and Nature Stock

## About

    天人合一 玄学炒股 永远满仓 永远热泪盈眶 awe

项目大纲: [Outline](https://github.com/MoYuStudio/M-N_Stock/blob/main/note/outline)<br/>
项目笔记: [Note](https://github.com/MoYuStudio/M-N_Stock/blob/main/note/note)<br/>

## 引索

>
> [`Official Documentation`](#OfficialDocumentation) 官方文档<br/>
>
>> [`API`](#API) 接口<br/>
>>
>>> [`Module`](#APIModule) 模块<br/>
>>>
>>>> [`utc_offset`](#APIModule_utc_offset) UTC时区均时差计算 <br/>
>>>> [`day_convert`](#APIModule_day_convert) 公历转换干支历 <br/>
>
> [`Rule`](#Rule) 格式规范<br/>
> 
>> [`MoYuStudio Python Code Rule`](#MoYuStudio_Python_Code_Rule) MoYuStudio Python代码编写格式规范<br/>
>> [`MoYuStudio Name Rule`](#MoYuStudio_Name_Rule) MoYuStudio 命名格式规范<br/>
>> [`MoYuStudio Git Commit Message Rule`](#MoYuStudio_Git_Commit_Message_Rule) MoYuStudio Git提交备注格式规范 (借鉴 Angular 团队的 Commit 规范)<br/>


## <span id = 'OfficialDocumentation'>`Official Documentation`</span> 官方文档

### <span id = 'API'>`API`</span> 接口

#### <span id = 'APIModule'>`Module`</span> 模块

#### <span id = 'APIModule_utc_offset'>`utc_offset`</span> UTC时区均时差计算

    功能:  UTC时区均时差计算

    实例化:  uo = utc_offset.UTCOffset()

    变量: 
        self.UTC [datetime.datetime] # UTC时间
        self.LMT [datetime.datetime] # 本地时间
        self.UTC_offset [float] # UTC时区均时差
        self.true_solar_time [datetime.datetime] # 真太阳时

    调用: 
        None

#### <span id = 'APIModule_day_convert'>`day_convert`</span> 公历转换干支历

    功能:  公历转换干支历

    实例化:  dc = day_convert.DayConvert(year, month, day, hour, min, sec)

    变量: 
        self.year_gan [str] # 年干
        self.month_gan [str] # 月干
        self.day_gan [str] # 日干
        self.hour_gan [str] # 时干

    调用: 
        self.run()
            转换干支历


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
