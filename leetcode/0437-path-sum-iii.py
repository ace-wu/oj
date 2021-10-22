from collections import defaultdict


class Solution:
    def pathSum_list(self, root: Optional[TreeNode], targetSum: int) -> int:
        def path_count(cursor, path_sum):
            if not cursor:
                return 0
            count = 0
            my_sum = path_sum[-1] + cursor.val
            for sum_ in path_sum:
                if my_sum - sum_ == targetSum:
                    count += 1
            path_sum.append(my_sum)
            count += path_count(cursor.left, path_sum)
            count += path_count(cursor.right, path_sum)
            path_sum.pop()
            return count
        return path_count(root, [0])

    def pathSum_dict(self, root: Optional[TreeNode], targetSum: int) -> int:
        def path_count(cursor, path_sum, sum_counts):
            if not cursor:
                return 0
            path_sum += cursor.val
            count = sum_counts[path_sum - targetSum]
            sum_counts[path_sum] += 1
            count += path_count(cursor.left, path_sum, sum_counts)
            count += path_count(cursor.right, path_sum, sum_counts)
            sum_counts[path_sum] -= 1
            return count
        sum_counts = defaultdict(int)
        sum_counts[0] += 1
        return path_count(root, 0, sum_counts)


## TC: O(n)
## SC: O(n)
