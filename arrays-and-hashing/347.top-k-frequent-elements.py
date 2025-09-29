#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        num_count = {}

        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in num_count.items():
            freq[c].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res

        # Cheat Method:
        # num_count = Counter(nums)
        # return [c[0] for c in num_count.most_common(k)]


# @lc code=end
