class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        even_head, even_tail, odd_head, odd_tail = head, head, head.next, head.next
        head = head.next.next
        while head:
            even_tail.next = head
            even_tail = head
            head = head.next
            if not head:
                break
            odd_tail.next = head
            odd_tail = head
            head = head.next
        odd_tail.next = None
        even_tail.next = odd_head
        return even_head


## TC: O(n)
## SC: O(1)
