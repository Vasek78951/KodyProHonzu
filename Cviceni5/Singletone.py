class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b) #Musi vypsat true

a.moje_nova_promenna_pro_a = "Test"
print(a.moje_nova_promenna_pro_a) #Musi vypsat test
print(b.moje_nova_promenna_pro_a) #Musi vypsat take test