class Node:
    def __init__(self, value):
        self.value = value
        self.head = value
        self.tail = value
        self.next = None
        self.size = 0

    def printList(self):  # print items in the list reverse list
        if self.next:
            self.next.printList()
        print(self.value)

    def printBorder(self):  # print items in the list
        res = self.value
        if self.next is not None:
            print(res)
            res = self.next
            self.next.printBorder()
        else:
            print(res)

    def popList(self):  # remove last item from the list
        res = self.value
        if self.next:
            # res = self.next
            # pre = self.value
            self.next.popList()
            # print(res)

    def prependList(self, value):  # add a new item on top of the list
        # if self.size > 1:
        if self.value:
            if self.value:
                return self.value
            else:
                old_node = self.value
                self.next = Node(old_node)
                self.value = value
                return self.value
                self.next.prependList(value)
        # self.next
        # self.value.next = old_node
        # return old_node
        # print(self.value)
        # self.next = self.value
        # self.value = Node(data)
        # print(self.value)
        # print(self.value)

    def appendItem(self, value):  # insert item in the list
        if self.value:
            if self.next is None:
                self.next = Node(value)
                # print(self.next)
            else:
                self.next.appendItem(value)
        else:
            self.value = value
        self.size += 1


my_linkedList = Node(4)
# my_linkedList.LinkedList()
my_linkedList.appendItem(2)
my_linkedList.appendItem(4)
my_linkedList.appendItem(7)
# my_linkedList.popList()
my_linkedList.prependList(5)
my_linkedList.prependList(13)
# my_linkedList.printList()
my_linkedList.printBorder()
# my_linkedList.appendItem(2)
