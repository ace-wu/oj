# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    ## TC: O(N), SC: O(N)
    def doubleIt(self, head: ListNode | None) -> ListNode | None:
        def _double_and_get_carry(node) -> int:
            if node is None:
                return 0
            sum_ = node.val * 2 + _double_and_get_carry(node.next)
            node.val = sum_ % 10
            return sum_ // 10

        carry = _double_and_get_carry(head)
        if carry:
            head = ListNode(carry, head)
        return head
