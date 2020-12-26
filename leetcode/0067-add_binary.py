"""
Title:      Add Binary
URL:        https://leetcode.com/problems/add-binary/
Space:      O(n)
Time:       O(n)
Difficulty: Medium
"""


class Solution:
    """Given two binary strings a and b, return their sum as a binary string."""

    def addBinary(self, a: str, b: str) -> str:
        a_equivalent = self.convert_str_to_int_equivalent(a)
        b_equivalent = self.convert_str_to_int_equivalent(b)

        return str(bin(a_equivalent + b_equivalent))[2:]

    @staticmethod
    def convert_str_to_int_equivalent(bin_str) -> int:
        idx = len(bin_str) - 1
        p = 0
        total = 0
        while idx >= 0:
            total += int(bin_str[idx]) * pow(2, p)
            p += 1
            idx -= 1
        return total

    def addBinary2(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
