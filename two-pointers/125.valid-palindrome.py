#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        if s.strip() == "":
            return True

        # If isalnum() is not allowed, use regex:
        # s = re.sub('[^a-zA-Z0-9]', '', s).lower()

        # return s == s[::-1]

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


# @lc code=end
