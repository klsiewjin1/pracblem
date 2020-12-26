"""
Title:      Rotate Array
URL:        https://leetcode.com/problems/rotate-array/
Space:
Time:
Difficulty: Medium
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]

    def reverse(self, nums: list, start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate_2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def rotate_3(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        start = count = 0

        while count < n:
            current_idx, prev_val = start, nums[start]
            while True:
                next_idx = (current_idx + k) % n
                nums[next_idx], prev_val = prev_val, nums[next_idx]
                current_idx = next_idx
                count += 1

                if start == count:
                    break
            start += 1
