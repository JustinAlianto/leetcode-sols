#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # IDEA: Check palindromic substring at each character

        count = 0

        for i in range(len(s)):
            # CASE 1: Even length palindrome
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1

                left -= 1
                right += 1

            # CASE 2: Odd length palindrome
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1

                left -= 1
                right += 1

        return count

        # TIME COMPLEXITY: O(n^2)
        # SPACE COMPLEXITY: O(1)


# @lc code=end
