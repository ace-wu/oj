from collections import deque


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        number_set = set([x, y])
        depth_list = []
        parent_list = []
        queue = deque([(root, 0, -1)])
        while queue and number_set:
            node, depth, parent = queue.popleft()
            if node.val in number_set:
                depth_list.append(depth)
                parent_list.append(parent)
            if node.left:
                queue.append((node.left, depth+1, node.val))
            if node.right:
                queue.append((node.right, depth+1, node.val))
        return depth_list[0] == depth_list[1] and parent_list[0] != parent_list[1]


## TC: O(n)
## SC: O(n)
