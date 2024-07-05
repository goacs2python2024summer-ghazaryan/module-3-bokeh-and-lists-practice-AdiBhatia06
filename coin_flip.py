#Flip a coin a hundred times, and record how mnay times it lands head, and show that in a histogram.

import random 
import math
import numpy as np
from bokeh.plotting import figure, show

def coin_flip(n):
    results = []
    head_count = 0
    for i in range(1, n + 1):
        flip = random.choice(["Heads", "Tails"])
        if flip == "Heads":
            head_count += 1
        else:
            head_count += 0
        results.append(head_count)
        
    print(f"Head Count: {head_count}")
    print(f"Tail Count: {tail_count}")

    hist = np.histogram(results, bins=5, range=(math.floor(min(results)), math.floor(max(results))))
    print(hist)
    yVals = hist[0]
    xVals = hist[1]
    XBarWidth = xVals[1] - xVals[0]
    xVals = xVals + XBarWidth / 2
    xVals = xVals[:-1]
    print(xVals)

    # Plot the histogram using Bokeh
    f = figure(title="Head Count", x_axis_label='Heads Count', y_axis_label='Frequency')
    for x, y in zip(xVals, yVals):
        f.vbar(x=x, width=XBarWidth, top=y, line_color="white")

    show(f)

# Test the function
coin_flip(100)