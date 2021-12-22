class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # find right half
        left_tail, right_tail = head, head
        while right_tail.next and right_tail.next.next:
            left_tail = left_tail.next
            right_tail = right_tail.next.next
        right_head = left_tail.next
        left_tail.next = None

        # reverse right half
        prev = None
        while right_head:
            next_ = right_head.next
            right_head.next = prev
            prev = right_head
            right_head = next_
        right_head = prev

        # merge left and right
        left_head = head
        while right_head:
            next_ = left_head.next
            left_head.next = right_head
            left_head = right_head
            right_head = next_


## TC: O(n)
## SC: O(1)
