"""
Title:      Add Two Numbers
URL:        https://leetcode.com/problems/add-two-numbers/
Space:      O(n)
Time:       O(n)
Difficulty: Medium
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        return_head = head
        carry_over = 0
        prev = None
        while l1 or l2:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            carry_over, head.val = divmod(l1_val + l2_val + carry_over, 10)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            prev = head
            head.next = ListNode()
            head = head.next

        if carry_over:
            head.val += 1
        else:
            prev.next = None
        return return_head
