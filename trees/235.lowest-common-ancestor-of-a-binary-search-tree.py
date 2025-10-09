#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        if root.val >= min_val and root.val <= max_val:
            return root
        elif root.val > max_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min_val:
            return self.lowestCommonAncestor(root.right, p, q)

        # # This line checks if p and q are both on the same side of the current root.
        # while (root.val - p.val) * (root.val - q.val) > 0:
        # # This is a tuple-based conditional selection — a short Python trick.
        #     root = (root.left, root.right)[p.val > root.val]
        # return root


# @lc code=end
