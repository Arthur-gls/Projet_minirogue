
import keyboard

TYPES = {'-' : 'wall', ' ': 'wall', '|' : 'wall', '.' : 'room', '#' : 'corridor', '+' : 'door', '=' : 'staircase'}


position = 

def move (key, position):
    x, y = position
    if key == 'left' :
        next_move = x - 1, y
    if key == 'right' :
        next_move = x + 1, y
    if key == 'up' :
        next_move = x, y - 1
    if key == 'down' :
        next_move = x, y - 1
    return next_move

WAIT = True

while WAIT :
    if keyboard.key_pressed('up') or keyboard.key_pressed('down') or keyboard.key_pressed('right') or keyboard.key_pressed('left'):


        key = keyboard.read_key()
        next_move = move(key, position)
        next_type = TYPES(map[next_move])

        if next_type == 'wall' :
            print_map()

        if next_type in ('room', 'door', 'corridor') :
            position = next_move
            print_map()

        if next_type == 'staircase' :
            position = next_move
            print_map()


