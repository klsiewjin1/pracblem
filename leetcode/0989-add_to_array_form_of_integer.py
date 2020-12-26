"""
Title:      Add to Array-Form of Integer
URL:        https://leetcode.com/problems/add-to-array-form-of-integer/
Space:      O(n)
Time:       O(n)
Difficulty: Easy
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a, result = "", []
        for elem in A:
            a += str(elem)
        total = str(int(a) + K)
        for elem in total:
            result.append(int(elem))
        return result
