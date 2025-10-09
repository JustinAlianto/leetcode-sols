#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # KNOW PREORDER AND INORDER AND POSTORDER ALGOS
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node):
            if not node:
                return []

            res.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)

        return res


# @lc code=end
