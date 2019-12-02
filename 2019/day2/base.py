# -*- utf-8 -*-
"""
Day 2
-----
Intcode - List of integers seperated by comma's

EX: 1,0,0,3,99

First position is called 0 position, has opcode :
    - 1  : add nums in next 2 memory position (where the values are)
    - 2  : multiply
    - 99 : program finished
once an opcode is processed, move forward 4 positions
"""
import os
import csv

PWD = os.getcwd()

class opcode_handler():
        def __init__(self):
            self.dataSet = self.read_input()
            self.cursor_position = 0

        def read_input(self):
            with open(PWD +'/2019/day2/input.txt', 'r') as input_data:
                input_reader = csv.reader(input_data)
                for row in input_reader:
                    pass
                return row

        def print_data(self, pos):
            return self.dataSet

        def get_value(self, pos):
            return self.dataSet[pos]

        def set_value(self, pos, value):
            print(self.dataSet[10])
            self.dataSet[pos] = value
            print(self.dataSet[10])

        def increment_operation_pos(self):
            self.cursor_position += 4
            return self.cursor_position

        def opcode_operator(self, operator_loc, v1_loc, v2_loc, op_loc):
            operation_type, v1_loc, v2_loc, op_loc =
            if operation_type == 1:
                #addition
                op_value = self.get_value(v1_loc) + self.get_value(v2_loc)
                self.set_value(op_loc, op_value)
            if operation_type == 2:
                #multiplication
                op_value = self.get_value(v1_loc) * self.get_value(v2_loc)
                self.set_value(op_loc, op_value)
            if operation_type == 99:
                pass
            self.opcode_operator(increment_operation_pos())

#Solution
sln = opcode_handler()
print(sln.get_value(10))
sln.set_value(10,33)
