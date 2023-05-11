# Function to draw 2d Self-Avoiding Walk (Square Lattice model)

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import saw2dFuncS_v2 as saws

fig = plt.figure()
ax = fig.add_subplot(111,title='', xlabel='X', ylabel='Y',
                      xlim=[-10, 10], ylim=[-5, 5])
ax.grid(b=True, which='major', color='#999999', linestyle='-')
ax.set_xticks(np.linspace(-10, 10, 21))
ax.set_xticklabels([])
ax.set_yticks(np.linspace(-5, 5, 11))
ax.set_yticklabels([])

N = 10
M = 2
m = 0

initial_coordinate_list = []
occupied_coordinate_list = []

while m < M:

    x_init = int((rd.random()-0.5)*20)
    y_init = int((rd.random()-0.5)*10)
    coordinate_init = [x_init,y_init]
    initial_coordinate_list.append(coordinate_init)

   # occupied_coordinate_list.append(coordinate_init) これうまくいかない・・・

    coordinate_list, coordinateS_list = saws.saw2dFuncS(coordinate_init, N)

    x_list = coordinateS_list[0]
    y_list = coordinateS_list[1]

#ここでoccupied_coordinate_listに生成された新規の経路が追加される

    for n in range(N):
        coordinate = coordinate_list[n]
        if coordinate in occupied_coordinate_list:
            pass
        else:
            occupied_coordinate_list.append(coordinate)

    check = len(occupied_coordinate_list)
    print(check)

    if check == (m+1)*N :   #ここまだ未完成
        plt.plot(x_list, y_list, color='red')
        for i in range(N+1):
            plt.plot(x_list[i], y_list[i], marker="o", color="red")
        m += 1
    else:
        m = m

print(initial_coordinate_list)

for i in range(20):
    for j in range(10):
        x = i-9.5
        y = j-4.5
        coordinate = [x, y]
        if coordinate in occupied_coordinate_list:
            pass
        else:
            ax.plot(x, y, marker=".", color="blue")

fig.savefig("./png/polmer_solution.png", dpi=300)

plt.show()
