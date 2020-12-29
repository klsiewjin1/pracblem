"""
Title:      Subarrays with K Different Integers
URL:        https://leetcode.com/problems/subarrays-with-k-different-integers/
Space:
Time:       O(n), makes 2 passes over A
Difficulty: Hard
"""
import collections
from typing import List


class Solution:
    # def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
    # """
    # # Result != 27 due to the indiscriminate addition to result even when subarrays do not have K distinct elements
    # # For example, when the idx is at 5, the subarrays counted are [2,2,1,2,2], [2,1,2,2], [1,2,2], [2,2]
    # # The last subarray does not meet the criteria but is counted in anyway
    # """
    #     lower_bound, upper_bound = 0, 0
    #     seen = set()
    #     result = 0
    #     for idx, elem in enumerate(A):
    #         seen.add(elem)
    #         if len(seen) > K:
    #             # Update lower bound to the index of the last element that makes len(seen) == K
    #             while len(set(A[lower_bound:idx + 1])) > K:
    #                 lower_bound += 1
    #             print(f"Removing {A[lower_bound - 1]} from seen set")
    #             print(f"Lower bound is now at index {lower_bound}")
    #             seen.remove(A[lower_bound - 1])
    #
    #         if len(seen) == K:
    #             print("Adding from ", idx, lower_bound)
    #             # Add the correct amount
    #             result += idx - lower_bound - K + 2
    #
    #     return result

    def subarraysWithAtMostKDistinct(self, A: List[int], K: int) -> int:
        """
        Timed out, passed 52/55 test cases
        """
        lower_bound, upper_bound = 0, 0
        seen = set()
        result = 0
        for idx, elem in enumerate(A):
            seen.add(elem)
            if len(seen) > K:
                # Update lower bound to the index of the last element that makes len(seen) == K
                while len(set(A[lower_bound:idx + 1])) > K:  # This part probably killing it
                    lower_bound += 1
                # print(f"Removing {A[lower_bound - 1]} from seen set")
                # print(f"Lower bound is now at index {lower_bound}")
                seen.remove(A[lower_bound - 1])
            if len(seen) <= K:
                # print("Adding from ", idx, lower_bound)
                # Add the correct amount
                result += idx - lower_bound
        return result

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        a = self.atMostK(A, K)
        b = self.atMostK(A, K - 1)
        # print(a, b)
        result = a - b
        return result

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0:
                # If A[j] is a new distinct, decrease K since we need to find K-1 distinct elements
                K -= 1
            count[A[j]] += 1  # Increment the count of A[j]
            while K < 0:
                count[A[i]] -= 1  # Lower boundary
                if count[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res


if __name__ == "__main__":
    test = Solution()
    result = test.subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=2)
    print(result)
    assert (result == 7)

    result = test.subarraysWithKDistinct(A=[1, 2, 1, 3, 4], K=3)
    print(result)
    assert result == 3

    result = test.subarraysWithKDistinct(A=[2, 2, 1, 2, 2, 2, 1, 1], K=2)
    print(result)
    assert result == 23
