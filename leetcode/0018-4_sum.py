"""
Title:      4Sum
URL:        https://leetcode.com/problems/4sum/
Space:
Time:       O(n^2)
Difficulty: Medium
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(nums, target, N, result, results):
            # print(target, nums, N)
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                # First 2 conditions are self explanatory
                # if minimum possible sum (every element is first element) > target
                # or maximum possible sum (every element is first element) < target, impossible to get target anyway
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
        findNSum(sorted(nums), target, 4, [], results)
        return results


if __name__ == "__main__":
    test = Solution()
    res = test.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
    print(res)
