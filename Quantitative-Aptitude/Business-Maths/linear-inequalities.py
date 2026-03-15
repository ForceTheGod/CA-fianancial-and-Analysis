# demonstrating the feasible region of two curves using matplotlib
# 35 - x = y
# 50 - 2x = y

import numpy as np
import matplolib.pyplot as plt

x = np.linspace(0,50,1000)
y = 35 - x

x_1 = np.linspace(0,50,1000)
y_1 = 50 - 2 * x


figure, axe = plt.subplots(figsize = (7,7), layout = "tight")
axe.plot(x,y,label = "Equation 1")
axe.plot(x_1, y_1, label = "Equation 2")
axe.legend()
axe.grid()

y_feasible = np.minimum(y, y_1)
y_feasible = np.maximum(y_feasible, 0)
axe.fill_between(x, 0, y_feasible, color='green', alpha=0.3, label="Feasible Region")
axe.legend()
