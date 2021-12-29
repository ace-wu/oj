from collections import deque


class Solution:
    # bfs
    ## TC: O(n)
    ## SC: O(n)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        prev_node, prev_depth = None, -1
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if prev_depth == depth:
                prev_node.next = node
            prev_node, prev_depth = node, depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return root

    # TC: O(n)
    # SC: O(1)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        level_head = root
        while level_head:
            curr, level_head = level_head, level_head.left
            while curr and curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
        return root
