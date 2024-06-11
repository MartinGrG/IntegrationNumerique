"""Ce script permet d'analyser les performances des fonctions d'intégration numérique"""

from timeit import timeit
import numpy as np
from calculs import integrale_analytique


# Cette fonction analyse une méthode d'intégration numérique et
# retourne les valeurs du temps de calcul, du résultat et de son
# erreur relative en comparaison à l'intégration analytique exacte.

# Entrées : - nom de la méthode
#           - liste des coefficients du polynome de 3ème degré
#           - bornes a et b
#           - nombre de
# Sorties :
#           - Temps de calcul
#           - valeur du résultat
#           - valeur de l'erreur relative sur le résultat
def analyse(nom_fct, P, a, b, nbre_seg):
    # Obtention du temps de calcul
    time = timeit(lambda: nom_fct(P, a, b, nbre_seg), number=500)/500
    # Obtention du résultat d'intégration numérique
    resultat = nom_fct(P, a, b, nbre_seg)[0]
    # Calcul de l'erreur relative à la valeur analytique
    erreur = ((nom_fct(P, a, b, nbre_seg)[0] - integrale_analytique(P, a, b)) / integrale_analytique(P, a, b)) * 100

    return time, resultat, erreur


# Cette fonction, met en forme les résultats de l'analyse de deux méthodes.
# La forme du tableau_compare de sorti est la suivante :

# tableau_compare[] --> permet de sélectionner les valeurs de la méthode 1 ou 2 [0 ou 1]

# tableau_compare[][] --> permet de sélectionner pour l'une des deux méthodes l'ensemble des temps [0],
# des résultats [1] ou encore des erreurs [2]

# tableau_compare[][][] --> permet d'obtenir pour l'une des deux méthodes, la valeur du temps, du résultat
# ou de l'erreur pour le premier nombre de segments [0], deuxieme nombre de segments [1] ...

# Le tableau_nombre_segment est un vecteur composé des nombres de segments liés à chaque triplet cité ci-dessus.
def compare(nom_fct1, nom_fct2, P, a, b):
    tableau_compare = np.zeros([2, 3, 10])
    tableau_nombre_segment = np.zeros(10)

    for i in range(1, 11):
        tableau_compare[0, :, i - 1] = (analyse(nom_fct1, P, a, b, int(((b - a) * i) / 10)))
        tableau_compare[1, :, i - 1] = (analyse(nom_fct2, P, a, b, int(((b - a) * i) / 10)))
        tableau_nombre_segment[i - 1] = int(((b - a) * i) / 10)

    return tableau_compare, tableau_nombre_segment