"""
Title:      Rotate Image
URL:        https://leetcode.com/problems/rotate-image/
Space:
Time:
Difficulty: Medium
"""

from typing import List


def swap_symmetry(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            # print(f"Swapping {i}{j} with {j}{i}")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotate_clockwise(matrix: List[List[int]]):
    """
    Reverse the x-axis and swap the symmetry
    1 2 3     7 8 9     7 4 1
    4 5 6  => 4 5 6  => 8 5 2
    7 8 9     1 2 3     9 6 3
    :param matrix:
    :return:
    """
    matrix.reverse()
    swap_symmetry(matrix)


def rotate_anticlockwise(matrix):
    """
    Reverse the y-axis and swap the symmetry
    1 2 3     3 2 1     3 6 9
    4 5 6  => 6 5 4  => 2 5 8
    7 8 9     9 8 7     1 4 7
    :return:
    """
    for i in range(len(matrix)):
        start, end = 0, len(matrix) - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1
    swap_symmetry(matrix)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotate_clockwise(matrix)


if __name__ == "__main__":
    two_by_two = [[1, 2], [3, 4]]
    test = Solution()
    rotate_clockwise(two_by_two)
    print(two_by_two)
    three_by_three = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_anticlockwise(three_by_three)
    print(three_by_three)
