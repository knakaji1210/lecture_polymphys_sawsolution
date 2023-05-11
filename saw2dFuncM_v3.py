# Function to draw 2d Self-Avoiding Walk (Square Lattice model)

# 周期的境界条件の設定（v3）
# coordinateXY_listを使わない計算

import random as rd
from math import *

def saw2dFuncM(lattice_x, lattice_y, coordinate_init, occupied_coordinate_list, N):

    num = 0
    num_f = 0

    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    while num < N:
        num = 0
        rep = 0 # 経路を探せなかったときの繰り返し回数
        x, y = coordinate_init[0], coordinate_init[1]
        x_list = [x]
        y_list = [y]
        coordinate_list = [[x,y]]      
        coordinate_list = occupied_coordinate_list + coordinate_list
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
            occupied_coordinate_list = coordinate_list
        else:
            print("final num = {}: failure".format(num+1)) # to check the number of steps
            num_f = num_f + 1
            if num_f == 100:
                print("num_f = {}".format(num_f))
                break

    return occupied_coordinate_list