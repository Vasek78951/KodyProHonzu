class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    def __str__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))  # Přidání dat aktuálního uzlu do seznamu
            current_node = current_node.next
        return ' '.join(elements)

linked_list = LinkedList()

# Přidání alespoň 5 prvků
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

# Výpis všech prvků na obrazovku
print(linked_list)