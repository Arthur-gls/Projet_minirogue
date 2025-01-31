
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
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN :
        key = event.name
        
    next_move = move(key, position)
    next_type = TYPES(map[next_move])

    if next_type in ('room', 'door', 'corridor', 'staircase'):
        position = next_move

    else :
        position = next_move
    
    

    mise_a_jour(arene)


