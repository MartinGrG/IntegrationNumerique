"""Ce script permet d'afficher le temps de calcul et l'erreur relative sur un graphique
pour chaque fonction de calcul d'intégrale"""

import matplotlib.pyplot as plt
from analyse import *
from methode_rectangles import *
from methode_trapezes import *
from methode_simpson import *

from calculs import *


# Définition des paramètres : a et b les bornes de l'intervalle a < b,
# liste_coefficient : la liste des coefficients du polynôme de degrés 3
a = 0
b = 100
coef = [1,-200,-300,4]
# Liste des différents découpages de l'intervalle,
# à ne pas modifier sauf s'il est modifié dans analyse.py dans la fonction compare
liste_nbre_seg = [i*(b-a) for i in range(1,11)]


# TEMPS DE CALCUL
# Tracé temps de calcul de chaque méthode
# RECTANGLES
def tracer_tps_calcul_rectangles():
    rect_base_tps = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)[0][0, 0, :]
    rect_numpy_tps = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)[0][1, 0, :]
    plt.plot(liste_nbre_seg, rect_base_tps, 'r-', label='Méthode des rectangles de base')
    plt.plot(liste_nbre_seg, rect_numpy_tps, 'r--', label='Méthode des rectangles Numpy')
    plt.title('RECTANGLES : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul')
    plt.legend()
    # Affichage du graphique
    plt.show()


# TRAPÈZES
def tracer_tps_calcul_trapezes():
    trap_base_tps = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)[0][0, 0, :]
    trap_numpy_tps = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)[0][1, 0, :]
    trap_existante_tps = compare(methode_trapezes_existante, methode_trapezes_numpy, coef, a, b)[0][0, 0, :]
    plt.plot(liste_nbre_seg, trap_base_tps, 'b-', label='Méthode des trapèzes de base')
    plt.plot(liste_nbre_seg, trap_numpy_tps, 'b--', label='Méthode des trapèzes Numpy')
    plt.plot(liste_nbre_seg, trap_existante_tps, 'b-.', label='Méthode des trapèzes existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('TRAPÈZES : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul')
    plt.legend()
    # Affichage du graphique
    plt.show()


# SIMPSON
def tracer_tps_calcul_simpson():
    simp_base_tps = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)[0][0, 0, :]
    simp_numpy_tps = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)[0][1, 0, :]
    simp_existante_tps = compare(methode_simpson_existante, methode_simpson_numpy, coef, a, b)[0][0, 0, :]
    plt.plot(liste_nbre_seg, simp_base_tps, 'g-', label='Méthode Simpson de base')
    plt.plot(liste_nbre_seg, simp_numpy_tps, 'g--', label='Méthode Simpson Numpy')
    plt.plot(liste_nbre_seg, simp_existante_tps, 'g-.', label='Méthode Simpson existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('SIMPSON : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul')
    plt.ylim(0, 0.002)
    plt.legend()
    # Affichage du graphique
    plt.show()


# ERREURS RELATIVES
# Tracé de l'erreur de chaque méthode
# RECTANGLES
def tracer_err_rectangle():
    rect_base_err= compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)[0][0, 2, :]
    rect_numpy_err = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)[0][1, 2, :]
    plt.plot(liste_nbre_seg, rect_base_err, 'r-', label='Méthode des rectangles de base')
    plt.plot(liste_nbre_seg, rect_numpy_err, 'r--', label='Méthode des rectangles Numpy')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('RECTANGLES : Tracé des erreurs relatives en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative')
    plt.legend()
    # Affichage du graphique
    plt.show()


# TRAPÈZES
def tracer_err_trapeze():
    trap_base_err = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)[0][0, 2, :]
    trap_numpy_err = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)[0][1, 2, :]
    trap_existante_err = compare(methode_trapezes_existante, methode_trapezes_numpy, coef, a, b)[0][0, 2, :]
    plt.plot(liste_nbre_seg, trap_base_err, 'b-', label='Méthode des trapèzes de base')
    plt.plot(liste_nbre_seg, trap_numpy_err, 'b--', label='Méthode des trapèzes Numpy')
    plt.plot(liste_nbre_seg, trap_existante_err, 'b-.', label='Méthode des trapèzes existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('TRAPÈZES : Tracé des erreurs relatives en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative')
    plt.legend()
    # Affichage du graphique
    plt.show()


# SIMPSON
def tracer_err_simpson():
    simp_base_err = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)[0][0, 2, :]
    simp_numpy_err = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)[0][1, 2, :]
    simp_existante_err = compare(methode_simpson_existante, methode_simpson_numpy, coef, a, b)[0][0, 2, :]
    plt.plot(liste_nbre_seg, simp_base_err, 'g-', label='Méthode Simpson de base')
    plt.plot(liste_nbre_seg, simp_numpy_err, 'g--', label='Méthode Simpson Numpy')
    plt.plot(liste_nbre_seg, simp_existante_err, 'g-.', label='Méthode Simpson existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('SIMPSON : Tracé des erreurs relatives en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative')
    plt.legend()
    # Affichage du graphique
    plt.show()


tracer_tps_calcul_rectangles()
tracer_tps_calcul_trapezes()
tracer_tps_calcul_simpson()
tracer_err_rectangle()
tracer_err_trapeze()
tracer_err_simpson()

# print(methode_trapezes_existante(coef, a, b, 100))
# print(methode_simpson_existante(coef, a, b, 100))
# print(integrale_analytique(coef, a, b))

