import random
import enemies
import player

###Title Words
class MapTile(object):
    def __init__(self, x, y):
        self.x = 1
        self.y = 1

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
            self.alive_text = "You skipped class AGAIN!?\nPrepare to be eaten by GUILT!!"
            self.dead_text = "You decide to go to class anyway.\nBetter late than never:)" 
        elif r < 0.80:
            self.enemy = enemies.ResearchPaper()
            self.alive_text = "A Rabid Research paper stands before you!!\nDid you cite your sources!?\nPrepare to be expelled for plagarism!!"
            self.dead_text = "The Research Paper rips down the middle and falls at your feet" 
        elif r < 0.95:
            self.enemy = enemies.Homework()
            self.alive_text = "A ornary Homework Assignment is blocking your way.\nYou thought Homework was supposed to be done at home...\nHomework follows you EVERYWHERE!!"
            self.dead_text = "You know the answers and showed that homework who's boss" 
        else:
            self.enemy = enemies.Procrastination()
            self.alive_text = "There is nothing left to defeat, but the embodiement of PROCRASTINATION!!!\nYou can defeat your homework and a research paper... \nbut can you defeat your own bad habits?"
            self.dead_text = "Lucky for you, you do your best work under pressure."
            
        super(EnemyTile, self).__init__(x,y)
        
    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text if self.enemy.is_alive() else self.dead_text
            return text
       
        
world_map = [
            [None,VictoryTile(1,0),None],
            [None,EnemyTile(1,1),None],
            [EnemyTile(0,2), StartTile(1,2), EnemyTile(2,2)],
            [None, BoringTile(1,3),None]
            ]

def tile_at(x,y):
    """ Locates the map tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None    
            
