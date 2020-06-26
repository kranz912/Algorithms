
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def helper(arr):
    sum_of_glasses = []
    for g in range(4):
        for i in range(4):
            sum_of_glass  = arr[g][i] + arr[g][i+1] + arr[g][i+2] + arr[g+1][i+1] + arr[g+2][i] + arr[g+2][i+1] + arr[g+2][i+2]
            sum_of_glasses.append(sum_of_glass)
    return max(sum_of_glasses)
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(helper(arr))
