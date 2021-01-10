class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 != 0 or n <= 0:
            return False
        return self.isPowerOfTwo(int(n / 2))

    def isPowerOfTwo_v2(self, n: int) -> bool:
        """
        If n = 16, bitwise represented as b10000
        n-1 = 15, bitwise represented as b01111
        Bitwise AND will return 0
        """
        return n > 0 and not (n & n - 1)
