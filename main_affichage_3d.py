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

# Créez une figure et un subplot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cette procedure permet de créer les vecteurs X et Y pour le tracé
def affichage_convergence_base(nom):
    comparaison = compare(methode_simpson_python, nom, coef, a, b)
    methode_tps = comparaison[0][1, 0, :]
    methode_erreur = comparaison[0][1, 2, :]
    liste_nbre_seg = comparaison[1]

    # Tracez les points
    ax.plot(liste_nbre_seg, methode_tps, methode_erreur, marker='.', label={nom.__name__})

    # Ajoutez des étiquettes aux axes
    ax.set_xlabel('Nombre de segments')
    ax.set_ylabel('Temps de calcul [sec]')
    ax.set_zlabel('Erreur relative [%]')
    ax.set_title("Tracé 3D de mettant en relation\nle nombre de segments, "
                 "le temps de calcul et l'erreur relative\npour les 3 méthodes en python")
    # Affichez le graphique

# Cette procédure permet d'afficher les tracés sur le même graphe.
def trace(nom):

    if nom =="python":
        affichage_convergence_base(methode_trapezes_python)
        affichage_convergence_base(methode_rectangle_python)
        affichage_convergence_base(methode_simpson_python)
        plt.legend()
        plt.show()
    elif nom == "numpy":
        affichage_convergence_base(methode_trapezes_numpy)
        affichage_convergence_base(methode_rectangle_numpy)
        affichage_convergence_base(methode_simpson_numpy)
        plt.legend()
        plt.show()
    else:
        affichage_convergence_base(methode_trapezes_existante)
        affichage_convergence_base(methode_simpson_existante)
        plt.legend()
        plt.show()

trace("python")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
trace("numpy")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
trace("existante")
