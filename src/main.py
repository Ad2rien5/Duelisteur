from Chevalier import Chevalier
from Jeux import *

def Main():
    nb_joueur = int(input("Combien de joueur voulez vous? "))

    #initialisation
    joueurs = initialisation(nb_joueur)

    #jeux
    manche = 0

    while len(joueurs) > 1:
        manche += 1
        print(f"\n  Manche {manche}  ")

        joueurs = duel(joueurs)
    
    #fin
    print(f"Le vainqueur est : ")
    joueurs[0].statistique()


Main()
