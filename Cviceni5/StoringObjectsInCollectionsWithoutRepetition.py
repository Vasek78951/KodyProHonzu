import re
class Zbozi:
    """ Trida zbozi pro ukazu prikladu relacnich operatoru"""

    def __init__(self, nazev: str, vaha: float):
        """
        Pri vytvoreni se nastavuje nazev zbozi a jeho vaha
        :param nazev: Nazev musi byt znaky v rozsahu 1 az 200 znaku
        :param vaha: Vaha musi byt kladne a nenulove cislo
        """
        if not re.match(r"^[\D ]{1,200}$", nazev):
            raise Exception('Nazev musi byt v rozsahu 1 az 200 znaku')
        if vaha <= 0:
            raise Exception('Vaha nesmi byt zapojna')

        self._nazev = nazev
        self._vaha = vaha

    def __lt__(self, other):
        """
        Metoda zjistuje jestli je zbozi mensi nez druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self mensi nez other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha < other._vaha
    def __gt__(self, other):
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha > other._vaha
    def __le__(self, other):
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha <= other._vaha
    def __ge__(self, other):
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha >= other._vaha
    def __eq__(self, other):
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._nazev == other._nazev and self._vaha == other._vaha
    def __ne__(self, other):
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha != other._vaha

    def __hash__(self):
        return hash((self._nazev, self._vaha))

    def __str__(self):
        return f"{self._nazev} ({self._vaha} kg)"

kilo_brambor = Zbozi("Bramobra", 1)
krabice_mleka = Zbozi("Mleko", 1.029)
if(kilo_brambor < krabice_mleka):
    print("Svet je jeste v poradku")

if kilo_brambor < krabice_mleka:
    print("Svet je jeste v poradku")

if krabice_mleka > kilo_brambor:
    print("Krabice mleka je tezsi nez kilo brambor.")

if kilo_brambor <= krabice_mleka:
    print("Kilo brambor je lehci nebo stejne tezke jako krabice mleka.")

if krabice_mleka >= kilo_brambor:
    print("Krabice mleka je tezsi nebo stejne tezka jako kilo brambor.")

if kilo_brambor == krabice_mleka:
    print("Brambory a mleko maji stejnou vahu.")

zbozi1 = Zbozi("Mrkev", 1)
zbozi2 = Zbozi("Mrkev", 1)
zbozi3 = Zbozi("Celer", 1)

x = set()
x.add(zbozi1)
x.add(zbozi2)
x.add(zbozi3)
print(len(x))