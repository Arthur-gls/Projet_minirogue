import keyboard
class Objets:
    arme_de_base = ["contact",1]
    épée = ["contact",2]
    hache = ["contact",3]
    lance = ["contact",4]
    baton = ["contact",1]
    dague = ["contact",6]
    arc = ["distance",2]
    arbalète = ["distance",3]
    fronde = ["distance",1]
    marteau = ["contact",5]

    veste_en_cuir = [3]
    gilet_jaune = [30]
    armure_en_or = [10]
    armure_de_bois = [5]
    armure_de_fer = [7]
    armure_de_diamant = [15]
    armure_de_cristal = [20]

    def __init__(self,arme_de_base, épée, hache, lance, baton, dague, arc, arbalète, fronde, marteau, veste_en_cuir, gilet_jaune, armure_en_or, armure_de_bois, armure_de_fer, armure_de_diamant, armure_de_cristal):
        self.armes = [arme_de_base, épée, hache, lance, baton, dague, arc, arbalète, fronde, marteau]
        self.armures = [veste_en_cuir, gilet_jaune, armure_en_or, armure_de_bois, armure_de_fer, armure_de_diamant, armure_de_cristal]

class Sac(Objets):
    def __init__ (self):
        self.compteur_or = 0
        self.armes = [Objets.arme_de_base]
        self.armures = []
        self.potions = []


sac = Sac()
print(sac.armes)

# Données de l'arène

LENGHT = 30
WIDTH = 30
MUR_H = "_"
MUR_V = "|"
INTERIOR = "."
DOOR = "+"
COULOIR = "#"


def salle(map, i1, j1, i2, j2):
    # On crée les murs

    for i in range(i1 + 1, i2):
        map[i][j1] = MUR_V
        map[i][j2] = MUR_V
    for j in range(j1, j2 + 1):
        map[i1][j] = MUR_H
        map[i2][j] = MUR_H

    # On remplit la salle

    for i in range(i1 + 1, i2):
        for j in range(j1 + 1, j2):
            map[i][j] = INTERIOR

    return map


def porte(map, i, j):
    map[i][j] = DOOR

    return map


def couloir(map, i1, j1, i2, j2, direction):
    if direction == "h":
        for j in (j1 + 1, j2):
            map[i1][j] = COULOIR
    elif direction == "v":
        for i in (i1 + 1, i2):
            map[i][j1] = COULOIR

    return map


def arena(LENGHT, WIDTH):
    map = [[" " for i in range(WIDTH)] for j in range(LENGHT)]  # On crée l'arène vide

    # On crée des salles

    map = salle(map, 0, 0, 29, 9)
    map = salle(map, 0, 20, 29, 29)

    # On crée des portes

    map = porte(map, 14, 9)
    map = porte(map, 14, 20)

    # On crée le couloir

    map = couloir(map, 14, 9, 14, 20, "h")

    return map


#print(arena(LENGHT, WIDTH))




nested_list = [
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['|', '1', '1', '1', '2', '1', '1', '|'],
    ['-', '-', '-', '-', '-', '-', '-', '-']
]

nested_list2 = [
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['|', '1', '1', '1', '1', '2', '1', '|'],
    ['-', '-', '-', '-', '-', '-', '-', '-']
]

bg_test2 = ['--------',
            '|   G  |',
            '--------']

def print_bg(background):
    for line in background:
        s = ''
        for char in line:
            s += char
        print(s)



TYPES = {'-' : 'wall', ' ': 'wall', '|' : 'wall', '.' : 'room', '#' : 'corridor', '+' : 'door', '=' : 'staircase'}


def get_position(arene):
    return position

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
   
import time
import os 
print_bg(nested_list)
time.sleep(0.2)
os.system("cls")
print_bg(nested_list2)
time.sleep(0.2)
os.system("cls")
print_bg(nested_list)
time.sleep(0.2)
os.system("cls")
print_bg(nested_list2)

