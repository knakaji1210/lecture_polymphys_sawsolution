# Function to draw 2d Self-Avoiding Walk from Random Points (Square Lattice model)

# 周期的境界条件の設定（v3）
# coordinateXY_listを使わない計算

import sys
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import saw2dFuncM_v3 as saws

try:
    lattice_x = int(input('X-Lattice Size (default=20): '))
except ValueError:
    lattice_x = 20

try:
    lattice_y = int(input('Y-Lattice Size (default=20): '))
except ValueError:
    lattice_y = 20

try:
    N = int(input('Degree of Polymerization (default=10): '))
except ValueError:
    N = 10

try:
    M = int(input('Number of Polymer Chains (default=2): '))
except ValueError:
    M = 2

Phi = N * M /  lattice_x /  lattice_y

# 初期の点も数に含めるため
N = N - 1

initial_coordinate_list = []
occupied_coordinate_list = []

m = 0

while m < M:
    x_init = int(rd.random()*lattice_x)
    y_init = int(rd.random()*lattice_y)
    coordinate_init = [x_init,y_init]
    if coordinate_init in occupied_coordinate_list:
        print("initial point failure")
        m = m
    else:
        print("initial point success")
        initial_coordinate_list.append(coordinate_init)
        occupied_coordinate_list = saws.saw2dFuncM(lattice_x, lattice_y, coordinate_init, occupied_coordinate_list, N)
        m += 1

if not len(occupied_coordinate_list) == M * (N + 1):
    print("total failure")
    sys.exit()

print("initial coordinate: ", initial_coordinate_list)

# coordinate_listなどをintのまま利用したいため、別途coordinateFloat_listを用意
occupied_sites_list = [list(map(float, coordinate)) for coordinate in occupied_coordinate_list]
occupied_sites_list = [list(map(lambda x: x+0.5, coordinateFloat)) for coordinateFloat in occupied_sites_list]

fig = plt.figure(figsize=[8,8])

ax_title = "2d Self-Avoiding Walk ({0}x{1} square lattice, $N$ = {2}, $M$ = {3})".format(lattice_x, lattice_y, N+1, M)
ax = fig.add_subplot(111,title=ax_title, xlabel='$X$', ylabel='$Y$',
                      xlim=[0, lattice_x], ylim=[0, lattice_y])
ax.grid(visible=True, which='major', color='#999999', linestyle='-', linewidth=10/lattice_x)
ax.set_xticks(np.linspace(0, lattice_x, lattice_x+1))
ax.set_xticklabels([])
ax.set_yticks(np.linspace(0, lattice_y, lattice_y+1))
ax.set_yticklabels([])

# 占有点・非占有点の描画
for i in range(lattice_x):
    for j in range(lattice_y):
        x = i
        y = j
        coordinate = [x, y]
        if coordinate in occupied_coordinate_list:
            ax.plot(x+0.5, y+0.5, marker="o", color="red", markersize=200/lattice_x)
        else:
            ax.plot(x+0.5, y+0.5, marker="o", color="blue", markersize=160/lattice_x)

# 占有点間を繋ぐ線の描画（周期的境界条件に対応）
for j in range(M):
    saw_chain_list = [occupied_sites_list[k] for k in range(j*(N+1), (j+1)*(N+1))]
    for l in range(N):
        if abs(saw_chain_list[l+1][0]-saw_chain_list[l][0]) <= 1 and abs(saw_chain_list[l+1][1]-saw_chain_list[l][1]) <= 1:
            plt.plot([saw_chain_list[l][0], saw_chain_list[l+1][0]], [saw_chain_list[l][1], saw_chain_list[l+1][1]], color="red",  linewidth=50/lattice_x)

result_text = "Φ = {}".format(Phi)
fig.text(0.75, 0.05, result_text, size=15)

savefile = "./png/SAW_2dSquareLattice_{0}x{1}_N{2}_M{3}.png".format(lattice_x, lattice_y, N+1, M)
fig.savefig(savefile, dpi=300)

plt.show()
