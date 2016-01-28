# #  coding=utf-8
__author__ = 'Jonathan Jackson'
#
#Fichier3 colgraph.py
#08 octobre 2015
#Montréal, QC, Canada
#
#  Programme pouvant créer des matrices 3 coloriables et contenant aussi un
# algorithme pour les colorier en temps polynomial
#
# L'algorithme fonctionne de la facon suivante:
# -On fait appel a la fonction principale color(matrix, ncol) qui démarera
#   le coloriage de la matrice donnée en argument.
# -On prend le sommet 0 de la matrice (arbitrairement)
# -On assigne les 3 couleurs possibles en étiquette (correspondant a nbcol) a tous les sommets
#     du graphe a la position [i][i] pour un sommet i
# -On itère k fois de telle façon(où k est le nombre de sommets de "matrix"):
#     -On assigne avec la fonction "assignColFromSet(matrix, i)" au sommet "i"
#         la couleur qui a la première position dans son étiquette
#     -Pour tous ses voisins on retire avec la fonction"restrictCol(matrix, i)"
#         la couleur de "i" de leurs possibles couleurs. Cette fonction fait appel
#         a la fonction "removeCol(matrix, i, j)" qui elle retire la couleur de l'étiquette
#         d'un sommet voisin s'il a plusieurs couleures possible et laisse la couleur du sommet
#         voisin intact sinon (on vérifie toujours tous les voisins
#             des sommets, ce sinon est donc important)
#     -On actualise la variable "i" pour qu'on choisisse un des sommets du graphe ayant le moins
#     de couleurs dans son étiquette avec la fonction selectSommet(matrix)
#
# A la fin de ce coloriage, on peut vérifier avec printMatrix(matrix) et
# verifyCol(matrix) si le coloriage est bon.
#
# printMatrix(matrix) affiche sur la console la liste de liste sous forme de
#   matrice en imprimant chaque ligne séparément.

# verifyCol(matrix) regardera, pour chaque sommet i, pour toutes positions sur
#   sa ligne ou il y a des "1" (connexions avec d'autres sommets j) si le sommet
#   auquel il est connecté a la même couleur que lui. Un message est imprimé en
#   conséquence
#
#fillmat3col(matrix) prend une matrice vide et la remplie avec des sommets
#   coloriés de facon a ce que la matrice soit 3 coloriable:
#   On ajoute chaque sommets avec leur couleurs et on les connecte
#   seulement avec des sommets existants de couleur différente. On
#   suppose que tous les graphes 3-coloriables peuvent être batis
#   de la sorte.
#
#On suppose aussi que le squelette de ce graphe permettra a
#   l'algorithme représenté par la fonction color(matrix, nbcol)
#   de tricolorier le graphe sans ne jamais échouer
#
#Au bas de ce programme réside l'appel de fonction permettant de créer
#   une matrice vide, de la connecter de facon tricoloriable, de la décolorier
#   et de la recolorier avec l'algorithme color(matrix, nbcolor)
#
#En théorie cet algorithme fonctionne pour tout nombre de couleur inférieur
#   ou égal a la chromaticité du graphe


import random


# fonction créant une matrice remplie de "0"
def createMat(nbVertices):
    matrix = list(list(0 for j in range(0, nbVertices, 1)) for j in range(0, nbVertices, 1))
    return matrix

# fonction assignant une couleur (2, 3 ou 4) a un sommet a la position (i,i) d'une amtrice
def assigncol(matrix, i):
    matrix[i][i] = random.randint(2, 4)

# fonction connectant deux sommets au hasard s'ils n'ont pas la meme couleur
def connect(matrix, i):
    for j in range(0, len(matrix), 1):
        if i == j: continue
        if matrix[j][j] == 0: continue  # le sommet n'existe pas et ne peux avoir aucune connexion
        if matrix[i][i] == matrix[j][j]: continue  # le sommet i a la meme couleure que j
        matrix[i][j] = random.randint(0, 1)
        if matrix[i][j] == 1: matrix[j][i] = 1

# fonction remplissant une matrice vide avec des sommets de sorte a créer une matrice 3col
def fillmat3col(matrix):
    for i in range(0, len(matrix), 1):
        assigncol(matrix, i)
        connect(matrix, i)

# print la liste "matrix" en format de matrice
def printMatrix(matrix):
    for i in range(0, len(matrix), 1):
        print(matrix[i])

