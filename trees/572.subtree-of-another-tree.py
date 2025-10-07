#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Helper function to check if the two trees are equal (from previous question)
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        left_bool = self.isSubtree(root.left, subRoot)
        right_bool = self.isSubtree(root.right, subRoot)

        return left_bool or right_bool


# @lc code=end
