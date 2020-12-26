"""
Title:      Add Strings
URL:        https://leetcode.com/problems/add-strings/
Space:      O(n)
Time:       O(n)
Difficulty: Easy
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))