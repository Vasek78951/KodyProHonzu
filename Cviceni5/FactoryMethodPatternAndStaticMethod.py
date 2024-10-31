class Firma:
    """ Třída reprezentuje firmu"""

    @staticmethod
    def factory_from_obchodni_nazev(Name):
        name, legal_form = Name.rsplit(", ", 1)
        return Firma(name, legal_form)
    def __init__(self, nazev, pravni_forma):
        """
        Vytvoří instanci firmy
        :param nazev: Název například Maso a uzeniny od Pavlíka
        :param pravni_forma: Právní forma, například s.r.o, nebo a.s. apod.
        """
        self.jmeno = nazev
        self.pravni_forma = pravni_forma

sporka = Firma.factory_from_obchodni_nazev("Česká spořitelna, a.s.")
print(sporka.pravni_forma) #ma vypsat "a.s."