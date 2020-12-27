"""
Title:      Split Linked List in Parts
URL:        https://leetcode.com/problems/split-linked-list-in-parts/
Space:
Time:
Difficulty: Medium
"""


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if root is None:
            return [None] * k
        n = 1
        node = root
        while node.next:
            n += 1
            node = node.next
        base_size, additional = divmod(n, k)
        counters = []  # Contains the number of nodes in each elem in result
        for x in range(0, k):
            if additional:
                counters.append(base_size + 1)
                additional -= 1
            else:
                counters.append(base_size)
        result = []
        for elem in counters:
            if not elem:
                result.append(None)
                continue
            result.append(root)
            end = root
            while elem > 1:
                elem -= 1
                end = end.next
            root = end.next
            end.next = None
        return result
