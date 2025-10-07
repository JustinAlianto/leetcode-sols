#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p is q
        elif p.val != q.val:
            return False
        else:
            left_p, right_p = p.left, p.right
            left_q, right_q = q.left, q.right

            left_bool = self.isSameTree(left_p, left_q)
            right_bool = self.isSameTree(right_p, right_q)

            return left_bool and right_bool


# @lc code=end
