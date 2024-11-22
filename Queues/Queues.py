class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.next = None
        self.length = 1

    def print_queue(self):
        res = self.first
        if self.next is not None:
            print(res)
            res = self.next
            self.next.print_queue()
        else:
            print(res)

    def print_print(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = value
            self.last = value
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        dequeued_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            dequeued_node.next = None
        self.length -= 1
        return dequeued_node


my_queue = Queue(5)
my_queue.enqueue(18)
my_queue.enqueue(21)
my_queue.enqueue(2)
my_queue.dequeue()
my_queue.print_print()
# my_queue.print_queue()
