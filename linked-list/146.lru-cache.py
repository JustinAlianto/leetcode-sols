#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key to node

        # Set a start and end pointer to represent least and most
        # recently used node. left and right are technically
        # "ghost" nodes that are only meant to mark the start and end
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = next, prev

    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Remember thet the key is used even in get(), so
            # update the cache to represent this use
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            # Delete from cache
            del self.cache[lru.key]

    # TIME COMPLEXITY: O(1) for get() and put()
    # SPACE COMPLEXITY: O(n)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
