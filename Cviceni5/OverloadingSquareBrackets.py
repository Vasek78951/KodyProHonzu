class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self._current = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.size += 1
    def __str__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))  # Přidání dat aktuálního uzlu do seznamu
            current_node = current_node.next
        return ' '.join(elements)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index >= self.size < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    def __setitem__(self, index, value):
        if index >= self.size < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

    def __contains__(self, item):
        for i in range(len(self)):
            if self[i] == item:
                return True
        return False

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            data = self._current.data
            self._current = self._current.next
            return data
linked_list = LinkedList()

# Přidání alespoň 5 prvků
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Výpis všech prvků na obrazovku
print(linked_list)

print(len(linked_list))

print(linked_list[2])

linked_list[0] = ("Pepa")
print(linked_list[0])

if "Pepa" in linked_list:
    print("Pepa je v seznamu")

for prvek in linked_list:
    print(prvek)  # Očekávaný výstup: A, B, C

# Použití iterátoru ručně pomocí next()
iterator_seznamu = iter(linked_list)
try:
    print(next(iterator_seznamu))  # A
    print(next(iterator_seznamu))  # B
    print(next(iterator_seznamu))  # C
    print(next(iterator_seznamu))  # StopIteration
except StopIteration:
    print("Iterace je dokončena.")