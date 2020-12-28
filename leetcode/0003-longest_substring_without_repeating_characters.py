"""
Title:      Longest Substring Without Repeating Characters
URL:        https://leetcode.com/problems/longest-substring-without-repeating-characters/
Space:      O(n)
Time:       O(n)
Difficulty: Medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        hash_table = {}
        longest_substring = curr = 0
        for idx, elem in enumerate(s):
            if elem in hash_table and curr <= hash_table[elem]:
                curr = hash_table[elem] + 1  # Update curr to the start of the next substring
            else:
                longest_substring = max(longest_substring, idx - curr + 1)
            hash_table[elem] = idx  # Update last-seen index
        return longest_substring


if __name__ == "__main__":
    test = Solution()
    assert test.lengthOfLongestSubstring("pwwkew") == 3
    assert test.lengthOfLongestSubstring("aab") == 2
    assert test.lengthOfLongestSubstring("aaba") == 2
    assert test.lengthOfLongestSubstring("bbbbb") == 1
    assert test.lengthOfLongestSubstring("abcabcbb") == 3
    assert test.lengthOfLongestSubstring("au") == 2
    assert test.lengthOfLongestSubstring("cdd") == 2
    assert test.lengthOfLongestSubstring("abba") == 2