# fonction vérifiant que le coloriage de la matrice est acceptable
def verifyCol(matrix):
    sameCol = True
    for i in range(0, len(matrix), 1):  # pour tous sommets i de "matrix"
        for j in range(0, len(matrix), 1):  # pour tous les sommets j connectés a i
            if matrix[i][j] == 1:  # s'ils sont connectes
                if matrix[i][i] == matrix[j][j]:  # S'ils ont la meme couleur
                    print(str(i) + " a la même couleur que " + str(j))
                    sameCol = False  # ne retournera pas le messsage qu'aucun sommet
                    break
    if sameCol == True: print("Aucun sommet connecte n'a la meme couleur")

# décolore une matrice
def uncolor(matrix):
    for i in range(0, len(matrix), 1):
        matrix[i][i] = 0

# fonction enlevant la couleur Ci de i a son voisin j
def removeCol(matrix, i, j):
    colori = matrix[i][i]
    if isinstance(matrix[j][j], int): return
    if colori in matrix[j][j]:
        matrix[j][j].remove(colori)

# fonction retournant le prochain sommet a sonder en favorisant ceux avec moins de couleurs
def selectSommet(matrix):
    for i in range(0, len(matrix), 1):  # une seule couleur
        if isinstance(matrix[i][i], int): continue  # si couleur deja assignée
        if len(matrix[i][i]) == 1:
            return i

    for i in range(0, len(matrix), 1):  # deux couleurs
        if isinstance(matrix[i][i], int):
            continue  # si couleur deja assignée
        elif len(matrix[i][i]) == 2:
            return i

    for i in range(0, len(matrix), 1):  # trois couleurs
        if isinstance(matrix[i][i], int):
            continue  # si couleur deja assignée
        elif len(matrix[i][i]) == 3:
            return i

# fonction réduisant les couleurs possibles pour tous les voisins de i
def restrictCol(matrix, i):
    for j in range(0, len(matrix), 1):  # pour tous les sommets
        if matrix[i][j] == 1:  # s'ils sont voisins
            removeCol(matrix, i, j)  # on enleve la couleur de i a j


# fonction donnant toutes les couleures possibles aux sommets d'une
# matrice selon le nombre de couleures allouees
def giveAllCol(matrix, nbcol):
    for i in range(0, len(matrix), 1):
        matrix[i][i] = list(range(2, nbcol + 2, 1))  # couleurs de 2 a nbcol+2 (1 et 0 réservés)

# fonction prenant la premiere couleur de l'ensemble des couleurs disponibles
# pour un sommet et lui assigne cette couleur
def assignColFromSet(matrix, i):
    matrix[i][i] = matrix[i][i][0]

# fonction composite prenant une matrice et un nombre de couleurs et tente
# de colorier cette matrice
def color(matrix, nbcol):
    i = 0  # On prend le premier sommet de matrix pour ittération 1
    giveAllCol(matrix, nbcol)  # on donne toutes les couleures possibles au sommets

    for k in range(0, len(matrix), 1):  # On effectue cette procédure une fois pour tout sommet
        assignColFromSet(matrix, i)  # on assigne une couleur au sommet selon celles dispo
        restrictCol(matrix, i)  # on restreint ses voisins
        i = selectSommet(matrix)



### Test des fonctions codées ci-haut

matricePierree = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matricePierre = [[0, 1, 0, 1, 0, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 1, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 0 ,1 ,0 ,0],
                 [0, 0, 1, 1, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 0, 1, 0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 1, 0, 0, 1, 0]]

#printMatrix(matricePierre)

#essai1 = createMat(10)             # creer une matrice vide (MODIFIER NOMBRE SOMMETS AU BESOIN)
# fillmat3col(essai1)                # remplissage de la matrice de facon tricoloriable
# printMatrix(essai1)                # visualisation du résultat
#
#
# uncolor(essai1)                          # enlever les couleurs de la matrice(diagonale)
print("                           ")
#
printMatrix(matricePierre)                 #visualisation du résultat décoloré
color(matricePierre, 3)                    #coloration de la matrice vide
#
print("                           ")

printMatrix(matricePierre)                 #visualisation du résultat sur la console
#
verifyCol(matricePierre)           #vérification qu'aucun sommet connecté n'a la même couleur
                                    #   que ses voisins

