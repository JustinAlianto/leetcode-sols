#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x == "+":
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(x2 + x1)
            elif x == "-":
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(x2 - x1)
            elif x == "*":
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(x2 * x1)
            elif x == "/":
                x1 = stack.pop()
                x2 = stack.pop()
                stack.append(int(x2 / x1))
            else:
                stack.append(int(x))

        return stack[0]


# @lc code=end
