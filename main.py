
#-*-coding:utf-8-*-

import src.module as m

op = m.Output()
op.eot = m.equation_of_time.EquationOfTime(2000,7,2,0,0,0,timezone='Europe/London')
op.run()