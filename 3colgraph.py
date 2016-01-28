#  coding=utf-8
__author__ = 'Winsis'
#
# Programme créant une matrice 3COL et la retournant sous forme de fichier CSV
#
#
#
#
#

import random
import types

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


#fonction remplissant une matrice vide avec des sommets de sorte a créer une matrice 3col
def fillmat3col(matrix):
    for i in range(0, len(matrix), 1):
        assigncol(matrix, i)
        connect(matrix, i)


#print la liste "matrix" en format de matrice
def printMatrix(matrix):
    for i in range(0, len(matrix), 1):
        print matrix[i]


#fonction vérifiant que le coloriage de la matrice est acceptable
def verifyCol(matrix):
    sameCol = True
    for i in range(0, len(matrix), 1):              #pour tous sommets i de "matrix"
        for j in range(0, len(matrix), 1):          #pour tous les sommets j connectés a i
            if matrix[i][j] == 1:                   #s'ils sont connectes
                if matrix[i][i] == matrix[j][j]:    #S'ils ont la meme couleur
                    print(i + " a la même couleur que " + j)
                    sameCol = False                 #ne retournera pas le messsage qu'aucun sommet
                    break
    if sameCol == True: print("Aucun sommet connecte n'a la meme couleur")


#décolore une matrice
def uncolor(matrix):
    for i in range(0, len(matrix), 1):
        matrix[i][i] = 0


#fonction enlevant la couleur Ci de i a son voisin j
def removeCol(matrix, i, j):
    colori = matrix[i][i]
    if isinstance(matrix[j][j], int): return
    if colori in matrix[j][j]:
        matrix[j][j].remove(colori)


#fonction retournant le prochain sommet a sonder en favorisant ceux avec moins de couleurs
def selectSommet(matrix):
    for i in range(0, len(matrix), 1):                  #une seule couleur
        if isinstance(matrix[i][i], int): continue      #si couleur deja assignée
        if len(matrix[i][i]) == 1:
            return i

    for i in range(0, len(matrix), 1):                  #deux couleurs
        if isinstance(matrix[i][i], int): continue      #si couleur deja assignée
        elif len(matrix[i][i]) == 2:
            return i

    for i in range(0, len(matrix), 1):                  #trois couleurs
        if isinstance(matrix[i][i], int): continue      #si couleur deja assignée
        elif len(matrix[i][i]) == 3:
            return i


#fonction réduisant les couleurs possibles pour tous les voisins de i
def restrictCol(matrix, i):
    for j in range(0, len(matrix), 1):      #pour tous les sommets
        if matrix[i][j] == 1:               #s'ils sont voisins
            removeCol(matrix, i, j)         #on enleve la couleur de i a j



#fonction donnant toutes les couleures possibles aux sommets d'une
#matrice selon le nombre de couleures allouees
def giveAllCol(matrix, nbcol):
    for i in range(0, len(matrix), 1):
        matrix[i][i] = range(2, nbcol+2, 1)     #couleurs de 2 a nbcol+2 (1 et 0 réservés)


def assignColFromSet(matrix, i):
    matrix[i][i] = matrix[i][i][0]


def color(matrix, nbcol):
    i = 0                                       #On prend le premier sommet de matrix pour ittération 1
    giveAllCol(matrix, nbcol)                   #on donne toutes les couleures possibles au sommets

    for k in range(0, len(matrix), 1):          #On effectue cette procédure une fois pour tout sommet
        assignColFromSet(matrix, i)             #on assigne une couleur au sommet selon celles dispo
        restrictCol(matrix, i)                  #on restreint ses voisins
        i = selectSommet(matrix)




essai1 = createMat(40)              #creer une matrice vide
fillmat3col(essai1)                #remplissage pour 3 coloriable
printMatrix(essai1)
print("                           ")
printMatrix(essai1)

color(essai1, 3)
print("                           ")
printMatrix(essai1)


# essai1 = {[2, 1, 1],[1, 2, 1],[1, 1, 2]}

verifyCol(essai1)



# couleurs = [1, 2 ,3]
# col1 = []
# col2 = []
# col3 = []
#
# matrix = []
#
#
#         coltemp = round(rand*3, 0)
#
#         if(coltemp == 1):
#             col1.append(i)
#             maxedges = len.col2 + len.col3
#             allowedset = col2 + col3
#         elif(coltemp == 2):
#             col2.append(i)
#             maxedges = len.col1 + len.col3
#             allowedset = col1 + col3
#         elif(coltemp == 3):
#             col3.append(i)
#             maxedges = len.col1 + len.col2
#             allowedset = col1 + col2
#
# ##################
#
#         tempsize = len(matrix[0])
#         rand = random.random()
#         nbedges = round(allowedset*rand)
#         chosenedges = []
#
# ## Shitty way of choosing a group of vertices
#         edgecount = nbedges
#         for j in range(0,len(nbedges),1):
#             rand = random.random()
#             edgeindex = round(nbedges*random, 0)
#             matrix[j].append(edgeindex)
