"""
Title: Max Min
URL: https://www.hackerrank.com/challenges/angry-children/problem


Comment: The minimum fairness will always be from consecutive numbers of an ordered list.
So the first step is to sort the array.
Once the list is sorted, the problem is fairly straightforward. Iterate through array taking k elements at a time
and finding the difference between the min and max. However, this simply brute forces through the array. A slightly
smarter approach can be made. Since the difference between the min and the max will always be from the first and last
element, simply get the difference between those elements instead of going through all the elements in the sub-array.
"""

# !/bin/python3

import os


def get_max_min(*args):
    return max(*args) - min(*args)


# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    max_min = []
    for x in range(len(arr) - k + 1):
        max_min.append(get_max_min(arr[x], arr[x + k - 1]))
    return min(max_min)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
