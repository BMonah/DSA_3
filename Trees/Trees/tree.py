class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def findVal(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        return False

    # levelorder traversal (Breadth-first Search) 0n2
    # per tree level starting with the root -> left -> right
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while queue:
            current_node = queue.pop(0)
            if current_node:
                results.append(current_node.value)
                queue.append(current_node.left)
                queue.append(current_node.right)
        return results

    # PreOrder traversal (DFS)
    #  Root -> Left -> Right
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return results

    # Postorder traversal (DFS)
    # Left -> RIght -> Root
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    # Inorder traversal (DFS)
    # Left -> Root -> Right
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    # Inorder traversal (DFS)
    # Left -> Root -> Right
    def kth_smallest_in_order(self, kth):
        if not self.root:
            return None
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        if (kth-1) not in range(len(results)):
            return None
        else:
            return results[kth-1]

    # Inorder traversal (DFS)
    # validate Tree
    def validate_BST(self):
        res = []

        def inOrderTraverse(current_node):
            if current_node.left:
                inOrderTraverse(current_node.left)
            res.append(current_node.value)
            if current_node.right:
                inOrderTraverse(current_node.right)

        inOrderTraverse(self.root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True


my_tree = BinarySearchTree()
my_tree.insert(27)
my_tree.insert(14)
my_tree.insert(35)
my_tree.insert(10)
my_tree.insert(19)
my_tree.insert(31)
my_tree.insert(82)
# print(my_tree.root.value)
# print(my_tree.root.right.value)
print(my_tree.findVal(52))
print(my_tree.BFS())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())
print(my_tree.kth_smallest_in_order(3))
print(my_tree.validate_BST())
