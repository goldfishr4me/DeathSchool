import game   
from player import Player
import world


                
def get_player_command():
    """the player input"""
    return raw_input('Action: ').lower().strip()




### Main Script
print("++++++++++++++++++++++++++++++++++")
print("|      DEATHSCHOOL!!!!           |")
print("|           By: Cori Sparks      |")
print("++++++++++++++++++++++++++++++++++\n\n\n")
print("You walk up the stairs on the first day of school.\n Something doesn't feel right......\n The parking lot was full, but building is eerily silent.\n")
player = Player()

while True:
    room = world.tile_at(player.x, player.y)
    print(room.intro_text())
    room.modify_player(player)
    action_input = get_player_command()
    if action_input == 'w':
        player.move_forward()
    elif action_input == 's':
        player.move_backward()
    elif action_input == 'a':
        player.move_left()
    elif action_input == 'd':
        player.move_right()
    elif action_input == 'b':
        player.print_pack()
    elif action_input == 'f':
        player.attack()
    elif action_input == 'q':
        break
    else:
        print("Invalid!")
        
        
