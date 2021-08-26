
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        branch_count = 1
        for node in preorder.split(','):
            if branch_count <= 0:
                return False
            if node == '#':
                branch_count -= 1
            else:
                branch_count += 1
        return branch_count == 0

    def isValidSerialization_dfs(self, preorder: str) -> bool:
        def is_preorder(preorder):
            if not preorder:
                return False
            if preorder.pop() == '#':
                return True
            return is_preorder(preorder) and is_preorder(preorder)
        preorder = preorder.split(',')[::-1]
        return is_preorder(preorder) and not preorder


# TC: O(n)
# SC: O(n), can be reduce to O(1)

s = Solution()
print(s.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#'))
print(s.isValidSerialization('1,#'))
print(s.isValidSerialization('9,#,#,1'))
