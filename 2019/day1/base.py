# -*- utf-8 -*-
"""
Day 1
-----
fuel_required = ()(mass/3) -2)

"""
import os
import csv

PWD = os.getcwd()
<<<<<<< HEAD

total_fuel = 0
module_fuel = 0
net_fuel = 0

def get_fuel_estimate(mass):
    fuel_required = int((int(mass)/3) -2)
    return fuel_required

def solve():
    with open(PWD +'/2019/day1/input.txt', 'r') as input_data:
        global primary_fuel_mass, net_fuel
        input_reader = csv.reader(input_data)
        for row in input_reader:
            primary_fuel_mass = get_fuel_estimate(row[0])
            while(primary_fuel_mass > 0):
                module_fuel += primary_fuel_mass
                primary_fuel_mass = get_fuel_estimate(primary_fuel_mass)
            net_fuel += module_fuel
            print(net_fuel)
            module_fuel = 0
    print(net_fuel)
    return (net_fuel)
=======
total_fuel = 0

def get_fuel_estimate(mass):
    fuel_required = ((int(mass)/3) -2)
    return fuel_required

with open(PWD +'/2019/day1/input.txt', 'r') as input_data:
    input_reader = csv.reader(input_data)
    for row in input_reader:
        total_fuel += get_fuel_estimate(row[0])

print(total_fuel)
>>>>>>> 3f838b8a5d0817b299a0542ce143cbaa47fab973
