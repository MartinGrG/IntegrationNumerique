# -------------------------------------------------------------------------- #
               #SCRIPT REALISANT LES INTEGRATIONS NUMERIQUE
        # AVEC LES METHODES DES TRAPEZES (PYTHON ET NUMPY VERSION)#
# -------------------------------------------------------------------------- #
# MGA-802

# Ce script est composé de deux fonctions. Elles réalisent toutes les deux
# une intégration numérique d'un polynome de 3eme degré donné entre a et b
# par la méthode des trapèzes. L'une est réalisée avec les outils Python de
# base et l'autre à l'aide de Numpy.


# -------------------------------------------------------------------------- #
                              #IMPORTATION#
# -------------------------------------------------------------------------- #

import numpy as np
from calculs import evaluation
# -------------------------------------------------------------------------- #
                              #FONCTIONS#
# -------------------------------------------------------------------------- #

def methode_trapezes_python(P, a, b, nbre):
    integrale = 0 # variable qui contiendra la valeur de l'intégrale

    x = []  # création du vecteur x contenant les abscisses avec le nombre de segments imposé
    for i in range(nbre+1):
        x.append(a+i*(b-a)/nbre)

    # On calcule l'aire de chacun des trapèzes et on les somme
    for i in range(len(x)-1):
        integrale += (x[i+1]-x[i])*((evaluation(P,x[i+1])+evaluation(P,x[i]))/2)

    return integrale, 0

def methode_trapezes_numpy(P, a, b, nbre):
    # vecteur x abscisses
    x = np.linspace(a, b, nbre+1)

    x1 = x[0:len(x)-1]  # vecteur des xi
    x2 = x[1:len(x)]    # vecteur des xi+1

    # On calcule simplement les trapèzes vectoriellement
    calcul = (x2-x1)*((evaluation(P,x2)+evaluation(P,x1))/2)

    # l'integrale est la somme du vecteur composé par chacune des aires
    integrale = np.sum(calcul)

    return integrale, 0
