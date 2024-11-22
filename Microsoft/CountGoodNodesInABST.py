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

        while True:
            if value == current_node.value:
                return False
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                current_node = current_node.right

    def insertList(self, nums):
        for number in nums:
            self.insert(number)

    def pre_order(self):
        results = []

        def traverse(root):
            results.append(root.value)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        traverse(self.root)
        return results

    def goodness(self):
        def traverse(node, max_val):
            if not node:
                return 0

            results = 1 if node.value >= max_val else 0
            max_val = max(node.value, max_val)
            results += traverse(node.left, max_val)
            results += traverse(node.right, max_val)
            return results
        return traverse(self.root, self.root.value)


nodes = [27, 14, 35, 10, 19, 31, 82]
BSTree = BST()
BSTree.insertList(nodes)
print(BSTree.pre_order())
print(BSTree.goodness())
