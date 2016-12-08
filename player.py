import game
import world
import enemies

class Player(object):
    def __init__(self):
        self.backpack = [game.Pencil(),
                         game.Ruler(),
                         game.Money(5),
                         'paper wads']
        self.x =1
        self.y =2
        self.lifepoints =100
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def move_forward(self):
        self.move(dx=0,dy=-1)
        
    def move_backward(self):
        self.move(dx=0,dy=1)
        
    def move_right(self):
        self.move(dx=1,dy=0)
        
    def move_left(self):
        self.move(dx=-1,dy=0)

    def print_pack(self):
        print ("***Backpack Contents***")
        best_weapon = self.most_powerful_weapon()
        for item in self.backpack:
            print(item)
        print ("\nYour best weapon is your {}\n" .format(best_weapon.name))
            
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

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x,self.y)
        enemy = room.enemy
        print("You use the {} against {}!".format(best_weapon.name, enemy.name))
        enemy.lifepoints -= best_weapon.damage
        if not enemy.is_alive():
            print("You Killed the {}!" .format(enemy.name))
        else:
            print ("{}'s Life Points are {}." .format(enemy.name, enemy.lifepoints))
            
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.lifepoints = player.lifepoints - self.enemy.damage
            print ("Enemy does {} damage. You Have {} Life Points remaining.".format(self.enemy.damage,player.lifepoints))
            
        
