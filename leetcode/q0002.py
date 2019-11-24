class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @classmethod
    def add_two_numbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next


if __name__ == '__main__':
    # [2, 4, 3]
    l1_3 = ListNode(3)
    l1_2 = ListNode(4)
    l1_1 = ListNode(2)
    l1_2.next = l1_3
    l1_1.next = l1_2

    # [5, 6, 4]
    l2_3 = ListNode(4)
    l2_2 = ListNode(6)
    l2_1 = ListNode(5)
    l2_2.next = l2_3
    l2_1.next = l2_2

    ans = Solution.add_two_numbers(l1_1, l2_1)

    # [7, 0, 8]
    assert ans.val == 7
    assert ans.next.val == 0
    assert ans.next.next.val == 8
