class Auto:
    """ Trida auto reprezentuje auto pro simulaci realneho vozidlo pro cviceni PV na SPSE Jecna """

    def __init__(self, objem_nadrze_l : float, spotreba_na_100_km_l : float):
        """
        Konstruktor nastavi objem nadrze a spotrebu dle parametru a nastavi prazdnou nadrz.

        :param objem_nadrze_l: Objem nadrze v litrech
        :param spotreba_na_100_km_l: Spotreba na 100km v litrech
        """

        if (objem_nadrze_l < 0):
            raise Exception("Nadrz musi mit kladny objem")
        if (spotreba_na_100_km_l < 0):
            raise Exception("Spotreba nesmi byt zaporna")

        self.objem_nadrze_l = objem_nadrze_l
        self.spotreba_na_100_km_l = spotreba_na_100_km_l
        self._aktualni_objem_paliva_v_nadrzi_l = 0
        self._pocet_najetych_km = 0

    def aktualni_stav_nadrze(self) -> float:
        """
        Metoda vrati aktualni stav nadrze

        :return: Zbyle palivo v nadrzi v litrech
        """
        return self._aktualni_objem_paliva_v_nadrzi_l

    def natankuj(self, objem_l : float ) -> None:
        """
        Metoda prida zadany objem paliva do nadrze.

        :param objem_l: objem paliva v litrech, ktere chceme natankovat.
        :return: nic, pouze upravuje stav nadrze
        """
        if(objem_l < 0):
            raise Exception("Nelze odcerpat palivo pomoci metody natankovat")

        if((self._aktualni_objem_paliva_v_nadrzi_l + objem_l) > self.objem_nadrze_l):
            raise Exception("Nelze nacerpat vice nez je kapacita nadrze")

        self._aktualni_objem_paliva_v_nadrzi_l += objem_l

    def popojed(self, pocet_km : float ) -> None:
        """
        pricita najete km a odcita ovjem paliva v nadrzi

        :param pocet_km: pocet kilometru, ktere checeme ujet
        :return:nic, pouze upravuje stav nadrze a pricita pocet ujetych kilometru
        """
        if(pocet_km < 0):
            raise Exception("Couvani je take jizda, smer neresime")

        spotreba_paliva_l = pocet_km/100.0 * self.spotreba_na_100_km_l
        self._pocet_najetych_km += pocet_km

        if(self._aktualni_objem_paliva_v_nadrzi_l < spotreba_paliva_l):
            raise Exception("Na jizdu neni dostatek paliva")

        self._aktualni_objem_paliva_v_nadrzi_l -= spotreba_paliva_l

    def aktualni_stav_najetych_km(self) -> float:
        """
        Metoda vrati aktualni poset najetych kilometru

        :return: pocet najetych kilometru
        """
        return self._pocet_najetych_km
a = Auto(30, 12.5)
a.natankuj(22.5)
a.popojed(20)

"""
1.Jaké jsou atributy/vlastnosti třídy?
    objem_nadrze_l, spotreba_na_100_km_l, aktualni objem paliva n narzi
2.Jaké atributy/vlastnosti třídy jsou public a jaké private?
    Public: objem_nadrze_l, spotreba_na_100_km_l
    Private: _aktualni_objem_paliva_v_nadrzi_l
3.Jak je řešen ve třídě princip zapouzdření, jak se manipuluje s private atributy?
    zapozrdreni je implementovano pomoci privatniho atributu _aktualni_objem_paliva_v_nadrzi_l,
     ktery lze ovladat prostrednictvim verejnych metod tridy 
"""


