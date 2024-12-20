class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if not self.top:
            return None
        poped_node = self.top
        self.top = self.top.next
        poped_node.next = None
        self.height -= 1
        return poped_node.value


my_stack = Stack(4)
my_stack.push(2)
my_stack.push(6)
my_stack.push(14)
# print(my_stack.pop())
# my_stack.pop()
# my_stack.pop()
my_stack.print_stack()
