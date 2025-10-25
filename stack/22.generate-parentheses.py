#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # We can keep adding opening brackets until we have
            # n of them
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # Cleanup because we are using the same
                # stack variable the whole time
                stack.pop()

            # Keep in mind that we can only add a closing bracket
            # when the number of closing brackets is still less than
            # the number of opening brackets
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# @lc code=end
