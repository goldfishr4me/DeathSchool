class Item(object):
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "\n\n{}\n-----\n{}\nValue: {}\n".format(self.name, self.description, self.value)
#Given Items

class Money(Item):                        
    """Currency"""
    def __init__(self, amt):
        self.amt = amt
        super(Money, self).__init__(name="Money",
        description="A Paper Bill with {} stamped on the front.".format(str(self.amt)),
        value=self.amt)
        
class Weapon(Item):
    """Items that will Damage enemies"""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super(Weapon, self).__init__(name, description, value) 
    def __str__(self):
        return "\n\n{}\n-----\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 
class Pencil(Weapon):
    def __init__(self):
        super(Pencil, self).__init__(name="Pencil",
                                     description="Only useful if sharpened",
                                     value=0,
                                     damage=1)
class Ruler(Weapon):
    def __init__(self):
        super(Ruler, self).__init__(name="Ruler",
                         description="A metal Ruler with cork backing. Can come in handy for measurements or self defense.",
                         value=5,
                         damage=5)
#consumables
class Consumable(object):
    def __init__(self, name, description, value,healing_value):
       
        self.name = name
        self.description = description
        self.value = value
        self.healing_value = healing_value
 
    def __str__(self):
        return "\n\n{}\n-----\n{}\nValue: {}\n".format(self.name, self.description, self.value, self.healing_value)

class Coffee(Consumable):
    def __init__(self):
       super(Coffee, self).__init__(name="Coffee",
        description="Just what you needed!",
        value=5,healing_value = 10)
