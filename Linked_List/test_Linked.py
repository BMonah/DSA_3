class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.next = None

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.head = new_node
            self.tail = new_node
            self.next = None

    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
            self.next = None

    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        head = self.head
        self.head = self.tail
        self.tail = head

    def printList(self):
        current = self.head
        arr = []
        while current is not None:
            arr.append(current.value)
            current = current.next
        print(arr)


myLinkedlist = Linkedlist(4)
myLinkedlist.append(5)
myLinkedlist.append(5)
myLinkedlist.append(21)
myLinkedlist.append(1)
myLinkedlist.append(7)
myLinkedlist.reverse()
myLinkedlist.printList()
