from __future__ import annotations
import dataclasses


class TreeNode:
    left: TreeNode | None
    right: TreeNode | None
    val: int


@dataclasses.dataclass
class ReversedNode:
    val: int
    parent: 'ReversedNode'  # | None

    def __lt__(self, rhs):
        if self.val < rhs.val:
            return True
        if self.val > rhs.val:
            return False
        if self.val == rhs.val == -1:
            return False
        return self.parent < rhs.parent

    def iter_chars(self):
        if self.val == -1:
            return
        yield chr(ord('a') + self.val)
        yield from self.parent.iter_chars()

    def __str__(self):
        return ''.join(self.iter_chars())


def make_reversed_tree(
    old_node: TreeNode | None, parent: ReversedNode, leaves: list[ReversedNode]
):
    if old_node is None:
        return
    new_node = ReversedNode(val=old_node.val, parent=parent)
    if not old_node.left and not old_node.right:
        leaves.append(new_node)
    if old_node.left:
        make_reversed_tree(old_node.left, new_node, leaves)
    if old_node.right:
        make_reversed_tree(old_node.right, new_node, leaves)


class Solution:
    ## TC: O(#leaves * depth), worst case: O(n^2)
    ## SC: O(n) additional space
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        sentinel = ReversedNode(-1, None)
        sentinel.parent = sentinel
        leaves = []
        make_reversed_tree(root, sentinel, leaves)
        return str(min(leaves))
