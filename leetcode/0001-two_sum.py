"""
Title:      Two Sum
URL:        https://leetcode.com/problems/two-sum/
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
                return [holder[diff], idx]
            else:
                holder[elem] = idx
