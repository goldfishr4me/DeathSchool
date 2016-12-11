# DeathSchool
School themed text adventure written to better understand the python language. 

## Files
action.py: main game function
game.py: item classes 
player.py: player class and functions 
world.py: maptile classes and functions 
npc.py: vendor classes and trading functions

## Controls 
w: forward 
s: backward
a: left 
d: right 
b: backpack 
h: heal
x: exit
you must press enter after selecting a hotkey.
The controls can be upper or lowercase, it shouldn't affect the game if you enter empty spaces after
the letter. 

### Map 
consists of 16 tiles. The start tile is on (2,3). The victory tile is (0,2). Other tiles include: 
Enemy tiles, nothing tiles, and trader tiles
    [EnemyTile(0,0),EnemyTile(0,1),VictoryTile(0,2),EnemyTile(0,3),EnemyTile(0,4)],
    [EnemyTile(1,0),BoringTile(1,1),BoringTile(1,2),BoringTile(1,3),EnemyTile(1,4)],
    [EnemyTile(2,0),FindGoldTile(1,2),EnemyTile(2,2),BoringTile(2,3),TraderTile(2,4)],
    [TraderTile(3,0),BoringTile(3,1),StartTile(3,2),FindGoldTile(3,3),EnemyTile(3,4)],
    [FindGoldTile(4,0),BoringTile(4,1),EnemyTile(4,2),BoringTile(4,3),FindGoldTile(4,4)]

#### Issues with the game 
The game is functioning and playable for the most part. The only things that need to be fixed is 
the player can't really die and the health goes into the negative, and the player can go off the map and it
causes an error. I will fix these issues when I have more time. 

#### Plans for the future
To fix the issues previously mentioned. I would like to add a boss enemy before the victory tile that always
spawns no matter what. You would have to buy a better weapon in order to beat it, so you would have to visit every room to get enough money. 
I would also like to make it to where the monsters drop money and items when they die. Because I have already set up trading functions, I don't think that 
this will be too much of an issue. 

 