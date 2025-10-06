#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # IDEA:
        # - Use 2 trackers again: fast and slow
        # - In this case, both traverse one step at a time, but
        #   give the fast tracker a headstart by n
        # - When fast tracker reaches the end, slow will be at
        #   the nth node
        slow = head
        fast = head

        while n > 0:
            try:
                fast = fast.next
                n -= 1
            except:
                return []

        # Check if fast is already None:
        # - If yes, that means n is the length of the list and that
        #   we are removing the first node
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head


# @lc code=end
