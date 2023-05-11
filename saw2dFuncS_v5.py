# Function to draw 2d Self-Avoiding Walk (Square Lattice model)

# 周期的境界条件の設定（v4）
# coordinateXY_listを使わない計算

import random as rd
from math import *

def saw2dFuncS(lattice_x, lattice_y, coordinate_init, N):

    num = 0

    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    while num < N:
        num = 0
        rep = 0 # 経路を探せなかったときの繰り返し回数
#        x, y = coordinate_init[0]+0.5, coordinate_init[1]+0.5 # v2ではこうしていた
        x, y = coordinate_init[0], coordinate_init[1]
        x_list = [x]
        y_list = [y]
        coordinate_list = [[x,y]]
        num_list = []
        while rep < 20 and num < N:
            step = rd.choice(direction_list)
            x_temp = x + step[0]
            y_temp = y + step[1]
            if x_temp >= lattice_x:
                x_temp = x_temp - lattice_x
            if x_temp < 0:
                x_temp = x_temp + lattice_x
            if y_temp >= lattice_y:
                y_temp = y_temp - lattice_y
            if y_temp < 0:
                y_temp = y_temp + lattice_y
            coordinate_temp = [x_temp, y_temp]
            if coordinate_temp in coordinate_list:
            #    x = x
            #    y = y
            #    x_list.append(x) ・・・ステイすることを示すためには必要（動画のためなのでここでは不要）
            #    y_list.append(y) ・・・ステイすることを示すためには必要（動画のためなのでここでは不要）
                num = num
                num_list.append(num)
                rep = num_list.count(num_list[-1])            
            else:
                x = x_temp
                y = y_temp
                x_list.append(x)
                y_list.append(y)
                coordinate = [x, y]
                coordinate_list.append(coordinate)
                num = num + 1 
        if num == N:
            print("final num = {}: success".format(num+1)) # to check the number of steps
        else:
            print("final num = {}: failure".format(num+1)) # to check the number of steps

    return coordinate_list