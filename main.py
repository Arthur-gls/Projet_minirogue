
import time
import random as rd
import os 
import keyboard
import copy

WAIT = True

class Objets:
    arme_de_base = ["arme", "arme_de_base", "contact",1]
    épée = ["arme", "épée", "contact",2]
    hache = ["arme", "hache", "contact",3]
    lance = ["arme", "lance", "contact",4]
    baton = ["arme", "baton", "contact",1]
    dague = ["arme", "dague", "contact",6]
    arc = ["arme", "arc", "distance",2]
    arbalète = ["arme", "arbalète", "distance",3]
    fronde = ['arme', "fronde", "distance",1]
    marteau = ['arme', "marteau", "contact",5]

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
            self.potions[object[1]] += 1
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
        if self.points <= 0 :
            WAIT = False

class Enemy ():
    def __init__(self, x, y, pv, stuff, degats):
        self.coord_x = x
        self.coord_y = y
        self.points = pv
        self.stuff = stuff
        self.degats = degats
    def hit(self, points, joueur):
        self.points -= points
        print(self.points)
        





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
            pos_salle1=(rd.randint(0,pos_couloir_2[0]-1),pos_door_2[1])
        else:
            pos_salle1=(rd.randint(i2+1,pos_couloir_2[0]-1),pos_door_2[1])
        pos_salle2=(rd.randint(max([pos_salle1[0]+2,pos_couloir_2[0]+1]),l-1),rd.randint(pos_salle1[1]+2,w-1))
    elif direction=='v':
        other_dir='h'
        pos_door=(rd.randint(i1+1,i2-1),j2)
        pos_couloir_1=(pos_door[0]+1,rd.randint(j2+1,w-3))
        pos_couloir_2=(rd.randint(pos_couloir_1[0],l-3),pos_couloir_1[1])
        pos_door_2=(pos_couloir_2[0]+1,pos_couloir_2[1])
        if pos_door_2[0]>i2+1:
            pos_salle1=(pos_door_2[0],rd.randint(0,pos_couloir_2[1]-1))
        else:
            pos_salle1=(pos_door_2[0],rd.randint(j2+1,pos_couloir_2[1]-1))
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



def move(key, joueur):
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

def event(key, joueur, map, original_map, Monstres, sac_ouvert, sac):
    if key == 'space' :
        sac_ouvert = not sac_ouvert
        return sac_ouvert
    
    if not(sac_ouvert) :
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
                
                else:
                    monstre = Monstres[(move(key,joueur))]
                    monstre.hit(joueur.degats, joueur)
                    if monstre.points <= 0 :
                        map[monstre.coord_x][monstre.coord_y] = '.'
                        for objet in monstre.stuff :
                            joueur.sac.add_object(objet)
                            print(joueur.sac)

                for monstre in Monstres.values() :
                    if abs(joueur.coord_x - monstre.coord_x) <= 1 or abs(joueur.coord_y - monstre.coord_y) <= 1 :
                        joueur.hit(monstre.degats)
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz123456789"
        i = 0
        inventaire = {}
        for arme in sac.armes:
            inventaire[alphabet[i]] = arme
            i += 1
        for armure in sac.armures:
            inventaire[alphabet[i]] = armure
            i += 1
        for potion in sac.potions:
            if sac.potions[potion] > 0 :
                inventaire[alphabet[i]] = potion
                i += 1
        if key in inventaire:
            object = inventaire[key]
            if object[0] == 'arme' :
                joueur.arme_equipee = object
                joueur.degats = object[3]
            if object[0] == 'armure' :
                joueur.sac.protection -= joueur.sac.armures[object]
                joueur.sac.armures.remove(object)
            if object[0] == 'potion' :
                joueur.add_points(object[2])
                joueur.sac.use_potion(object)
    
    return sac_ouvert

def print_sac(sac):
    alphabet = "abcdefghijklmnopqrstuvwxyz123456789"
    print("Or : ", sac.gold)
    print("Protection : ", sac.protection)
    print("Armes : ")
    i = 0
    for arme in sac.armes:
        print(alphabet[i],") ",arme[1])
        i += 1
    print("Armures : ")
    for armure in sac.armures:
        print(alphabet[i],") ",armure)
        i += 1
    print("Potions : ")
    for potion in sac.potions:
        if sac.potions[potion] > 0 :
            print(alphabet[i],") ",potion, " : ", sac.potions[potion])
            i += 1

def main():
    map = arena(30,30)
    original_map = copy.deepcopy(map)
    monstre1 = Enemy(5, 5, 10, [Objets.armure_de_cristal], 0)
    monstre2 = Enemy(23, 27, 10, [], 0)
    Monstres = {(23,27) : monstre2, (5,5) : monstre1}
    sac = Sac()
    joueur = Joueur(27, 5, sac)
    sac.add_object(Objets.bouteille_eau)
    map[joueur.coord_x][joueur.coord_y] = "@"
    for monstre in Monstres :
        x, y = monstre
        map[x][y] = 'K'
    sac_ouvert = False
    print_bg(map)

    while WAIT :
        # Wait for the next event.
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN :
            key = key.name
        
        if key == "q":
            break

        sac_ouvert = event(key, joueur, map, original_map, Monstres, sac_ouvert, sac)
        

        
        os.system("cls")
        if sac_ouvert :
            print_sac(sac)
        else:
            print_bg(map)
    print("Tu es mort, espèce d'andouille ! Apprends à jouer au lieu de faire de la QSE... Guignol")


main()