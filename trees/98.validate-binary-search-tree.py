#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_val = math.inf
        min_val = -math.inf

        def helper(node, maximum, minimum):
            if not node:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            left = helper(node.left, node.val, minimum)
            right = helper(node.right, maximum, node.val)

            return left and right

        return helper(root, max_val, min_val)


# @lc code=end
