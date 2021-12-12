"""
Matplotlib Styles:
"""

import numpy as np
import matplotlib.pyplot as plt


styles = ['default'] + plt.style.available
print(styles)
print(len(styles))

x = np.arange(-2, 8, .1)
y = .1 * x ** 3 - x ** 2 + 3 * x + 2

fig = plt.figure(dpi=100, figsize=(15, 9), tight_layout=True)
for i, style in enumerate(styles, start=1):
    with plt.style.context(style):
        ax = fig.add_subplot(4, 7, i)
        ax.plot(x, y)
    ax.set_title(style)
plt.show()

# Style's Setting:
print(plt.style.library['seaborn-darkgrid'])
