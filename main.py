# Collections : (Tableaux : Array), Listes, Tuples...
# Tupple (): C'est immutable, c'est à dire non modifiable
# Liste []: -> mutable, c'est à dire qu'elle est modifiable : on peut ajouter, supprimer des éléments ou les modifier


"""
personnes = ["Jean", "Marc", "Bob", "Arthur"]

# ------TUPPLE---------
# for i in range(0, len(personnes)):
#    print(personnes[i])

# for i in personnes:
#     print(i)
#     print(len(i))
#     print(i[0])

# fournit le dernier index du tableau -> c'est une  particularité propre à Python
# print(personnes[-1])

# -----LISTE-------
# tout ce qui est avant est valable mais on peut modifier les résultats :
# pour ajouter sur la liste :
# nouvelle_personne = "Jion"
# personnes.append(nouvelle_personne)
# pour supprimer une personne on met son indice avec del :
# del personne[1]

test = 5


def modifier_valeur(a):
    a[0] = "Josh"


print(personnes)
modifier_valeur(personnes)
print(personnes)
"""

# ---------- Fonction et Tuples----------


# def obtenir_info():
#     return "Mélanie", 1.8, 60
#
#
# def afficher_info(nom, taille, poids):
#     print(f"information de la personne nom : {nom}, taille: {taille}, poids: {poids}")
#
#
# info = obtenir_info()
#
#
# #afficher_info(*info)
# print(info)
#
# print(*info) # Quand on met l'étoile cela veut dire que l'on  : unpack tuple
#
# print(info[0], info[1], info[2])

# print("Nom : " + info[0])
# print("Taille : " + str(info[1]))
# print("Poids : " + str(info[2]))

# nom, taille, poids = obtenir_info()
# print(f"information de la personne nom : {nom}, taille: {taille}, poids: {poids}")


# ---------- Slices ----------
personnes = ("Jean", "Marc", "Bob", "Arthur", "Marie", "Josh")
#[start : stop : step]
for i in personnes[::]:
    print(i)

# nom = "marie"
# print(nom[::-1])
