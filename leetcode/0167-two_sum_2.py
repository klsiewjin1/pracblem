"""
Title:      Two Sum II - Input Array is sorted
URL:        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Space:      O(n)
Time:       O(n)
Difficulty: Easy
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dict with entries (value-index)
        holder = {}
        for idx, elem in enumerate(nums):
            diff = target - elem
            if diff in holder:
                return [holder[diff] + 1, idx + 1]
            else:
                holder[elem] = idx
