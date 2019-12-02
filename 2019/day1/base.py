# -*- utf-8 -*-
"""
Day 1
-----
fuel_required = ()(mass/3) -2)

"""
import os
import csv

PWD = os.getcwd()
total_fuel = 0

def get_fuel_estimate(mass):
    fuel_required = ((int(mass)/3) -2)
    return fuel_required

with open(PWD +'/2019/day1/input.txt', 'r') as input_data:
    input_reader = csv.reader(input_data)
    for row in input_reader:
        total_fuel += get_fuel_estimate(row[0])

print(total_fuel)
