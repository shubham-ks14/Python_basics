#program to illustrate module

import math


def Main():
    num = float(input("Enter the number: "))
    #fabs is used to get absolute value of a decimal number
    num = math.fabs(num)
    print(num)

if __name__ == "__main__":
    Main()


