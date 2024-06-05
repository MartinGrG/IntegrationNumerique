
from timeit import timeit

import numpy as np

from calculs import integrale_analytique


def analyse(nom_fct, P, a, b, nbre_seg):
    time = timeit(lambda: nom_fct(P, a, b, nbre_seg), number=1)
    resultat = nom_fct(P, a, b, nbre_seg)[0]
    erreur = ((nom_fct(P, a, b, nbre_seg)[0] - integrale_analytique(P, a ,b))/integrale_analytique(P, a, b))*100

    return time, resultat, erreur



def compare(nom_fct1, nom_fct2, P, a, b):

    tableau_compare = np.zeros([2,3,10])

    for i in range(1,11):
        tableau_compare[0,:,i].append(analyse(nom_fct1, P, a, b, int((b-a)*(i))))
        tableau_compare[1,:,i].append(analyse(nom_fct2, P, a, b, int((b-a)*(i))))


    return tableau_compare