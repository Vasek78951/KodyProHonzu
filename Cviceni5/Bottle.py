

class Bottle:
    def __init__(self,capacity):
        """
        Creates a new bottle of capacity,volume,max_volume
        :param capacity: liters
        """
        if not isinstance(capacity, (float, int)):
            raise Exception("Invalid type of capacity")
        if not capacity >= 0.2 and capacity <= 10:
            raise Exception("Invalid capacity")
        self.capacity = capacity
        self.volume = 0
        self.is_closed = False

    def open_bottle(self):
        self.is_closed = False
    def close_bottle(self):
        self.is_closed = True

    def set_volume_liters(self, volume):
        """
        sets the volume of the bottle if the bottle is not closed and volume is not bigger than capacity
        :param volume: liters
        :return:
        """
        if not isinstance(volume, (float, int)):
            raise Exception("Invalid type of volume")
        if volume < 0:
            raise Exception("Invalid volume")
        if self.is_closed:
            return "Lahev je zavrena"
        if volume > self.capacity:
            self.volume = self.capacity
        else:
            self.volume = volume
    def get_volume_liters(self):
        """
        :return: volume in liters
        """
        return self.volume
    def empty_bottle(self):
        if self.is_closed:
            return "lahev je zavrena"
        else:
            self.volume = 0

    def set_volume_milliliters(self, volume_milliliters):
        if  not isinstance(volume_milliliters, (float, int)):
            raise Exception("Invalid type of volume")
        if volume_milliliters < 0:
            raise Exception("Invalid volume")
        volume_liters = volume_milliliters / 1000
        return self.set_volume_liters(volume_liters)

    def get_volume_milliliters(self):
        return self.volume * 1000

# Ukázka použití
bottle = Bottle(1.5)  # Kapacita láhve je 1,5 litru
bottle.open_bottle()  # Otevřeme láhev
bottle.set_volume_liters(1.2)  # Nastavíme objem 1,2 litru
print(bottle.get_volume_liters())  # Získáme aktuální objem v litrech (1.2 litru)
bottle.close_bottle()  # Zavřeme láhev
print(bottle.set_volume_milliliters(500))  # Pokusíme se změnit objem kapaliny (láhev je zavřená)
bottle.open_bottle()  # Otevřeme láhev
bottle.set_volume_milliliters(500)  # Nastavíme objem kapaliny v mililitrech
print(bottle.get_volume_milliliters())  # Získáme aktuální objem v mililitrech (500 ml)