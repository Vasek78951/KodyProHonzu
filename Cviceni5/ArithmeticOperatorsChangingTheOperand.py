import re
from idlelib.run import Executive


class PenezniHotovost:
    """
    Trida reprezentuje penezni hotovost v urcite mene
    """

    def __init__(self, castka: float, mena: str):
        """
        Pri vytvoreni tridy se musi specifikovat castka a mena, nebo se pouzije defaultnich 0 EUR

        :param castka: Jakekoli realne cislo, muze byt i zaporne
        :param mena: Mena vyjadrena jako tripismeny kod
        :return: Objekt penezni hotovosti
        """
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._mena = mena
        self._castka = castka

    def __str__(self):
        """
        Vrati castku a menu jako string
        :return: <castka> <mena>
        """
        return str(self._castka)+" "+self._mena

    def __add__(self, other):
        """
        Pretizeni operatoru + ktere vytvori novy objekt jako vysledek operace scitnai
        :param other: Lze scitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")

    def __sub__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other
            return vysledek

        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other._castka
            return vysledek

        raise Exception("Penezni hotovost lze odecitat pouze s int,float a hotovosti ve stejne mene")

    def __mul__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other
            return vysledek

        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other._castka
            return vysledek

        raise Exception("Penezni hotovost lze nasobit pouze s int,float a hotovosti ve stejne mene")
    def __pow__(self, power, modulo=None):
        if not isinstance(power, (int, float)):
            raise Exception("Exponent musi byt typy int nebo float.")

        vysledek = PenezniHotovost(self._castka ** power, self._mena)
        return vysledek

    def __truediv__(self, other):
        """
        Implementace operatori /= ma za ukol vydelit hotovost a zachovat puvodni objekt
        :param other: Muze byt int, float nebo trida PenezniHotovost
        :return: Vraci stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace deleni
        """
        if (isinstance(other, float) or isinstance(other, int)):
            self._castka /= other
            return self

        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka /= other._castka
            return self

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")
    def __iadd__(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            self._castka += other
            return self
        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka += other._castka
            return self
        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")
    def isub(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            self._castka -= other
            return self
        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka -= other._castka
            return self
        raise Exception("Penezni hotovost lze odecitat pouze s int,float a hotovosti ve stejne mene")
    def imul(self, other):
        if (isinstance(other, float) or isinstance(other, int)):
            self._castka *= other
            return self
        if (isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka *= other._castka
            return self
        raise Exception("Penezni hotovost lze nasobit pouze s int,float a hotovosti ve stejne mene")
sto_korun = PenezniHotovost(100, "CZK")
dve_sta_korun = sto_korun + 100

print(sto_korun)
print(dve_sta_korun)

hotovost_umocnena = (sto_korun ** 2)
print(hotovost_umocnena)

vyplata = PenezniHotovost(1000, "CZK")
vyplata /= 2
print(vyplata)

vyplata = PenezniHotovost(1000, "CZK")
vyplata += 2000 #1000 + 2000 = 3000
vyplata -= 500 #3000 - 500 = 2500
vyplata *= 2 #2500 * 2 = 5000
print(vyplata) #ma vypsat 5000