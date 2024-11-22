class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.next = None
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = None

    def callAppend(self, List):
        for node in List:
            self.append(node)

    def reverse(self):
        previous = None
        current_node = self.head
        while current_node:
            next = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next
        head = self.head
        self.head = self.tail
        self.tail = head

    def removeNth(self, index):
        current_node = self.head
        nodecount = 0
        while current_node:
            nodecount += 1
            current_node = current_node.next

        if index < 0 or index > nodecount-1:
            return False

        temp = self.head

        if index == 0:
            self.head = temp.next
            temp.next = None

        for count in range(index):
            current = temp
            next_node = temp.next
            if count == index-1:
                current.next = next_node.next
                next_node.next = None
        return True

    def printList(self):
        current_node = self.head
        results = []
        while current_node:
            results.append(current_node.value)
            current_node = current_node.next
        return results


List = ['grow', 5, 7, 8, 'new']
linkedList = LinkedList()
linkedList.callAppend(List)
linkedList.reverse()
# print(linkedList.removeNth(0))
print(linkedList.printList())
