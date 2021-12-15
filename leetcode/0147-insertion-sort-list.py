class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        while head:
            insert_after = result
            while insert_after.next:
                if head.val <= insert_after.next.val:
                    break
                insert_after = insert_after.next
            next_head = head.next
            head.next = insert_after.next
            insert_after.next = head
            head = next_head
        return result.next
