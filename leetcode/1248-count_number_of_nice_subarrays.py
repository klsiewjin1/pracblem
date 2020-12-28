"""
Title:      Count Number of Nice Subarrays
URL:        https://leetcode.com/problems/count-number-of-nice-subarrays/
Space:      O(n)
Time:       O(n)
Difficulty: Medium
"""
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        lower_boundary = -1
        left_most_odd_numbered_idx = 0
        for num in nums:
            k -= num % 2  # when k = 0, we have reached a point where the nice subarray criteria is true
            if nums[left_most_odd_numbered_idx] % 2 == 0:
                # Move to index of the left most odd number
                left_most_odd_numbered_idx += 1
            if k < 0:
                # Too many odd numbers in the subarray, update the lower boundary to the left most odd number index
                lower_boundary = left_most_odd_numbered_idx
            while k < 0:  # return k to 0
                left_most_odd_numbered_idx += 1
                k += nums[left_most_odd_numbered_idx] % 2  # add to k if num is odd
            if k == 0:
                total += left_most_odd_numbered_idx - lower_boundary
        return total


if __name__ == "__main__":
    test = Solution()
    ans = test.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)
    print("ASD")
    print(ans)
