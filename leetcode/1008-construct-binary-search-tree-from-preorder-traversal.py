from bisect import bisect


class Solution:
    def bstFromPreorder_bisect(self, preorder: List[int]) -> Optional[TreeNode]:
        def build_bst(i, j):  # [i...j-1] j
            if i >= j:
                return None
            node_value = preorder[i]
            k = bisect(preorder, node_value, i, j)
            k = i + 1
            while k < j and preorder[k] < node_value:
                k += 1
            return TreeNode(
                node_value,
                build_bst(i + 1, k),
                build_bst(k, j),
            )
        return build_bst(0, len(preorder))

    def bstFromPreorder_upper_bound(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def build_bst(i, parent_value):
            if i >= n or preorder[i] >= parent_value:
                return i, None
            node_value = preorder[i]
            i += 1
            i, left = build_bst(i, node_value)
            i, right = build_bst(i, parent_value)
            return i, TreeNode(node_value, left, right)
        _, root = build_bst(0, float('inf'))
        return root


## TC: O(n) for the upper bound version, O(n*log(n)) for the bisect version
## SC: O(n)
