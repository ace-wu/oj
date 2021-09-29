# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cursor = head
        while cursor:
            n += 1
            cursor = cursor.next

        result = []
        cursor = head
        for i in range(k):
            result.append(cursor)
            for i in range(n // k + int(i < n % k) - 1):
                cursor = cursor.next
            if cursor:
                next_part = cursor.next
                cursor.next = None
                cursor = next_part
        return result


## TC: O(n)
## SC: O(1)
