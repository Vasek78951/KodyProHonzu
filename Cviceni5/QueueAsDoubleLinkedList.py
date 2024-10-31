class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            raise IndexError('List is empty')
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def count(self):
        return self.size

    def clear(self):
        self.head = self.tail = None
        self.size = 0

    def popAll(self):
        element = []
        while self.head:
            element.append(self.pop())
            return element


queue = Queue()

# Přidání prvků do fronty
queue.add(10)
queue.add(20)
queue.add(30)
queue.add(40)
queue.add(50)

print("Počet prvků ve frontě:", queue.count())

# Odebrání prvního prvku
print("Odebrán prvek:", queue.pop())
print("Počet prvků po odebrání jednoho prvku:", queue.count())

# Získání všech prvků a vyprázdnění fronty
print("Všechny prvky ve frontě:", queue.popAll())
print("Počet prvků po vyprázdnění:", queue.count())

# Vyprázdnění fronty znovu
queue.clear()
print("Fronta vyprázdněna.")
print("Počet prvků po vyprázdnění:", queue.count())

# Ošetření chyby při pokusu odebrat z prázdné fronty
try:
    queue.pop()
except IndexError as e:
    print(e)  # Očekávaná chyba: "Fronta je prázdná."

