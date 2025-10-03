# DESCRIPTION:
# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:
# - Input: ["neet","code","love","you"]
# - Output:["neet","code","love","you"]

# Example 2:
# - Input: ["we","say",":","yes"]
# - Output: ["we","say",":","yes"]

# Constraints:
# - 0 <= strs.length < 100
# - 0 <= strs[i].length < 200
# - strs[i] contains only UTF-8 characters.

# You should aim for a solution with O(m) time for each encode() and decode() call
# and O(m+n) space, where m is the sum of lengths of all the strings and
# n is the number of strings.

# Notes:
# - Can't just join the list of strings with a delimiter, because that delimiter might
#   just be a part of a string.
# - Keep track of the length of each string by embedding the lengths into the joined string.
from collections import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "!" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length_s = ""
            j = i

            while s[j] != "!":
                length_s += s[j]
                j += 1

            length = int(length_s)

            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res


def main():
    input1 = ["we", "say", ":", "yes"]
    output1 = ["neet", "code", "love", "you"]

    encoded1 = Solution.encode(input1)
    decoded1 = Solution.decode(encoded1)
    print(f"Test 1: {decoded1 == output1}")

    input2 = ["we", "say", ":", "yes"]
    output2 = ["we", "say", ":", "yes"]

    encoded2 = Solution.encode(input2)
    decoded2 = Solution.decode(encoded2)
    print(f"Test 2: {decoded2 == output2}")


if __name__ == "__main__":
    main()
