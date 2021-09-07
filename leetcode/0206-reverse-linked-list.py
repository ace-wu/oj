from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_list(val_list, i=0):
        if i < len(val_list):
            return ListNode(val_list[i], ListNode.create_list(val_list, i+1))
        return None

    def __repr__(self):
        if self.next is None:
            return f'{self.val}'
        else:
            return f'{self.val}, {self.next}'


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            next_head = head.next
            head.next = tail
            tail = head
            head = next_head
        return tail


## TC: O(n)
## SC: O(1)

s = Solution()
print(s.reverseList(ListNode.create_list([1,2,3,4,5])))
