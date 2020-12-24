"""
Title:      Remove Element
URL:        https://leetcode.com/problems/remove-element/
Space:      O(n)
Time:       O(n)
Difficulty: Easy
"""
from typing import List


class Solution:
    """
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        idx = len(nums) - 1
        while idx >= 0:
            if nums[idx] == val:
                nums.pop(idx)
            idx -= 1
        return len(nums)
