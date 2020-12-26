"""
Title:      Rotate List
URL:        https://leetcode.com/problems/rotate-list/
Space:
Time:
Difficulty: Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        1 -> 2 -> 3 -> 4 -> 5
        There are 3 things to accomplish
        1. For any value of k != 0, the last node (points to None) has to point to head
        2. k elements will be in front of the head. Thus, head points to (n-k+1)th node
        3. The (n-k)th node points to None

        :param head:
        :param k:
        :return:
        """
        if not head:
            return None
        curr = head
        n = 1
        while curr.next:  # Get number of nodes
            curr = curr.next
            n += 1
        k %= n
        if k == 0:  # No rotations necessary
            return head
        curr.next = head  # Step 1 curr is the last node, so it's next should be head
        idx = 0
        while idx < n - k:  # Get to the node where it's pointer should point to None
            curr = curr.next
            idx += 1
        head = curr.next  # Step 2
        curr.next = None  # Step 3
        return head
