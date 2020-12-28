"""
Title:      3Sum
URL:        https://leetcode.com/problems/3sum/
Space:
Time:
Difficulty: Medium
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findNSum(nums, target, N, result, results):
            # print(target, nums, N)
            if len(nums) < N or N < 2:
                return
            if N == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum == target:
                        results.append(result + [nums[left], nums[right]])
                        # print(results)
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNSum(sorted(nums), 0, 3, [], results)
        return results
