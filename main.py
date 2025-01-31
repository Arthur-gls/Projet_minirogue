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