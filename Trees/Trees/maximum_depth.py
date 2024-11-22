class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            new_node.right = None
            new_node.left = None
        current_node = self.root
        while (True):
            if new_node.value == current_node.value:
                return False
            if new_node.value < current_node.value:
                if current_node.left == None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                current_node = current_node.right

    def insert_List(self, List):
        for value in List:
            self.insert(value)

    def BFS(self):
        arr = []
        queue = []
        current_node = self.root
        queue.append(current_node)
        while queue:
            current_node = queue.pop(0)
            arr.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return arr

    def invert(self, node):
        if node is None:
            return None

        temp = node.left
        node.left = node.right
        node.right = temp

        self.invert(node.left)
        self.invert(node.right)

    def invert_tree(self):
        self.invert(self.root)

    def levelorderTraversal(self, node):
        queue = []
        results = []
        # enqueue root and initialize height
        queue.append(node)
        count = 0
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                # print(node)
                # enqueue left child
                if node:
                    level.append(node.value)
                    queue.append(node.left)
                    queue.append(node.right)
                    # print(len(queue))
            if level:
                results.append(level)
                count += 1
        return results, count

    def find_depth(self):
        return self.levelorderTraversal(self.root)

    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

    def maxDepth2(self):
        return self.maxDepth(self.root)


values = [27, 14, 35, 10, 19, 31, 82]
bst = Tree()
bst.insert_List(values)
bst.invert_tree()
print(bst.BFS())
print(bst.find_depth())
print(bst.maxDepth2())
