import game   

            
def get_player_command():
    """the player input"""
    return raw_input('Action: ').lower().strip()

def play():
    """Main Game Script"""

print("Alarm Rings on Syllabus Day!")
print("Is going to class really necessary?")
print("Go back to sleep? Y or N")
action_input = get_player_command()
backpack = [game.Pencil(),game.Ruler(),game.Gold(5), 'paper wads']
#while True:
    #action_input = raw_input("Y or N").lower().strip()
    #if not 'y' or 'n' :
        #print("invalid input")
        #continue
    #else:
         #break
if action_input == 'y':
    print ('...zzzzz')
    
if action_input == 'n':
    print("You're Still probably going to be five minutes late")

elif action_input == 'b':
    print ("****Backpack contents****")
    for item in backpack:
        print(str(item))
