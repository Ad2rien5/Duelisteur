from random import *
from Chevalier import Chevalier

ALPHABET = "abcdefghijkmnlopqrstuvwxyz"

def create_soldier():
    #création du prénom du soldat
    taille = randint(3, 8)
    nom = ""
    for _ in range(taille):
        nom += choice(ALPHABET)

    return Chevalier(nom)

def initialisation(n):
    liste = []
    for _ in range(n):
        liste.append(create_soldier())
    return liste

def duel(liste):
    #sélection des duelistes
    chev1 = randint(0, len(liste)-1)
    chev2 = randint(0, len(liste)-1)
    while chev1 == chev2:
        chev2 = randint(0, len(liste)-1)

    liste[chev1].nb_duel += 1
    liste[chev2].nb_duel += 1
    
    #chev1 attaque
    liste[chev2].defense(liste[chev1].attaque())

    if liste[chev2].is_alive():
        #chev2 attaque
        liste[chev1].defense(liste[chev2].attaque())
        
        if not liste[chev1].is_alive():
            liste[chev2].got_kill()
            print(f"{liste.pop(chev1).nom} is dead!\n")
    else:
        liste[chev1].got_kill()
        print(f"{liste.pop(chev2).nom} is dead!\n")
    
    return liste
