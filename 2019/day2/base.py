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
            print(len(self.dataSet))

        def read_input(self):
            with open(PWD +'/2019/day2/input.txt', 'r') as input_data:
                input_reader = csv.reader(input_data)
                for row in input_reader:
                    pass
                return row

        def print_data(self):
            return print(self.dataSet)

        def get_value(self, pos):
            return int(self.dataSet[pos])

        def set_value(self, pos, value):
            self.dataSet[int(pos)] = int(value)

        def increment_operation_pos(self):
            self.cursor_position += 4
            return self.cursor_position

        def opcode_operator(self, operator_loc):
            if self.cursor_position >= len(self.dataSet)-1 :
                print("exit")
                return
            operation_type, v1_loc, v2_loc, op_loc = self.get_value(operator_loc), self.get_value(operator_loc+1), self.get_value(operator_loc+2), self.get_value(operator_loc+3)
            if operation_type == 1:
                #addition
                op_value = self.get_value(v1_loc) + self.get_value(v2_loc)
                self.set_value(op_loc, op_value)
                # print("::", operation_type, v1_loc, v2_loc)
                print(operation_type, op_loc, op_value)
            if operation_type == 2:
                #multiplication
                op_value = self.get_value(v1_loc) * self.get_value(v2_loc)
                self.set_value(op_loc, op_value)
                print(operation_type, op_loc, op_value)
            if operation_type == 99:
                print("***",operation_type)
                return
            return self.opcode_operator(self.increment_operation_pos())

        # def compute():
        #     for i in range(0, len(self.dataSet)-1,4)

#Solution
sln = opcode_handler()
sln.print_data()
sln.opcode_operator(0)
sln.print_data()
