


TYPES = {'-' : 'wall', ' ': 'wall', '|' : 'wall', '.' : 'room', '#' : 'corridor', '+' : 'door', '=' : 'staircase'}

next_move = x, y

if type(map[next_move]) == 'wall' :


if type(map[next_move]) == 'room' :
    coord_x, coord_y = next_move
