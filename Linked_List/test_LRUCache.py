class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None


class LRUCache:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.cache = {}
        self.capacity = capacity

    def delete(self, node):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        elif node == self.head:
            head = self.head
            self.head = self.head.next
            self.head.previous = None
            head.next = head.previous = None
        elif node == self.tail:
            tail = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            tail.next = tail.previous = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.next = node.previous = None

    def append(self, node):
        if not self.head:
            self.head = self.tail = node
            self.next = self.previous = None
        else:
            head = self.head
            self.head = node
            self.head.next = head
            self.head.previous = None
            head.previous = node

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
            if self.capacity <= len(self.cache):
                del self.cache[self.tail.key]
                self.delete(self.tail)
            node = Node(key, value)
            self.cache[key] = node
            self.append(node)


# Testing the LRUCache
LRUtest = LRUCache(2)
LRUtest.put(1, 10)
print(LRUtest.get(1))
LRUtest.put(2, 20)
LRUtest.put(3, 30)
print(LRUtest.get(2))
print(LRUtest.get(3))
print(LRUtest.get(1))
["LRUCache", [4], "put", [1, 1], "put", [2, 2], "put", [3, 3],
 "get", [1], "get", [2], "get", [4], "put", [4, 4], "get", [1],
 "get", [2], "get", [3], "get", [4], "get", [2], "put", [5, 5],
 "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get",
 [2], "get", [3], "get", [4], "put", [6, 6], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [6]]
