from random import randint

class Chevalier:
    def __init__(self, name):
        self.nom = name
        self.life = randint(15, 50)

        self.kill = 0
        self.nb_duel = 0
        
        self.liste_attaque = []
        self.crit = randint(0, 25)
        self.nb_crit = 0

        self.dodge = randint(0, 15)
        self.nb_dodge = 0

    def is_alive(self):
        return self.life > 0

    def attaque(self):
        damage = randint(0, 10)

        if randint(0, 100) <= self.crit:
            self.nb_crit += 1
            damage *= 2
        self.liste_attaque.append(damage)
        return damage

    def defense(self, damage):
        if randint(0, 100) > self.dodge:
            self.life -= damage
        else:
            self.nb_dodge += 1


    def got_kill(self):
        self.kill += 1

    def __dmg_moyen(self):
        total = 0
        for element in self.liste_attaque:
            total += element
        return total/len(self.liste_attaque)

    def statistique(self):
        print(self.nom)

        print()

        print(f"{self.life} points de vie restant")
        print(f"{self.nb_duel} duel participé\n")

        print(f"{sum(self.liste_attaque)} dégâts infligés")
        print(f"{self.__dmg_moyen()} dégât moyen")
        print(f"{self.nb_crit} attaques critiques\n")

        print(f"{self.nb_dodge} attaques esquivées\n")

        print(f"{self.crit} de taux de critiques")
        print(f"{self.dodge} de taux d'esquive")

