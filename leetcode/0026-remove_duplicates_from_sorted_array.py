"""
Title:      Remove Duplicates from Sorted Array
URL:        https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Space:      O(n)
Time:       O(n)
Difficulty: Easy
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        idx = len(nums) - 1
        while idx >= 0:
            if prev is not None and prev == nums[idx]:
                nums.pop(idx)
            prev = nums[idx]
            idx -= 1
        return len(nums)
