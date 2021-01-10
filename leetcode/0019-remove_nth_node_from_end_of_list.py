from leetcode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        num_nodes = 0
        counter = head
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while counter:
            num_nodes += 1
            counter = counter.next
        for _ in range(0, num_nodes - n):
            curr = curr.next  # stop before the element to be removed
        prev = curr
        tmp = curr.next.next
        prev.next = tmp
        return dummy.next
