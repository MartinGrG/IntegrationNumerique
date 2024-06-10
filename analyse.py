from timeit import timeit
from calculs import integrale_analytique


def analyse(nom_fct, P, a, b, nbre_seg):
    time = timeit(lambda: nom_fct(P, a, b, nbre_seg), number=1)
    resultat = nom_fct(P, a, b, nbre_seg)[0]
    erreur = ((nom_fct(P, a, b, nbre_seg)[0] - integrale_analytique(P, a ,b))/integrale_analytique(P, a, b))*100

    return time, resultat, erreur



def compare(nom_fct1, nom_fct2, P, a, b):

    tableau_compare = [[],[]]
    tableau_compare[0].append(nom_fct1)
    tableau_compare[1].append(nom_fct2)

    for i in range(11):
        tableau_compare[0].append(analyse(nom_fct1, P, a, b, int((b-a)*(i+1))))
        tableau_compare[1].append(analyse(nom_fct2, P, a, b, int((b-a)*(i+1))))


    return tableau_compare