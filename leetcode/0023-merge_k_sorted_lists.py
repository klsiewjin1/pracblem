"""
Title:      Merge K Sorted Lists
URL:        https://leetcode.com/problems/merge-k-sorted-lists/
Space:      O(k)
Time:       O(n log(k))
Difficulty: Hard
"""

from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode()
        queue = []
        entry_count = 0  # entry_count serves as a tie breaker for when the first elem in the tuple has another same priority
        for elem in lists:
            if elem is not None:
                entry_count += 1
                heapq.heappush(queue, (elem.val, entry_count, elem))
        while len(queue) > 0:
            _, _, curr.next = heapq.heappop(queue)
            curr = curr.next
            if curr.next is not None:
                entry_count += 1
                heapq.heappush(queue, (curr.next.val, entry_count, curr.next))

        return head.next
