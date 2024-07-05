import random 
import math
import numpy as np
from bokeh.plotting import figure, show


def dice_difference(n):
  results=[]
  for i in range (n): 
    r1 =random.randint(1,6)
    r2=random.randint(1,6)
    total=abs(r1-r2)
    results.append(total)

  return results
results = dice_difference(100)
print(results)



hist= np.histogram(results, bins=5, range=(math.floor(min(results)),math.floor(max(results))))
print (hist)
yVals=hist[0]
xVals=hist[1]
XBarWidth=xVals[1]-xVals[0]
xVals= xVals+XBarWidth/2
xVals=xVals[0:-1]
print(xVals)

f= figure()
for x, y in zip (xVals,yVals):
    f.vbar(x,XBarWidth,y, line_color= "white")

show(f)