class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return ' '.join(elements)

    def backward_str(self):
        elements = []
        current_node = self.tail
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.prev
        return ' '.join(elements)


dll = DoubleLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

print("Výpis od prvního k poslednímu:")
print(dll)

print("Výpis od posledního k prvnímu:")
print(dll.backward_str())