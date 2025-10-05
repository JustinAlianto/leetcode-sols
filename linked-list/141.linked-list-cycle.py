#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # IDEA:
        # - Have 2 trackers, one travelling twice as fast as the other
        # - Make them start at different positions to get past the first
        #   slow == fast check
        # - If they ever cross path again before the fast tracker
        #   becomes None, there's a cycle
        slow = head
        fast = head.next

        while fast:
            if slow == fast:
                return True

            slow = slow.next

            try:
                fast = fast.next.next
            except:
                fast = None

        return False


# @lc code=end
