import math
x=float(3.74*(10**(-2)))
y=float(-0.825)
z=float(0.16*10**2)
s=float((1+((math.sin(x+y))**2))/(abs(x-((2*y)/(1+x**2*y**2))))*(x**(abs(y))))+(math.cos(math.atan(1/z)))**2
print(round(s,5))