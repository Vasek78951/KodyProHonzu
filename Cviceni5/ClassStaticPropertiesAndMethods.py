class KonfiguraceKonference:

    _maximalni_pocet_ucastniku = 0
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def set_maximalni_pocet_ucastniku(cls, max):
        cls._maximalni_pocet_ucastniku = max;

    @classmethod
    def get_maximalni_pocet_ucastniku(cls):
        return cls._maximalni_pocet_ucastniku;


mojeKonfigurace = KonfiguraceKonference()
print(mojeKonfigurace.get_maximalni_pocet_ucastniku())

mojeKonfigurace.set_maximalni_pocet_ucastniku(212)
print(mojeKonfigurace.get_maximalni_pocet_ucastniku())

mojeKonfigurace2 = KonfiguraceKonference()
mojeKonfigurace2.set_maximalni_pocet_ucastniku(300)
print(mojeKonfigurace2.get_maximalni_pocet_ucastniku())
print(mojeKonfigurace2.get_maximalni_pocet_ucastniku())