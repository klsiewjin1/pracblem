"""
Title:      Maximum Erasure Value
URL:        https://leetcode.com/problems/maximum-erasure-value/
Space:      O(n)
Time:       O(n)
Difficulty: Medium
"""
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result, curr, i = 0, 0, 0
        seen = set()
        for j in range(len(nums)):
            if nums[j] in seen:
                curr -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            curr += nums[j]
            result = max(result, curr)
        return result
