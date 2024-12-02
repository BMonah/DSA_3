class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        current_node = self.root
        while (True):
            if new_node.value == current_node.value:
                return False
            if new_node.value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            if new_node.value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                current_node = current_node.right

    def insertList(self, value):
        for item in value:
            self.insert(item)


class BSTIterator:
    def __init__(self, bst):
        # initialize a stack to store the traversal state
        self.stack = []

        # initialize traversal to the leftmost node
        current = bst.root
        while current:
            self.stack.append(current)
            current = current.left

    def next(self):
        # pop the topmost element
        topmost_node = self.stack.pop()

        # if the node has a right child process its left most element
        current = topmost_node.right
        while current:
            self.stack.append(current)
            current = current.left
        return topmost_node.value

    def hasNext(self):
        # check if stack is empty or not
        if self.stack != []:
            return True
        else:
            return False


nodes = [27, 14, 35, 10, 19, 31, 82]
BSTree = BST()
BSTree.insertList(nodes)
iterator = BSTIterator(BSTree)
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
