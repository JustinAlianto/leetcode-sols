#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_dict[sorted_s].append(s)

        return [val for val in anagram_dict.values()]


# @lc code=end
