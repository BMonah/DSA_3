class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, value):
        self.stack_list = []
        self.top = Node(value)
        self.stack_list.append(5)
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.stack_list.append(self.top.value)
        return (self.stack_list)

    def remove_nth(self):
        node = self.top
        self.next = self.top.next
        self.top.next.next.next = self.top.next.next.next.next

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_stack = Stack(5)
my_stack.push(17)
my_stack.push(21)
my_stack.push(9)
my_stack.push(0)
my_stack.remove_nth()
my_stack.print_stack()
