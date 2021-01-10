"""
Title:      Container With Most Water
URL:        https://leetcode.com/problems/container-with-most-water/
Space:
Time:
Difficulty: Medium
Comments: Intuition is that the wider apart it is, the larger the volume
The volume is calculated only from with width (R index - L index) * min(height[L], height[R])
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        res = 0
        for w in range(R - L, 0, -1):
            if height[L] < height[R]:
                res = max(res, height[L] * w)
                L += 1
            else:
                res = max(res, height[R] * w)
                R -= 1
        return res
