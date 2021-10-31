class Solution:
    def flatten(self, head, tail=None):
        if not head:
            return tail
        head.next = self.flatten(head.child, self.flatten(head.next, tail))
        if head.next:
            head.next.prev = head
        head.child = None
        return head


## TC: O(n)
## SC: O(n)
