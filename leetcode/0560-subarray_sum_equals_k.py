"""
Title:      Subarray Sum Equals K
URL:        https://leetcode.com/problems/subarray-sum-equals-k/
Space:      O(n)
Time:       O(n)
Difficulty: Medium
Comments: As we go through the list, if the 'running_sum' increases by k, we have found a subarray of sums == k
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        running_sum = 0
        hash_table = defaultdict(lambda: 0)
        for elem in nums:
            running_sum += elem
            diff = running_sum - k
            if running_sum == k:
                total += 1
            if diff in hash_table:
                total += hash_table[diff]
            hash_table[running_sum] += 1

        return total
