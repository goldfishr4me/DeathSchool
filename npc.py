import items

class Npc(object):
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name

class Trader(Npc):
    def __init__(self):
        self.name = "Shop Keeper"
        self.Money = 10000
        self.backpack = [items.Coffee(),
                         items.Coffee(),
                         items.Bagle(),
                         items.Bagle(),
                         items.FlashDrive,
                         items.Ramen()]
        
                         
    
