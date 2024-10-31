import re
class Zbozi:
    def __new__(cls, nazev, cena):
        if not re.match("[0-9]+", nazev):
            instance = None
        elif cena < 0:
            instance = None
        elif not re.match("[A-Za-z]+", nazev):
            instance = None
        else:
            instance = super().__new__(cls)
        return instance
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena


a = Zbozi("", 5)
b = Zbozi("Hackers item", "dadwa")

print(a)
print(b)