#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP: f(n) = f(n - 1) + f(n - 2)

        # These represent the only 2 states we need at a time
        # Working backwards from n:
        # - one -> the second last state n - 1
        # - two -> the last state n
        # IDEA: When we work backwards, we only need the next 2 states
        #       ahead, i.e. one and two if we are at state n - 2, since
        #       we can only move in 2 ways.

        # These 2 are initialized at 1 because there is only 1 way to reach
        # the goal n from either of the steps:
        # - To take 1 step from state n - 1 (one)
        # - To do nothing from the goal state n (two)
        one, two = 1, 1

        # Don't care about the "forward" direction of this loop.
        # The logic is still backwards where we are traversing from the end
        # goal n (or n - 2 to be exact) to the beginning. We just need n - 1
        # backward steps to get one to represent the first state 0.
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        # one is returned, because when we work backwards, we stop when one
        # is at the first state 0. At this point, two will be at the state 1.
        return one

        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(1)


# @lc code=end
