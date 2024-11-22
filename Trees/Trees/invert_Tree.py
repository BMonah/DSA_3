class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Iterative insertion method
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        current = self.root

        while True:
            if value == current.value:
                # If value already exists, do not insert duplicates
                return False

            # Traverse left if the value is smaller
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            else:
                # Traverse right if the value is larger
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right

    # Method to insert all values from a list
    def insert_from_list(self, values):
        for value in values:
            self.insert(value)

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        level = 1
        while queue:
            current_node = queue.pop(0)
            if current_node:
                results.append(current_node.value)
                queue.append(current_node.left)
                queue.append(current_node.right)
                level += 1
        return results

    def __invert_tree(self, node):
        if node is None:
            return None

        temp = node.left
        node.left = node.right
        node.right = temp

        self.__invert_tree(node.left)
        self.__invert_tree(node.right)

        return node

    def invert(self):
        return self.__invert_tree(self.root)


# Example usage
values = [27, 14, 35, 10, 19, 31, 82]
bst = BinarySearchTree()
bst.insert_from_list(values)
print(bst.BFS())
bst.invert()
print(bst.BFS())
