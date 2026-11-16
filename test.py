def choice01():
    
    print("a")
    print("b")
    print("c")
    print("d")
    choix = input("quel choix est ce que tu choisis ?: ")
    if choix == "a" or choix == "b" or choix == "c":
        print("faux")
    elif choix == "d":
        print("vrai")
    else:
        print("réponse invalide")

choice01()