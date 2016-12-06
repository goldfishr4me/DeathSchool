import game
class Player(object):
    def __init__(self, backpack):
        self.backpack = [game.Pencil(),
                         game.Ruler(),
                         game.Gold(5),
                         'paper wads']

    def print_pack(self):
        print ("***Backpack Contents***")
        for item in self.backpack:
            print(str(item))
            best_weapon = self.most_powerful_weapon()
            print ("Your best weapon is your {}" .format(best_weapon))
            
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.backpack:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
            return best_weapon
        
