#Enemy
class Enemy:
    """base class for all enemies"""
    def __init__(self, name, lifepoints, damage):
        self.name = name
        self.lifepoints = lifepoints
        self.damage = damage
 
    def is_alive(self):
        return self.lifepoints > 0
class Guilt(Enemy):
    def __init__(self):
        super().__init__(name="Guilt", lifepoints = 10, damage = 3)
class Homework(Enemy):
    def __init__(self):
        super().__init__(name="Homework", lifepoints=5, damage=2)
 
 
class ResearchPaper(Enemy):
    def __init__(self):
        super().__init__(name="Research Paper", lifepoints=30, damage=15)

#boss 
class Procrastination(Enemy):
    def __init__(self):
        super().__init__(name="Procrastination", lifepoints=50, damage=20)
