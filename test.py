import random

#ensemble des questions

def choice01():
    print("À une intersection sans signalisation (pas de panneau, pas de feu), quelle règle générale s'applique ?")
    print("A) Priorité à gauche.")
    print("B) Priorité à droite.")
    print("C) Le véhicule le plus rapide passe en premier.")
    print("D) Le véhicule venant de la route la plus large a toujours priorité.")
    choix = input("quel choix est ce que tu choisis ?: ")
    if choix == "a" or choix == "d" or choix == "c":
        print("faux, Sauf indication contraire par une signalisation, vous devez céder le passage à tout véhicule venant de la droite.")
    elif choix == "b":
        print("vrai, Sauf indication contraire par une signalisation, vous devez céder le passage à tout véhicule venant de la droite.")
    else:
        print("réponse invalide")
        choice01()

def choice02():
    
    print("a1")
    print("b2")
    print("c3")
    print("d4")
    choix = input("quel choix est ce que tu choisis ?: ")
    if choix == "a1" or choix == "b2" or choix == "c3":
        print("faux")
    elif choix == "d4":
        print("vrai")
    else:
        print("réponse invalide")


#Le choix des questions

choix_possibles = [choice01,choice02]
question01 = random.choice(choix_possibles)
del choix_possibles[choix_possibles.index(question01)]
question02 = random.choice(choix_possibles)
del choix_possibles[choix_possibles.index(question02)]

#execution des questions

question01()
question02()