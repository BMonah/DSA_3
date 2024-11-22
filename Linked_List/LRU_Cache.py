class Node:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
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


LRUtest = LRUCache(2).put(1, 2)
LRUtest
print(LRUtest.get(1))
