class Node:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache1:
    def __init__(self, capacity: int):
        self.map = {}  # Hash map to store key-node pairs
        self.capacity = capacity
        self.head = None  # Head of the doubly linked list
        self.tail = None  # Tail of the doubly linked list

    def _delete_from_list(self, node: Node):
        """Remove a node from the doubly linked list."""
        if node.prev:
            node.prev.next = node.next
        else:
            # Node is head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            # Node is tail
            self.tail = node.prev

    def _set_list_head(self, node: Node):
        """Move a node to the head of the doubly linked list."""
        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node
        self.head = node

        if self.tail is None:
            # If the list was empty, tail also points to this node
            self.tail = node

    def get(self, key: str) -> str:
        if key not in self.map:
            return None

        node = self.map[key]

        # Move the accessed node to the head of the list (most recently used)
        self._delete_from_list(node)
        self._set_list_head(node)

        return node.value

    def put(self, key: str, value: str):
        if key in self.map:
            # Update the node's value and move it to the head
            node = self.map[key]
            node.value = value

            self._delete_from_list(node)
            self._set_list_head(node)
        else:
            if len(self.map) >= self.capacity:
                # Remove the least recently used node (tail)
                del self.map[self.tail.key]
                self._delete_from_list(self.tail)

            # Create a new node
            node = Node(key, value)

            # Add it to the map and move it to the head of the list
            self.map[key] = node
            self._set_list_head(node)


class Node:
    def __init__(self, key, value):
        self.value = value
        self.next = self.previous = None
        self.key = key


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = None

    def append(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
            node.previous = None

    def delete(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

    def get(self, key):
        if key not in self.cache:
            return -1

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
                del self.cache[self.tail.key]
                self.delete(self.tail)
            node = Node(key, value)
            self.cache[key] = node
            self.append(node)


["LRUCache", [4], "put", [1, 1], "put", [2, 2], "put", [3, 3],
 "get", [1], "get", [2], "get", [4], "put", [4, 4], "get", [1],
 "get", [2], "get", [3], "get", [4], "get", [2], "put", [5, 5],
 "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get",
 [2], "get", [3], "get", [4], "put", [6, 6], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [6]]
