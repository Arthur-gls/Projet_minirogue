import time
import os 
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

class Joueur ():
    def __init__(self, x, y):
        self.coord_x = x
        self.coord_y = y
        self.points = 10
    def move(self, new_position):
        x, y = new_position
        self.coord_x = x
        self.coord_y = y
    def add_points(self, points):
        self.points += points
    def hit(self, points):
        self.points -= points

class Enemy ():
    def __init__(self, x, y, pv, stuff):
        self.coord_x = x
        self.coord_y = y
        self.points = pv
        self.stuff = stuff
    def hit(self, points):
        self.points -= points
        if self.points <= 0 :
            self.death()
    def death(self):
        for objet in stuff :
            #ajouter au sac
            pass



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
        for j in range(j1 + 1, j2):
            map[i1][j] = COULOIR
    elif direction == "v":
        for i in range(i1 + 1, i2):
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
    pass


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



TYPES = {'-' : 'wall', ' ': 'wall', '|' : 'wall', '.' : 'room', '#' : 'corridor', '+' : 'door', '=' : 'staircase', '*' : 'gold',
         'j' : 'potion', "!" : "sword", ")" : "bow", "K" : "enemy"}



def move (key, joueur):
    x,y = joueur.coord_x, joueur.coord_y
    next_position = x,y
    if key == 'gauche' :
        next_position = x - 1, y
    if key == 'droite' :
        next_position = x + 1, y
    if key == 'haut' :
        next_position = x, y - 1
    if key == 'bas' :
        next_position = x, y - 1
    return(next_position)

def valid_move(key, joueur, map):
    next_move = move(key, joueur)
    print(next_move)
    print(map[next_move[0]][next_move[1]])
    next_type = TYPES[map[next_move[0]][next_move[1]]]
    if next_type != "wall" :
        return True

def event(key, joueur, map):
    #print(key)
    print("a")
    if key == 'space' :
        sac_ouvert = not sac_ouvert
        # A FAIRE: afficher le sac ou la carte
    
    if key in ['gauche', 'droite', 'haut', 'bas'] :
        if valid_move(key, joueur, map) :
            ancien_x, ancien_y = joueur.coord_x, joueur.coord_y
            next_type = TYPES[map[move(key, joueur)[0]][move(key, joueur)[1]]]
            if next_type != "enemy" :
                joueur.move(move(key, joueur))
            map[ancien_x][ancien_y] = "." # On remet le point de départ à sa valeur initiale
            map[joueur.coord_x][joueur.coord_y] = "@"

def main():
    map = arena(30,30)
    sac = Sac()
    joueur = Joueur(27,5)
    map[joueur.coord_x][joueur.coord_y] = "@"
    sac_ouvert = False
    WAIT = True
    print_bg(map)

    while WAIT :
        # Wait for the next event.
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN :
            key = key.name

        event(key, joueur, map)
        

        
        os.system("cls")
        print_bg(map)


main()