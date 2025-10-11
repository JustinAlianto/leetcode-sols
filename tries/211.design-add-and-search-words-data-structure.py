#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


# @lc code=start
class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if curr.children[ord(c) - ord("a")] == None:
                curr.children[ord(c) - ord("a")] = WordDictionary()
            curr = curr.children[ord(c) - ord("a")]

        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self

        for i in range(len(word)):
            c = word[i]

            if c == ".":
                for child in curr.children:
                    if child is not None and child.search(word[i + 1 :]):
                        return True
                return False

            if curr.children[ord(c) - ord("a")] == None:
                return False

            curr = curr.children[ord(c) - ord("a")]

        return curr.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
