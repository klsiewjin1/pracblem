"""
URL: https://www.hackerrank.com/challenges/crush/

Comment: Instead of adding every single element to the array, merely keep track of the relative
"""


def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for query in queries:
        a, b, k = query
        a -= 1  # index 0
        arr[a] += k
        arr[b] -= k

    running_count, largest = 0, 0
    for elem in arr:
        running_count += elem
        largest = max(largest, running_count)
    return largest
