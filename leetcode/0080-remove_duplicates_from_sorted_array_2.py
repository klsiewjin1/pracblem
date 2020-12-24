"""
Title:      Remove Duplicates from Sorted Array II
URL:        https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Space:      O(n)
Time:       O(n)
Difficulty: Medium
"""
from typing import List


class Solution:
    """
    Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
    Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        idx = len(nums) - 1
        first = False
        second = False
        while idx >= 0:
            curr = nums[idx]
            if prev is not None and prev == curr:
                if not first:
                    first = True
                else:
                    second = True
                if first and second:
                    nums.pop(idx)
            else:
                first, second = False, False
            prev = curr
            idx -= 1
        return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    test = Solution()
    test.removeDuplicates(nums)
    print(nums)
    assert (nums == [1, 1, 2, 2, 3])
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    test.removeDuplicates(nums)
    print(nums)
    assert (nums == [0, 0, 1, 1, 2, 3, 3])
