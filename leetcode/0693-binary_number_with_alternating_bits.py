class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = bin(n)
        i = len(tmp) - 1
        while i > 2:
            if tmp[i] == tmp[i - 1]:
                return False
            i -= 1
        return True
