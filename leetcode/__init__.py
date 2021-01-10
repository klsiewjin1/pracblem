class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_int_to_32_bit(n: int) -> str:
    x_str = str(bin(n))[2:]
    x_str = "0" * (32 - len(x_str)) + x_str
    return x_str