
from re import I


import math


N = 100

B = (math.degrees(360)*(N-81))/364

E = 9.87*math.sin(2*B) - 7.53*math.cos(B) - 1.5*math.sin(B)

print(E)