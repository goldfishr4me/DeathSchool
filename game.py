class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
#Given Items

class Gold(Item):
    """Currency"""
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
        description="A round coin with {} stamped on the front.".format(str(self.amt)),
        value=self.amt)
class Weapon(Item):
    """Items that will Damage enemies"""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value) 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 
class Pencil(Weapon):
    def __init__(self):
        super().__init__(name="Pencil",
                         description="Only useful if sharpened",
                         value=0,
                         damage=5)
class Ruler(Weapon):
    def __init__(self):
        super().__init__(name="Ruler",
                         description="A metal Ruler with cork backing. Can come in handy for measurements or self defense.",
                         value=10,
                         damage=10)
#first aid
class Coffee(Item):
    def __init__(self,restore):
        self.restore = restore
        super(). __init__(name="Coffee!", description="Restores 10 lifepoints", value = 5, restore = 10)
    
