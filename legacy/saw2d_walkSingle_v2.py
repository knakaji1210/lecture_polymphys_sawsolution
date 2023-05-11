# Function to draw 2d Self-Avoiding Walk from a Random Point (Square Lattice model)

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import saw2dFuncS_v2 as saws

try:
    lattice_x = int(input('X-Lattice Size (default=40): '))
except ValueError:
    lattice_x = 40

try:
    lattice_y = int(input('Y-Lattice Size (default=40): '))
except ValueError:
    lattice_y = 40

try:
    N = int(input('Degree of Polymerization (default=20): '))
except ValueError:
    N = 20

# 初期の点も数に含めるため
N = N - 1

x_init = int((rd.random()-0.5)*lattice_x/2)
y_init = int((rd.random()-0.5)*lattice_y/2)
coordinate_init = [x_init,y_init]

coordinate_list, coordinateS_list = saws.saw2dFuncS(coordinate_init, N)

x_list = coordinateS_list[0]
y_list = coordinateS_list[1]

ax_title = "2d Self-Avoiding Walk ({0}x{1} square lattice, $N$ = {2})".format(lattice_x, lattice_y, N+1)

fig = plt.figure(figsize=[8,8])
ax = fig.add_subplot(111,title=ax_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[-lattice_x/2, lattice_x/2], ylim=[-lattice_y/2, lattice_y/2])
ax.grid(b=True, which='major', color='#999999', linestyle='-', linewidth=10/lattice_x)
ax.set_xticks(np.linspace(-lattice_x/2, lattice_x/2, lattice_x+1))
ax.set_xticklabels([])
ax.set_yticks(np.linspace(-lattice_y/2, lattice_y/2, lattice_y+1))
ax.set_yticklabels([])

# 非占有点の描画
for i in range(lattice_x):
    for j in range(lattice_y):
        x = i-lattice_x/2 + 0.5
        y = j-lattice_y/2 + 0.5
        coordinate = [x, y]
        if coordinate in coordinate_list:
            pass
        else:
            ax.plot(x, y, marker="o", color="blue", markersize=160/lattice_x)

# 占有点の描画
for i in range(N+1):
    plt.plot(x_list[i], y_list[i], marker="o", color="red", markersize=200/lattice_x)

# 占有点間を繋ぐ線の描画
plt.plot(x_list, y_list, color="red")

savefile = "./png/SAW_2dSquareLattice_{0}x{1}_N{2}.png".format(lattice_x, lattice_y, N+1)
fig.savefig(savefile, dpi=300)

plt.show()