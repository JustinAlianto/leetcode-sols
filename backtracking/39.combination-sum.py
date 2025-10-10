#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # MAIN IDEA:
        # - 2 Recursions: 1 chooses to include that number and the other skips that.
        res = []

        def backtrack(start_i, cur_path, cur_total):
            if cur_total == target:
                # Make sure to pass in a copy of cur_path since cur_path is
                # allocated the same memory throughout the recursions
                res.append(list(cur_path))
                return

            if start_i == len(candidates) or cur_total > target:
                return

            # Recursion 1: Include the current number in our path
            cur_path.append(candidates[start_i])
            backtrack(start_i, cur_path, cur_total + candidates[start_i])
            # Recursion 2: Exclude the current number in our path
            cur_path.pop()
            backtrack(start_i + 1, cur_path, cur_total)

        backtrack(0, [], 0)
        return res


# @lc code=end
