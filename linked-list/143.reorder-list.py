#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # IDEA:
        # - Use slow and fast trackers to figure out the mid point
        #   of the list before we reverse
        # - Once fast is None, slow tracker should be pointing at the
        #   first node to reverse
        if not head:
            return

        slow = head
        fast = head

        while fast:
            slow = slow.next

            try:
                fast = fast.next.next
            except:
                fast = None

        # Implement reverse linked list here to reverse the second set
        prev = None

        while slow:
            next_node = slow.next

            slow.next = prev
            prev = slow

            slow = next_node

        # prev is the head of the reversed set,
        # **BUT** keep in mind, this method doesn't cut off the
        # connection between the 2 sets YET

        while prev:
            head_next = head.next
            prev_next = prev.next

            head.next = prev
            prev.next = head_next

            head = head_next
            prev = prev_next

        # FINAL CHECK to make sure we cut off the connection between
        # the last node of the first set and the first node of the
        # second set
        if head:
            head.next = None


# @lc code=end
