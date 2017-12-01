'''
Source: ACM Mid-Atlantic United States 2001.
IDs for online judges: POJ 1005, ZOJ 1049, UVA 2363.

I Think I Need a Houseboat
problem
Fred Mapper is considering purchasing some land in Louisiana to build his house on. In the
process of investigating the land, he learned that the state of Louisiana is actually shrinking by
50 square miles each year, due to erosion caused by the Mississippi River. Since Fred is hoping to
live in this house for the rest of his life, he needs to know if his land is going to be lost to erosion.
After doing more research, Fred has learned that the land that is being lost forms a semicircle.
This semicircle is part of a circle centered at (0, 0), with the line that bisects the circle being the X
axis. Locations below the X axis are in the water. The semicircle has an area of 0 at the beginning
of year 1.
Input
The first line of input will be a positive integer indicating how many data sets will be included (N).
Each of the next N lines will contain the X and Y Cartesian coordinates of the land Fred is
considering. These will be floating-point numbers measured in miles. The Y coordinate will be
nonnegative. (0, 0) will not be given.
output
For each data set, a single line of output should appear. This line should take the form of
Property N: This property will begin eroding in year Z.
where N is the data set (counting from 1) and Z is the first year (start from 1) this property will be
within the semicircle AT THE END OF YEAR Z. Z must be an integer. After the last data set,
this should print out “END OF OUTPUT.”
samples:
2
1.0 1.0  Property 1: This property will begin eroding in year 1.
25.0 0.0 Property 2: This property will begin eroding in year 20.
         END OF OUTPUT.


Analysis:Solution
The number of test cases n is given. Therefore, a for repetition statement is used to deal with all test
cases. Each test case contains only X and Y Cartesian coordinates. The ith test case (Xi, Yi) and the
center of the circle (0, 0) constitute the semicircle that will be eroded. Each year 50 square miles
of land is eroded. And the number of years is an integer. When (Xi, Yi) is in water, the number of
years must be the least integer that is greater than
Area of the semicircle / 50
and function ceil(x) is used to round up the fare.
'''
from sys import stdin
from math import ceil

M_PI = 3.14159265
nos_of_tests = int(stdin.readline())
for i in range(1, nos_of_tests+1):
    x, y = list(map(float, stdin.readline().strip().split()))
    calc = (x*x + y*y)* M_PI / 2 / 50
    years = ceil(calc)
    print("Property {}: This property will begin eroding in year {}.".format( i, years))
print("END OF OUTPUT")




