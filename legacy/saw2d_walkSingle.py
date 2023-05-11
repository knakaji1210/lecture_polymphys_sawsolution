# Function to draw 2d Self-Avoiding Walk (Square Lattice model)

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import saw2dFuncS_new as saws

fig = plt.figure()
ax = fig.add_subplot(111,title='', xlabel='X', ylabel='Y',
                      xlim=[-10, 10], ylim=[-5, 5])
ax.grid(b=True, which='major', color='#999999', linestyle='-')
ax.set_xticks(np.linspace(-10, 10, 21))
ax.set_xticklabels([])
ax.set_yticks(np.linspace(-5, 5, 11))
ax.set_yticklabels([])


N = 15

x_init = int((rd.random()-0.5)*20)
y_init = int((rd.random()-0.5)*10)
coordinate_init = [x_init,y_init]

coordinate_list, coordinateS_list = saws.saw2dFuncS(coordinate_init, N)
#print(coordinate_list)
#print(coordinateS_list)

x_list = coordinateS_list[0]
y_list = coordinateS_list[1]

plt.plot(x_list, y_list, color="red")

for i in range(N+1):
    plt.plot(x_list[i], y_list[i], marker="o", color="red")

plt.show()