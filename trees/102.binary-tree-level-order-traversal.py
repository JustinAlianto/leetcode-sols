#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        # IDEA: Modify res directly as we go, so we don't have to iterate results
        #       numerous times from the recursions
        def helper(node: Optional[TreeNode], depth: int):
            if not node:
                return

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)

            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)

        return res

    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []

    #     res = [[root.val]]

    #     if not root.left and not root.right:
    #         return res
    #     elif not root.left:
    #         right = self.levelOrder(root.right)
    #         for i in range(len(right)):
    #             res.append(right[i])
    #     elif not root.right:
    #         left = self.levelOrder(root.left)
    #         for i in range(len(left)):
    #             res.append(left[i])
    #     else:
    #         left = self.levelOrder(root.left)
    #         right = self.levelOrder(root.right)

    #         min_len = min(len(left), len(right))

    #         for i in range(min_len):
    #             left_i = left[i]
    #             right_i = right[i]

    #             res_i = left_i + right_i

    #             res.append(res_i)

    #         if len(left) > min_len:
    #             for j in range(min_len, len(left)):
    #                 res.append(left[j])
    #         elif len(right) > min_len:
    #             for j in range(min_len, len(right)):
    #                 res.append(right[j])

    #     return res


# @lc code=end
