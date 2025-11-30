#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = 0

        def recursiveDiameter(node: Optional[TreeNode]):
            nonlocal length

            if not node:
                return 0

            # Length of left and right branch
            left = recursiveDiameter(node.left)
            right = recursiveDiameter(node.right)

            # Updates max length
            length = max(length, left + right)

            # Returns the length of the longer branch to root,
            # so this refers to only one side (left/right)
            return 1 + max(left, right)

        recursiveDiameter(root)

        return length


# @lc code=end
