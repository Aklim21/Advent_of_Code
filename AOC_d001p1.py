'''
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
'''

#pandas provides the import data ability
#math gives us the rounding ability

import pandas as pd
import math 

mydata = pd.read_csv("C:\\Users\\antho\\Google Drive\\Work\\Python\\Scripts\\AOC_d1.csv", header = None)

#function returns all the data from the csv as a list of ints.
def formatData(data):
    x=[]
    for i in data[0]:
        x.append(i)
    return x
print(len(formatData(mydata)))
#function to iterate the formula over the given dataset
def findFuel(data):
    tot = 0
    for i in data:
        x = (math.floor(i/3)-2)
        tot = tot + x
    return tot


print(findFuel(formatData(mydata)))
        