
import time
import time
import time
import os 
import keyboard
import copy

class Objets:
    arme_de_base = ["arme", "contact",1]
    épée = ["arme", "contact",2]
    hache = ["arme", "contact",3]
    lance = ["arme", "contact",4]
    baton = ["arme", "contact",1]
    dague = ["arme", "contact",6]
    arc = ["arme", "distance",2]
    arbalète = ["arme", "distance",3]
    fronde = ['arme', "distance",1]
    marteau = ['arme', "contact",5]

    veste_en_cuir = ["armure", 3]
    gilet_jaune = ["armure", 30]
    armure_en_or = ["armure", 10]
    armure_de_bois = ["armure", 5]
    armure_de_fer = ["armure", 7]
    armure_de_diamant = ["armure", 15]
    armure_de_cristal = ["armure", 20]
    slip = ["armure", 0]

    bouteille_eau = ['potion', 'bouteille_eau', 1]
    bouteille_whisky = ['potion', 'bouteille_whisky', 2]
    poison = ['potion', 'poison', -8]
    potion_guerison = ['potion', 'potion_guerison', 10]

    def __init__(self,arme_de_base, épée, hache, lance, baton, dague, arc, arbalète, fronde, marteau, veste_en_cuir, gilet_jaune, armure_en_or, armure_de_bois, armure_de_fer, armure_de_diamant, armure_de_cristal):
            self.armes = [arme_de_base, épée, hache, lance, baton, dague, arc, arbalète, fronde, marteau]
            self.armures = [veste_en_cuir, gilet_jaune, armure_en_or, armure_de_bois, armure_de_fer, armure_de_diamant, armure_de_cristal, slip]

class Sac(Objets):
    def __init__ (self):
        self.compteur_or = 0
        self.armes = [Objets.arme_de_base]
        self.armures = []
        self.potions = {'bouteille_eau' : 0, 'bouteille_whisky' : 0, 'poison' : 0, 'potion_guerison' : 0}
        self.gold = 5
        self.protection = 0
    def add_object(self, object):
        object_type = object[0]
        if object_type == 'arme' : 
            self.armes.append(object)
        if object_type == 'armure' :
            self.armures.append(object)
            self.protection += object[1]
        if object_type == 'potion' :
            self.potion[object[1]] += 1
    def use_potion(self, potion):
        self.potions[potion[1]] -= 1
    def add_gold (self, gold):
        self.gold += gold

class Joueur ():
    def __init__(self, x, y, sac):
        self.coord_x = x
        self.coord_y = y
        self.points = 10
        self.sac = sac
        self.arme_equipee = Objets.arme_de_base
        self.degats = 1
    def move(self, new_position):
        x, y = new_position
        self.coord_x = x
        self.coord_y = y
    def add_points(self, points):
        self.points += points
    def hit(self, points):
        self.points -= points

class Enemy ():
    def __init__(self, x, y, pv, stuff, degats):
        self.coord_x = x
        self.coord_y = y
        self.points = pv
        self.stuff = stuff
        self.degats = degats
    def hit(self, points, joueur):
        self.points -= points
        if self.points <= 0 :
            for objet in self.stuff :
                joueur.sac.add_object(objet)





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
        for j in range(j1, j2+1):
            map[i1][j] = COULOIR
    elif direction == "v":
        for i in range(i1, i2+1):
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

import random as rd

