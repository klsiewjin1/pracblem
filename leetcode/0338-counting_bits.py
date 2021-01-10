from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i & (i - 1)] + 1  # Brian Kernighan's Algorithm
        return result
