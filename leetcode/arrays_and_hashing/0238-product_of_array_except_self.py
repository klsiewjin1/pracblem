from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        # output elements are product of preceding elements
        # in the following loop, going backwards, multiply the
        # elements by the preceding elements

        # Numbers [1 2 3 4 5]
        # Pass 1: [- 1 12 123 1234]
        # Pass 2: [2345 345 45 5 -]
        # =========================
        # Pass 3: [2345, 1345, 1245, 1235, 1234]

        # 2nd loop is to multiply Pass 2 with Pass 1 and return Pass 3

        p = 1
        for i in range(n-1, -1, -1):
            output[i] *= p
            p *= nums[i]
            print(output[i], p)
        return output