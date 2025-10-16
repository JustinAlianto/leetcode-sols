#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # This True value means we managed to cover the whole string
        memo = {len(s): True}

        def dfs(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True

            # At this starting point, no words in the dict matches
            memo[i] = False

            return False

        return dfs(0)


# @lc code=end
