class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            raise IndexError('Stack is empty')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def clear(self):
        self.head = None
        self.size = 0

    def pop_all(self):
        elements = []
        while self.head:
            elements.append(self.pop())
        return elements

    def count(self):
        return self.size


stack = Stack()

# Přidání prvků do zásobníku
stack.add(10)
stack.add(20)
stack.add(30)
stack.add(40)
stack.add(50)

print("Počet prvků v zásobníku:", stack.count())

# Odebrání vrchního prvku
print("Odebrán prvek:", stack.pop())
print("Počet prvků po odebrání jednoho prvku:", stack.count())

# Získání všech prvků a vyprázdnění zásobníku
print("Všechny prvky v zásobníku:", stack.pop_all())
print("Počet prvků po vyprázdnění:", stack.count())

# Vyprázdnění zásobníku znovu
stack.clear()
print("Zásobník vyprázdněn.")
print("Počet prvků po vyprázdnění:", stack.count())

# Ošetření chyby při pokusu odebrat z prázdného zásobníku
try:
    stack.pop()
except IndexError as e:
    print(e)  # Očekávaná chyba: "Zásobník je prázdný."