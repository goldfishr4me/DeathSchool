import random
import enemies
import player

###Title Words
class MapTile(object):
    def __init__(self, x, y):
        self.x = 1
        self.y = 2

    def intro_text(self):
        raise NotImplementedError("Create a subclass instread!")

    def modify_player(self, player):
        pass 
    

    
class StartTile(MapTile):
    def intro_text(self):
        print("You are standing in the building's threshhold.\n There are 4 hallways in front of you.")
           

class BoringTile (MapTile):
    def intro_text(self):
        print ("You can't just leave! You have to find out whats going on!")

class VictoryTile(MapTile):
    def intro_text(self):
        print("You saved the school and all your classmates!!\n Now can you pass your test next week?\n")

class EnemyTile(MapTile):
    def __init__(self, x,y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.Guilt()
            self.alive_text = "\nYou skipped class AGAIN!?\nPrepare to be eaten by GUILT!!"
            self.dead_text = "\nYou decide to go to class anyway.\nBetter late than never:)" 
        elif r < 0.80:
            self.enemy = enemies.ResearchPaper()
            self.alive_text = "\nA Rabid Research paper stands before you!!\nDid you cite your sources!?\nPrepare to be expelled for plagarism!!"
            self.dead_text = "\nThe Research Paper rips down the middle and falls at your feet" 
        elif r < 0.95:
            self.enemy = enemies.Homework()
            self.alive_text = "\nAn ornary Homework Assignment is blocking your way.\nYou thought Homework was supposed to be done at home...\nHomework follows you EVERYWHERE!!"
            self.dead_text = "\nYou know the answers and showed that homework who's boss" 
        else:
            self.enemy = enemies.Procrastination()
            self.alive_text = "\nIts the embodiement of PROCRASTINATION!!!\nYou can defeat your homework and a research paper... \nbut can you defeat your own bad habits?"
            self.dead_text = "\nLucky for you, you do your best work under pressure."
            
        super(EnemyTile, self).__init__(x,y)
        
    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text if self.enemy.is_alive() else self.dead_text
            return text
        
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.lifepoints = player.lifepoints - self.enemy.damage
            print ("\nEnemy does {} damage. You Have {} Life Points remaining.".format(self.enemy.damage,player.lifepoints))
       
        
world_map = [
            [None,VictoryTile(1,0),None],
            [None,EnemyTile(1,1),None],
            [EnemyTile(0,2), StartTile(1,2), EnemyTile(2,2)],
            [None, BoringTile(1,3),None]
            ]

tile_type_dict = {"VT" : VictoryTile,
                  "EN" : EnemyTile,
                  "ST": StartTile,
                  "  ": None}

world_dsl = """
|  |VT|  |
|  |EN|  |
|EN|ST|EN|
|  |EN|  |
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError ("Dsl is Invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cells in enumerate(dsl_cells):
            tile_type = title_type_dict[dsl_cells]
            row.append(tile_type(x,y) if tile_type else None)

        world_map.append(row)


def tile_at(x,y):
    """ Locates the map tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None    
            
