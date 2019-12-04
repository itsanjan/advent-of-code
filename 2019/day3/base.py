# -*- utf-8 -*-
"""
Day 3
-----
Manhattan distance
Directions :
 U
L R
 D
R3 : O-3->

EX: X (3,3) : distance is 3+3 = 6
"""

import os
import csv
import unittest

PWD = os.getcwd()

class plotter():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dataSet = self.read_input()

    def reload_input(self):
        self.dataSet = self.read_input()
        self.x = 0
        self.y = 0

    def read_input(self):
        with open(PWD +'/2019/day3/input.txt', 'r') as input_data:
            input_reader = csv.reader(input_data)
            for row in input_reader:
                pass
            return row

    def get_distance(self, x, y, x_ref, y_ref):
        return abs(x-x_ref) + abs(y-y_ref)

    def get_ship_distance(self):
        # print(self.x, self.y)
        return self.get_distance(self.x, self.y, 0, 0)

    def navigate(self, directive):
        direction = directive[0]
        steps = directive[1:]
        # print(direction, steps)
        if direction == 'R':
            self.x +=int(steps)
        if direction == 'L':
            self.x -=int(steps)
        if direction == 'U':
            self.y +=int(steps)
        if direction == 'D':
            self.y -=int(steps)

### P1
sln = plotter()

# for element in sln.dataSet
for i in range(0, len(sln.dataSet)):
    sln.navigate(sln.dataSet[i])

print(sln.get_ship_distance())
