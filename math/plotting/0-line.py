#!/usr/bin/env python3
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)  # x values from 0 to 10

plt.plot(x, y, 'r-')  # 'r-' means red solid line
plt.xlim(0, 10)       # Set x-axis limits
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^3')
plt.grid(True)
plt.show()
