class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1])
        if result > 2147483647 or result < -2147483648:
            return 0
        return result * sign
