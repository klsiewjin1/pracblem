from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # think of what the end results can be
        # Situation 1: no 0s in array, with even number of -ve values --> multiply every element to get max
        # Situation 2: no 0s in array, with odd number of -ve values --> multiply every element from the first
        # element after the first -ve to the end of the array or the last -ve to the start of the array
        # This is called prefix product, where an element with index i is equal to the product of all elements
        # [i-1, i-2, ..., 0] and suffix product is the reverse for [i+1, i+2, ..., N] for N elements in array
        # Situation 3: 0 in the array, we start over again from the next element
        prefix_product, suffix_product, max_so_far = 0, 0, float("-inf")
        for i in range(len(nums)):
            prefix_product = (prefix_product or 1) * nums[i]
            suffix_product = (suffix_product or 1) * nums[~i]  # tilde does bitwise not
            max_so_far = max(max_so_far, prefix_product, suffix_product)
            print("prefix product", prefix_product)
            print("suffix product", suffix_product)
        return max_so_far


if __name__ == "__main__":
    s = Solution()
    maxProduct = s.maxProduct([1, 2, -3, 10, 3, -5, 0, 5])
    print(maxProduct)
