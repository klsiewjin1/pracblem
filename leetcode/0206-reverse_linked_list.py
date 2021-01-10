from leetcode import ListNode


class Solution:
    def reverseList(self, head: ListNode):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
