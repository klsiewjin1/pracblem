"""
Title:      Palindrome Number
URL:        https://leetcode.com/problems/palindrome-number/
Space:      O(n)
Time:       O(n)
Difficulty: Easy
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert to String, split in the middle and reverse one side of it
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        x_str: str = str(x)
        halved = int(len(x_str))
        if x % 2 == 0:
            l, r = x_str[:halved], x_str[halved::-1]
        else:
            l, r = x_str[:halved], x_str[halved + 1::-1]

        for i in range(len(l)):
            if l[i] != r[i]:
                return False
        return True
