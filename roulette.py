import random 
import math
import numpy as np
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

def roulette(n):
    results = []
    count = 0
    for i in range(1, n):
        roll = random.randint(1, 38)
        if roll <= 18:
            count += 1
            results.append(count / i)
        else:
            count -= 1
            results.append(count / i)
    return results
results = []
for i in range(200):
    results.append(roulette(100)[-1])

hist, boundaries = np.histogram(results, bins=10, range=(math.floor(min(results)), math.ceil(max(results))))
xVals = (boundaries[:-1] + boundaries[1:]) / 2

hist_plot = figure(title="Roulette Histogram", x_axis_label='Value', y_axis_label='Frequency')
hist_plot.vbar(x=xVals, top=hist, width=(boundaries[1] - boundaries[0]), line_color="white")


line_plot = figure(title="Rouletten Line Graph", x_axis_label='Frequency', y_axis_label='Result')
line_plot.line(range(1, 201), results, line_width=2)


grid = gridplot([[hist_plot, line_plot]])
show(grid)