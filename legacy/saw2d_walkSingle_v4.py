# Function to draw 2d Self-Avoiding Walk from a Random Point (Square Lattice model)

# 周期的境界条件の設定（v4）

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import saw2dFuncS_v4 as saws

try:
    lattice_x = int(input('X-Lattice Size (default=40): '))
except ValueError:
    lattice_x = 40

try:
    lattice_y = int(input('Y-Lattice Size (default=40): '))
except ValueError:
    lattice_y = 40

try:
    N = int(input('Degree of Polymerization (default=30): '))
except ValueError:
    N = 30

# 初期の点も数に含めるため
N = N - 1

x_init = int(rd.random()*lattice_x)
y_init = int(rd.random()*lattice_y)
coordinate_init = [x_init,y_init]

coordinate_list, coordinateXY_list = saws.saw2dFuncS(lattice_x, lattice_y, coordinate_init, N)

# coordinate_listなどをintのまま利用したいため、別途coordinateFloat_listを用意

coordinateFloat_list = [list(map(float, coordinate)) for coordinate in coordinate_list]
coordinateFloat_list = [list(map(lambda x: x+0.5, coordinateFloat)) for coordinateFloat in coordinateFloat_list]

coordinateXYFloat_list = [list(map(float, coordinateXY)) for coordinateXY in coordinateXY_list]
coordinateXYFloat_list = [list(map(lambda x: x+0.5, coordinateXYFloat)) for coordinateXYFloat in coordinateXYFloat_list]

x_list = coordinateXYFloat_list[0]
y_list = coordinateXYFloat_list[1]

ax_title = "2d Self-Avoiding Walk ({0}x{1} square lattice, $N$ = {2})".format(lattice_x, lattice_y, N+1)

fig = plt.figure(figsize=[8,8])
ax = fig.add_subplot(111,title=ax_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[0, lattice_x], ylim=[0, lattice_y])
ax.grid(b=True, which='major', color='#999999', linestyle='-', linewidth=10/lattice_x)
ax.set_xticks(np.linspace(0, lattice_x, lattice_x+1))
ax.set_xticklabels([])
ax.set_yticks(np.linspace(0, lattice_y, lattice_y+1))
ax.set_yticklabels([])

# 非占有点の描画
for i in range(lattice_x):
    for j in range(lattice_y):
        x = i
        y = j
        coordinate = [x, y]
        if coordinate in coordinate_list:
            pass
        else:
            ax.plot(x+0.5, y+0.5, marker="o", color="blue", markersize=160/lattice_x)

# 占有点の描画
for i in range(N+1):
    plt.plot(x_list[i], y_list[i], marker="o", color="red", markersize=200/lattice_x)

# 占有点間を繋ぐ線の描画（周期的境界条件に対応）
for i in range(N):
    if abs(x_list[i+1]-x_list[i]) <= 1 and abs(y_list[i+1]-y_list[i]) <= 1:
        plt.plot([x_list[i], x_list[i+1]], [y_list[i], y_list[i+1]], color="red",  linewidth=50/lattice_x)

savefile = "./png/SAW_2dSquareLattice_{0}x{1}_N{2}.png".format(lattice_x, lattice_y, N+1)
fig.savefig(savefile, dpi=300)

plt.show()