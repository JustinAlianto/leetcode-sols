#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        left, right = 0, 0

        cur_s = set()

        while right < len(s):
            if left == right:
                cur_s.add(s[left])
                right += 1
            elif s[right] in cur_s:
                # Rather than having a temporary list of current string
                # to track the order, just increment left by 1 to eventually
                # find the duplicated char and remove it
                cur_s.remove(s[left])
                left += 1
            else:
                cur_s.add(s[right])
                right += 1

            max_len = max(max_len, len(cur_s))

        return max_len


# @lc code=end
