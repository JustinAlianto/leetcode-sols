#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # preorder.pop(0) takes (and removes) the first element from the preorder list.
            # -> This is always the root of the current (sub)tree.
            ind = inorder.index(preorder.pop(0))

            # Then inorder.index(...) finds where that root appears in the inorder list.
            # -> Everything to the left of that index belongs to the left subtree.
            # -> Everything to the right belongs to the right subtree.
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1 :])

            return root


# @lc code=end
