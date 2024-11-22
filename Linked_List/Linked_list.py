class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            # temp = self.head
            # self.head = new_node
            # self.head.next = temp
        self.length += 1

    def pop_first(self):
        if not self.head:
            return None
        elif self.head.next:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            if not self.head.next:
                self.tail = self.head
        else:
            self.head = None
            self.tail = None
        self.length -= 1

    def get(self, index):
        temp = self.head
        count = index
        if self.head:
            while count != 0:
                if temp:
                    temp = temp.next
                    count -= 1
                else:
                    return None
            if temp is not None:
                return temp.value
        else:
            return None

    def get2(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for item in range(index):
            # print(temp.value)
            temp = temp.next
        return temp.value

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        temp = self.head
        new_node = Node(value)
        if index == 0:
            return self.prepend(value)
        for _ in range(index):
            pre = temp
            temp = temp.next
        pre.next = new_node
        new_node.next = temp
        self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index == 0:
            return self.pop_first()
        for _ in range(index):
            pre = temp
            temp = temp.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1

    def reverse(self):
        temp = self.head
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        self.head.next = None
        head = self.head
        self.head = self.tail
        self.tail = head


my_linkedList = LinkedList(4)
my_linkedList.append(2)
my_linkedList.append('grow')
# my_linkedList.pop()
# my_linkedList.pop()
# my_linkedList.pop()
my_linkedList.prepend(5)
# my_linkedList.pop_first()
# my_linkedList.pop()
my_linkedList.set_value(2, 'new')
# print(my_linkedList.get(2))
print(my_linkedList.get2(2))
my_linkedList.insert(2, 7)
# my_linkedList.remove(3)
my_linkedList.reverse()
my_linkedList.print_list()
