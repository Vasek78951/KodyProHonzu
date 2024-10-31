class Door:
    def __init__(self,locked):
        if not type(locked) == bool:
            raise ValueError("Door must be boolean type")
        self.locked = locked

    def open(self):
        if self.locked:
            raise LockedDoorException("Door is locked")
        print("Door opened")
class LockedDoorException(Exception):
    pass

d = Door(locked=True)
passed = False
try:
    d.open()
    passed = True
except LockedDoorException as e:
    passed = False
    raise e
finally:
    if passed:
        print("prosel jsem")
    else:
        print("neprosel jsem")


