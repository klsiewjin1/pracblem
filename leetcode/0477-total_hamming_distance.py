from typing import List

from leetcode import convert_int_to_32_bit


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        Brute force method
        Time: O(n ^ 2)
        Space: O(1)
        """
        distance = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                distance += bin(nums[i] ^ nums[j]).count("1")
        return distance

    def totalHammingDistance_2(self, nums: List[int]) -> int:
        """
        Count the number of zeros and ones for each i-th bit in every num in nums and multiply them.
        This will be the Hamming distance for the i-th bit. Calculate for every bit and sum them up.
        Instead of runtime O(n^2), this will be reduced to O(32 * n) which is O(n)
        """
        new_nums = list(map(lambda x: convert_int_to_32_bit(x), nums))
        counter = 0
        for i in range(32):
            zeros = 0
            ones = 0
            for n in new_nums:
                tmp = n[i]
                if tmp == "0":
                    zeros += 1
                else:
                    ones += 1
            counter += zeros * ones
        return counter