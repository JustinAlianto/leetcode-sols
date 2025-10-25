#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        # This is a setup for a sliding window, where the range of
        # the window is the length of s1 at all times
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        # This will be the initial number of matches for the
        # first len(s1) words.
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        left = 0

        # Right pointer starts at the character after the first
        # len(s1) words
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx_right = ord(s2[right]) - ord("a")
            s2_count[idx_right] += 1

            if s2_count[idx_right] == s1_count[idx_right]:
                matches += 1
            # Handles when the additional character added from the
            # right pointer makes the initially matching count of
            # the character to be not matching anymore (1 more)
            elif s2_count[idx_right] == s1_count[idx_right] + 1:
                matches -= 1

            idx_left = ord(s2[left]) - ord("a")
            s2_count[idx_left] -= 1

            if s2_count[idx_left] == s1_count[idx_left]:
                matches += 1
            # Handles when the additional character removed from the
            # left pointer makes the initially matching count of
            # the character to be not matching anymore (1 less)
            elif s2_count[idx_left] + 1 == s1_count[idx_left]:
                matches -= 1

            left += 1

        return matches == 26


# @lc code=end
