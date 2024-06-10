import matplotlib.pyplot as plt
from analyse import *
from methode_rectangles import *
from methode_trapezes import *
from methode_simpson import *


a = 0
b = 10
coef = [1, 2, 3, 4]


def recuperer_tps(liste_compare):
    """Cette fonction permet d'extraire les temps de réponse du renvoi de la fonction compare
    pour les 2 fonctions comparées"""
    liste_tps_fct1 = []
    liste_tps_fct2 = []
    for i in range(1,len(liste_compare[0])):
        liste_tps_fct1.append(liste_compare[0][i][0])
        liste_tps_fct2.append(liste_compare[1][i][0])
    return liste_tps_fct1, liste_tps_fct2


def recuperer_err(liste_compare):
    """Cette fonction permet d'extraire les erreurs du renvoi de la fonction compare
        pour les 2 fonctions comparées"""
    liste_err_fct1 = []
    liste_err_fct2 = []
    for i in range(1, len(liste_compare[0])):
        liste_err_fct1.append(liste_compare[0][i][2])
        liste_err_fct2.append(liste_compare[1][i][2])
    return liste_err_fct1, liste_err_fct2


# Tracé temps de réponse de chaque méthode
liste_nbre_seg = [i*(b-a) for i in range(1,12)]
rect_base_tps, rect_numpy_tps = recuperer_tps(compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b))
trap_base_tps, trap_numpy_tps = recuperer_tps(compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b))
trap_existante_tps = recuperer_tps(compare(methode_trapezes_existante, methode_trapezes_numpy, coef, a, b))[0]
simp_base_tps, simp_numpy_tps = recuperer_tps(compare(methode_simpson_python, methode_simpson_numpy, coef, a, b))
simp_existante_tps = recuperer_tps(compare(methode_simpson_existante, methode_simpson_numpy, coef, a, b))[0]

plt.plot(liste_nbre_seg, rect_base_tps, 'r-', label='Méthode des rectangles de base')
plt.plot(liste_nbre_seg, rect_numpy_tps, 'r--', label='Méthode des rectangles Numpy')
plt.plot(liste_nbre_seg, trap_base_tps, 'b-', label='Méthode des trapèzes de base')
plt.plot(liste_nbre_seg, trap_numpy_tps, 'b--', label='Méthode des trapèzes Numpy')
plt.plot(liste_nbre_seg, trap_existante_tps, 'b-.', label='Méthode des trapèzes existante')
plt.plot(liste_nbre_seg, simp_base_tps, 'g-', label='Méthode Simpson de base')
plt.plot(liste_nbre_seg, simp_numpy_tps, 'g--', label='Méthode Simpson Numpy')
plt.plot(liste_nbre_seg, simp_existante_tps, 'g-.', label='Méthode Simpson existante')

plt.title('Tracé du temps de calcul en fonction du nombre de segments')
plt.xlabel('Nombre de segments')
plt.ylabel('Temps de réponse')
plt.legend()

plt.show()


# Tracé de l'erreur de chaque méthode
rect_base_err, rect_numpy_err = recuperer_err(compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b))
trap_base_err, trap_numpy_err = recuperer_err(compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b))
trap_existante_err = recuperer_err(compare(methode_trapezes_existante, methode_trapezes_numpy, coef, a, b))[0]
simp_base_err, simp_numpy_err = recuperer_err(compare(methode_simpson_python, methode_simpson_numpy, coef, a, b))
simp_existante_err = recuperer_err(compare(methode_simpson_existante, methode_simpson_numpy, coef, a, b))[0]

plt.plot(liste_nbre_seg, rect_base_err, 'r-', label='Méthode des rectangles de base')
plt.plot(liste_nbre_seg, rect_numpy_err, 'r--', label='Méthode des rectangles Numpy')
plt.plot(liste_nbre_seg, trap_base_err, 'b-', label='Méthode des trapèzes de base')
plt.plot(liste_nbre_seg, trap_numpy_err, 'b--', label='Méthode des trapèzes Numpy')
plt.plot(liste_nbre_seg, trap_existante_err, 'b-.', label='Méthode des trapèzes existante')
plt.plot(liste_nbre_seg, simp_base_err, 'g-', label='Méthode Simpson de base')
plt.plot(liste_nbre_seg, simp_numpy_err, 'g--', label='Méthode Simpson Numpy')
plt.plot(liste_nbre_seg, simp_existante_err, 'g-.', label='Méthode Simpson existante')

plt.title('Tracé des erreurs relatives en fonction du nombre de segments')
plt.xlabel('Nombre de segments')
plt.ylabel('Erreur relative')
plt.legend()

plt.show()


