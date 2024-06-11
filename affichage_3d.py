"""Ce code va permettre de tracer les graphiques 3D mettant en relation directe le temps de
calcul et l'erreur relative pour chaque méthode"""

from analyse import *
from methode_trapezes import *
from methode_rectangles import *
from methode_simpson import *
import matplotlib.pyplot as plt


a = 0
b = 100
coef = [1,-200,-300,4]
def affichage_convergence_base(nom):
    comparaison = compare(methode_simpson_python, nom, coef, a, b)
    methode_tps = comparaison[0][1, 0, :]
    methode_erreur = comparaison[0][1, 2, :]
    liste_nbre_seg = comparaison[1]

    # Créez une figure et un subplot 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Tracez les points
    ax.plot(liste_nbre_seg, methode_tps, methode_erreur, c='b', marker='.')

    # Ajoutez des étiquettes aux axes
    ax.set_xlabel('Nombre de segments')
    ax.set_ylabel('Temps de calcul [sec]')
    ax.set_zlabel('Erreur relative [%]')
    ax.set_title(f"Tracé 3D de mettant en relation\nle nombre de segments, "
                 f"le temps de calcul et l'erreur relative\npour la méthode {nom.__name__}")
    # Affichez le graphique
    plt.show()


affichage_convergence_base(methode_trapezes_python)
affichage_convergence_base(methode_rectangle_python)
affichage_convergence_base(methode_simpson_python)