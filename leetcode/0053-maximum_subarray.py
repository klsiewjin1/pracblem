"""
Title:      Maximum Subarray
URL:        https://leetcode.com/problems/maximum-subarray/
Space:      O(1)
Time:       O(n)
Difficulty: Easy
Comments: https://en.wikipedia.org/wiki/Maximum_subarray_problem
Tags: 'Kadane's algorithm'
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = curr_sum = nums[0]
        for x in nums[1:]:
            curr_sum = max(x, curr_sum + x)
            best_sum = max(curr_sum, best_sum)
        return best_sum
