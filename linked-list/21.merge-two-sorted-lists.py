#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        tmp = ListNode()

        head = tmp

        while list1 and list2:
            if list1.val > list2.val:
                # CONNECTION: First, link the current node in the merged list ('tmp')
                # to the chosen node from list2. This adds the node to the merged chain.
                tmp.next = list2
                # POSITIONING: Move the 'tmp' pointer forward to this newly added node.
                # This updates the "current end" of the merged list for the next iteration.
                tmp = list2

                list2 = list2.next
            else:
                tmp.next = list1
                tmp = list1

                list1 = list1.next

        if list1:
            tmp.next = list1
        elif list2:
            tmp.next = list2

        return head.next


# @lc code=end