def random_arena(l,w):
    map=[[" " for i in range(WIDTH)] for j in range(LENGHT)]

    p1=(rd.randint(0,l-9),rd.randint(0,w-9))
    p2=(rd.randint(p1[0]+2,l-7),rd.randint(p1[1]+2,w-7))

    i1,j1=p1[0],p1[1]
    i2,j2=p2[0],p2[1]

    map=salle(map,i1,j1,i2,j2)

    rd_direction=rd.randint(0,1)
    if rd_direction == 0:
        direction='h'
    else:
        direction='v'

    if direction=='h':
        other_dir='v'
        pos_door=(i2,rd.randint(j1+1,j2-1))
        pos_couloir_1=(rd.randint(i2+1,l-3),pos_door[1]+1)
        pos_couloir_2=(pos_couloir_1[0],rd.randint(pos_couloir_1[1],w-3))
        pos_door_2=(pos_couloir_2[0],pos_couloir_2[1]+1)
        if pos_door_2[1]>j2+1:
            pos_salle1=(rd.randint(0,l-3),pos_door_2[1])
        else:
            pos_salle1=(rd.randint(p2[0]+2,l-3),pos_door_2[1])
        pos_salle2=(rd.randint(max([pos_salle1[0]+2,pos_couloir_2[0]+1]),l-1),rd.randint(pos_salle1[1]+2,w-1))
    elif direction=='v':
        other_dir='h'
        pos_door=(rd.randint(i1+1,i2-1),j2)
        pos_couloir_1=(pos_door[0]+1,rd.randint(j2+1,w-3))
        pos_couloir_2=(rd.randint(pos_couloir_1[0],l-3),pos_couloir_1[1])
        pos_door_2=(pos_couloir_2[0]+1,pos_couloir_2[1])
        if pos_door_2[0]>i2+1:
            pos_salle1=(pos_door_2[0],rd.randint(0,w-3))
        else:
            pos_salle1=(pos_door_2[0],rd.randint(j2+2,w-3))
        pos_salle2=(rd.randint(pos_salle1[0]+2,l-1),rd.randint(max([pos_salle1[1]+2,pos_couloir_2[1]+1]),w-1))

    map=porte(map,pos_door[0],pos_door[1])
    if direction=='h':
        map=couloir(map,pos_door[0]+1,pos_door[1],pos_couloir_1[0],pos_couloir_1[1],other_dir)
        map=couloir(map,pos_couloir_1[0],pos_couloir_1[1],pos_couloir_2[0],pos_couloir_2[1],direction)
    else:
        map=couloir(map,pos_door[0],pos_door[1]+1,pos_couloir_1[0],pos_couloir_1[1],other_dir)
        map=couloir(map,pos_couloir_1[0],pos_couloir_1[1],pos_couloir_2[0],pos_couloir_2[1],direction)

    map=salle(map,pos_salle1[0],pos_salle1[1],pos_salle2[0],pos_salle2[1])
    map=porte(map,pos_door_2[0],pos_door_2[1])

    return map

map_random=(random_arena(30,30))


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

print(print_bg(map_random))

TYPES = {'_' : 'wall', ' ': 'wall', '|' : 'wall', '.' : 'room', '#' : 'corridor', '+' : 'door', '=' : 'staircase', '*' : 'gold',
         'j' : 'potion', "!" : "sword", ")" : "bow", "K" : "enemy"}



def move (key, joueur):
    x,y = joueur.coord_x, joueur.coord_y
    next_position = x,y
    if key == 'gauche' :
        next_position = x, y - 1
    if key == 'droite' :
        next_position = x, y + 1
    if key == 'haut' :
        next_position = x - 1, y
    if key == 'bas' :
        next_position = x + 1, y
    return(next_position)

def valid_move(key, joueur, map):
    next_move = move(key, joueur)
    next_type = TYPES[map[next_move[0]][next_move[1]]]
    if next_type != "wall" :
        return True

def event(key, joueur, map, original_map, Monstres):
    if key == 'space' :
        sac_ouvert = not sac_ouvert
        # A FAIRE: afficher le sac ou la carte
    
    if key in ['gauche', 'droite', 'haut', 'bas'] :
        if valid_move(key, joueur, map):
            ancien_x, ancien_y = joueur.coord_x, joueur.coord_y
            ancien_symbole = original_map[ancien_x][ancien_y]
            symbol = map[move(key, joueur)[0]][move(key, joueur)[1]]
            next_type = TYPES[symbol]
            if next_type != "enemy" :
                joueur.move(move(key, joueur))
                ancien_type = TYPES[ancien_symbole]
                if ancien_type in ("corridor", "door", "staircase"):
                    map[ancien_x][ancien_y] = ancien_symbole # On remet le point de départ à sa valeur initiale
                else:
                    map[ancien_x][ancien_y] = "."
                map[joueur.coord_x][joueur.coord_y] = "@"
            else :
                Monstres[(move(key, joueur))].hit(joueur.degats, joueur)


def main():
    map = arena(30,30)
    original_map = copy.deepcopy(map)
    monstre1 = Enemy(5, 5, 10, [Objets.armure_de_cristal], 0)
    monstre2 = Enemy(15, 15, 10, [], 0)
    Monstres = {(15,15) : monstre2, (5,5) : monstre1}
    sac = Sac()
    joueur = Joueur(27, 5, sac)
    map[joueur.coord_x][joueur.coord_y] = "@"
    for monstre in Monstres :
        x, y = monstre
        map[x][y] = 'K'
    sac_ouvert = False
    WAIT = True
    print_bg(map)

    while WAIT :
        # Wait for the next event.
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN :
            key = key.name

        event(key, joueur, map, original_map, Monstres)
        

        
        os.system("cls")
        print_bg(map)


main()