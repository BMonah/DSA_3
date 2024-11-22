
"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.

int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.




Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)


"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def delete(self, node):
        if self.head == self.tail:  # Only one node in the list
            self.head = None
            self.tail = None

        elif node == self.head:  # Remove head
            self.head = node.next
            if self.head:
                self.head.previous = None
        elif node == self.tail:  # Remove tail
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
        else:  # Remove a middle node
            node.previous.next = node.next
            node.next.previous = node.previous
            node.previous = node.next = None

    def append(self, node):
        if not self.head:  # Empty list
            self.head = node
            self.tail = node
        else:  # Insert at the head
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.head.previous = None

    def get(self, key):
        if key not in self.cache:
            return False

        node = self.cache[key]
        self.delete(node)
        self.append(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.append(node)
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.tail.key]  # Remove from the cache
                self.delete(self.tail)

            node = Node(key, value)
            self.append(node)
            self.cache[key] = node


# Testing the LRUCache
LRUtest = LRUCache(2)
LRUtest.put(1, 10)
print(LRUtest.get(1))
LRUtest.put(2, 20)
LRUtest.put(3, 30)
print(LRUtest.get(3))
print(LRUtest.get(3))
