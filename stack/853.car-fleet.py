#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        # Sort by the starting position in reverse order
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p, s in pair:
            cur_time = (target - p) / s
            # prev_time represents the time taken needed to reach the
            # target by the PREVIOUS car in the list (but actually,
            # this is the car that starts in front of the current car)
            prev_time = stack[-1] if stack else 0

            stack.append(cur_time)

            if stack and cur_time <= prev_time:
                stack.pop()

        return len(stack)


# @lc code=end
