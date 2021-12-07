class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head:
            answer = answer * 2 + head.val
            head = head.next
        return answer


## TC: O(n)
## SC: O(1)
