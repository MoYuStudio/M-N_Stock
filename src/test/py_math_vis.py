
import matplotlib
import matplotlib.pyplot
import numpy as np

year_days = 365

x = np.linspace(0,year_days,year_days)
b = 2*np.pi*(x-81)/364
y = 9.87*np.sin(2*b)-7.53*np.cos(b)-1.5*np.sin(b)

print(len(y))

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()

# ,linestyle='--',color='green',marker='<'

leapYear = int(input("Input a Year "))

if leapYear %4 == 0:
    print("Its a leap year")
else:
    print ("Its a normal year")