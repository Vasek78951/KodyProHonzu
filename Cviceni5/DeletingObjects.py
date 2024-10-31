#Deleting an Object with del
class Zbozi:

    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print(f"Zbozi '{self.nazev}' bylo vymazano z pameti.")

# Step 1: Create an object and delete it
z = Zbozi("Banán")
del z  # Manually deleting the object

# Output: Zbozi 'Banán' bylo vymazano z pameti.

#Running the Program Without del
class Zbozi:
    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print(f"Zbozi '{self.nazev}' bylo vymazano z pameti.")

# Step 2: Create an object but don't explicitly delete it
z = Zbozi("Banán")

print("Konec programu")  # Add this to see the program end clearly


#Multiple References to the Same Object

class Zbozi:
    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print(f"Zbozi '{self.nazev}' bylo vymazano z pameti.")

# Step 3: Create an object and another reference to the same object
z = Zbozi("Banán")
me_oblibene_zbozi = z  # Two references to the same object

del z  # Delete only one reference

print("Konec programu")

# Output will be:
# Konec programu
# Zbozi 'Banán' bylo vymazano z pameti.