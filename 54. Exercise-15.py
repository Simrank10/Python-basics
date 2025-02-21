import math

def can(height, width, coverage = 7):
    no_of_can = math.ceil((height*width)/coverage)
    print(f"No. of paint cans required to paint the wall is {no_of_can}")

h = int(input("Enter the height of the wall in mts : "))
w = int(input("Enter width of the wall in mts : "))

can(height = h, width = w)
