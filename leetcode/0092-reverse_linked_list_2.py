from leetcode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for _ in range(m - 1):
            pre = pre.next
        # we need to connect m -> n+1 and m-1 to n after we reverse
        reverse = None
        cur = pre.next  # First element to be rotated, m-th element
        for _ in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        pre.next.next = cur
        pre.next = reverse
        return dummy.next
