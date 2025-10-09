#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # IDEA:
    # - Using Recursion.
    # - Perform an in-order traversal of the binary search tree.
    # - In each recursive call, check if the kth smallest element
    #   has been found.
    # - If found, update the result and stop further traversal.
    # - Return the result after the traversal.

    # COMPLEXITY:
    # - Time complexity: O(n),
    #   where n is the number of nodes in the binary search tree.
    #   The inorder traversal visits each node once.
    # - Space complexity: O(h),
    #   where h is the height of the binary search tree.
    #   The space complexity is determined by the recursion stack.
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = 0
        self.inorderTraversal(root, k)
        return self.result

    def inorderTraversal(self, node, k):
        if not node or self.count >= k:
            return

        self.inorderTraversal(node.left, k)

        self.count += 1
        if self.count == k:
            self.result = node.val
            return

        self.inorderTraversal(node.right, k)


# @lc code=end
