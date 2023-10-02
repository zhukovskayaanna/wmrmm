import math
x=float(0.4*10**4)
y=float(-0.875)
z=float(-0.475*10**(-3))
s=float(((abs(math.cos(x)-math.cos(y)))**(1+2*(math.sin(y))**2))*(1+z+(z**2/2)+(z**3/3)+(z**4/4)))
