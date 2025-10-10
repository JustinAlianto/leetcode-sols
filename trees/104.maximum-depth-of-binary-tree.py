#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def getDepth(self, cur: Optional[TreeNode], depth) -> int:
    #     left, right = cur.left, cur.right
    #     if not left and not right:
    #         return depth + 1
    #     elif not left:
    #         return self.getDepth(right, depth + 1)
    #     elif not right:
    #         return self.getDepth(left, depth + 1)
    #     else:
    #         left_depth = self.getDepth(left, depth + 1)
    #         right_depth = self.getDepth(right, depth + 1)

    #         return max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# @lc code=end
