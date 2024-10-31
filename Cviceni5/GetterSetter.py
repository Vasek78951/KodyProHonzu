class Obdelnik:
    def __init__(self, sirka=0, vyska=0):
        self._sirka = 0
        self._vyska = 0
        self.sirka = sirka
        self.vyska = vyska

    @property
    def sirka(self):
        return self._sirka

    @sirka.setter
    def sirka(self, hodnota):
        if hodnota < 0:
            raise ValueError("Šířka nemůže být záporná.")
        self._sirka = hodnota

    @property
    def vyska(self):
        return self._vyska

    @vyska.setter
    def vyska(self, hodnota):
        if hodnota < 0:
            raise ValueError("Výška nemůže být záporná.")
        self._vyska = hodnota

    def __str__(self):
        return f"Obdélník: šířka = {self.sirka}, výška = {self.vyska}"

obdelnik = Obdelnik(5, 10)
print(obdelnik)  # Obdélník: šířka = 5, výška = 10

obdelnik.sirka = 20
print(obdelnik.sirka)  # 20

obdelnik.vyska = -5  # This will raise a ValueError: Výška nemůže být záporná.