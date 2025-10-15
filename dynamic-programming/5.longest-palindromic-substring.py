#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # IDEA: Check palindromic substring at each character

        max_len = 0
        start_idx = 0

        for i in range(len(s)):
            # CASE 1: Even length palindrome
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_len = right - left + 1

                if right - left + 1 > max_len:
                    max_len = cur_len
                    start_idx = left

                left -= 1
                right += 1

            # CASE 2: Odd length palindrome
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_len = right - left + 1

                if right - left + 1 > max_len:
                    max_len = cur_len
                    start_idx = left

                left -= 1
                right += 1

        return s[start_idx : start_idx + max_len]

        # TIME COMPLEXITY: O(n^2)
        # SPACE COMPLEXITY: O(1), but O(n) for the output string


# @lc code=end
