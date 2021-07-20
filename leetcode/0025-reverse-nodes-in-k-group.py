class Solution:
    def reverseKGroupIter(self, head, k):
        stack = []
        while head is not None:
            while head is not None and len(stack) < k:
                stack.append(head)
                head = head.next
            if len(stack) < k:
                stack = stack[::-1]
            while stack:
                yield stack.pop()

    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head
        result = ListNode(0)
        prev = result
        for node in self.reverseKGroupIter(head, k):
            prev.next = node
            prev = node
        prev.next = None
        return result.next