class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRUCache:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.cache = {}

    def append(self, node):
        if not self.head:
            self.head = self.tail = node
            node.next = None
            node.previous = None
        else:
            node.next = self.head
            node.previous = None
            self.head.previous = node
            self.head = node

    def delete(self, node):
        if not self.head:
            return False
        elif self.head == self.tail:
            self.head = self.tail = None
            return None
        elif node == self.head:
            head = self.head
            self.head = head.next
            self.head.previous = None
            head.next = None
        elif node == self.tail:
            tail = self.tail
            self.tail = tail.previous
            tail.previous = None
            self.tail.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.next = node.previous = None

    def get(self, key):
        if key not in self.cache:
            return False
        node = self.cache[key]
        self.delete(node)
        self.append(node)
        return self.cache[key].value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.append(node)
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.tail.key]
                self.delete(self.tail)
            node = Node(key, value)
            self.cache[key] = node
            self.append(node)


LRUtest = LRUCache(2)
LRUtest.put(1, 10)
print(LRUtest.get(1))
LRUtest.put(2, 20)
LRUtest.put(3, 30)
print(LRUtest.get(2))
print(LRUtest.get(3))
print(LRUtest.get(1))
