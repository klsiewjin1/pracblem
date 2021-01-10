class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(int(str(n)))).count("1")