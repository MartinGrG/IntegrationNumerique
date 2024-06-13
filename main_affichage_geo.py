"""Script affichant la représentation graphique des méthode d'intégration: rectangle, trapèze et Simpson"""

import matplotlib.pyplot as plt
import numpy as np
from methode_rectangles import methode_rectangle_numpy
from calculs import  evaluation
def affichage_rectangle(liste, a, b, n):  # Affichage de la méthode des rectangles

    # Plot fonction analytique
    x_analytique = np.linspace(a, b, 1000)
    y_analytique = evaluation(liste, x_analytique)
    plt.plot(x_analytique, y_analytique, label=f'f(x) = {liste[0]} + {liste[1]}x + {liste[2]}x^2 + {liste[3]}x^3',
             color='blue')

    x_rectangle1 = np.linspace(a, b, n + 1)  # Liste des abscisses des points évalués
    y_rectangle = methode_rectangle_numpy(liste, a, b, n)[1]  # On récupère les ordonnées des point évalués et on les
    #                                                           stocks
    pas = b - a / n  # Calcul du pas

    # Création de listes plus grandes car l'affichage de des rectangles nécessite plus de points 2 fois plus + 2
    y_rectangle2 = np.zeros(2 * (n + 1))
    x_rectangle = np.zeros(2 * (n + 1))

    # Algorithme permettant de créer les coordonnées des points des rectangles
    # Liste des abscisses
    m = 0
    for l in range(0, 2 * (n + 1), 2):  # On stock 2 fois la même abscisse l'une à la suite de l'autre
        x_rectangle[l] = x_rectangle1[m]  # exemple [0,1,2,3] -> [0,0,1,1,2,2,3,3]
        x_rectangle[l + 1] = x_rectangle1[m]
        m += 1

    # Liste des ordonnées
    j = 0
    for i in range(0, 2 * n, 2):  # On stock 2 fois la même ordonnées l'une à la suite de l'autre mais la
        y_rectangle2[i + 1] = y_rectangle[j]  # premiere et la derniere valeur sont à 0
        y_rectangle2[i + 2] = y_rectangle[j]
        j += 1

    # Plot des rectangles et remplissage pour symboliser l'aire
    plt.plot(x_rectangle, y_rectangle2, color='orange')
    plt.fill_between(x_rectangle, y_rectangle2, 0, color='orange', alpha=0.3, label='Approximation de l\'aire')

    # Ajouter des points (ronds rouges) pour bien les voir
    plt.scatter(x_rectangle, y_rectangle2, color='red', s=10)

    # Ajouter des lignes verticales pour délimiter les segments
    x_segment = x_rectangle[2::]
    y_segment = y_rectangle2[2::]
    plt.vlines(x_segment, 0, y_segment, colors='orange', linewidth=1)

    # Caractérstiques du plot
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Intégration par la méthode des rectangles (n={n})')
    plt.legend()
    plt.grid(True)

    return plt


def affichage_trapeze(liste, a, b, n):
    # Plot fonction analytique
    x_analytique = np.linspace(a, b, 1000)
    y_analytique = evaluation(liste, x_analytique)
    plt.plot(x_analytique, y_analytique, label=f'f(x) = {liste[0]} + {liste[1]}x + {liste[2]}x^2 + {liste[3]}x^3',
             color='blue')

    # Calcul des coordonnées des trapèzes
    x_trapeze = np.linspace(a, b, n)  # Liste des abscisses des points évalués
    y_trapeze = evaluation(liste, x_trapeze)  # On évalue tout simplement les points

    # Plot des trapèzes et remplissage pour symboliser l'aire
    plt.plot(x_trapeze, y_trapeze, color='orange')
    plt.fill_between(x_trapeze, y_trapeze, 0, color='orange', alpha=0.3, label='Approximation de l\'aire')

    # Ajouter des points (ronds rouges) pour bien les voir
    plt.scatter(x_trapeze, y_trapeze, color='red', s=10)

    # Ajouter des lignes verticales pour délimiter les segments
    plt.vlines(x_trapeze, 0, y_trapeze, colors='orange', linewidth=1)

    # Caractérstiques du plot
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Intégration par la méthode des trapèzes (n={n})')
    plt.legend()
    plt.grid(True)

    return plt


def affichage_simpson(liste, a, b, n):
    # Test si le nombre de sous-intervalles est pair. Nécessaire pour la méthode employée
    if n % 2 != 0:
        print("Le nombre de sous-intervalles n doit être pair.")
        return 12

    # Tracer la courbe analytique
    x_analytique = np.linspace(a, b, 1000)
    y_analytique = evaluation(liste, x_analytique)
    plt.plot(x_analytique, y_analytique, label=f'f(x) = {liste[0]} + {liste[1]}x + {liste[2]}x^2 + {liste[3]}x^3',
             color='blue')

    # Initialisation des listes de coordonnées
    x_simpson = []
    y_simpson = []
    x = np.linspace(a, b, 2*n + 1)  # On ajoute des points afin d'avoir trois points sur un segment évalué
    y = evaluation(liste, x)

    # La méthode Simpson fait une approximation de la courbe sur un segment par une parabolle. Sur chaque segment
    # [a,b] on considère 3 points : a, a+b/2 et b par lesquels la parabole doit passer.
    for i in range(0, 2*n, 2):
        x_simpson2 = np.linspace(x[i], x[i + 2], 10)
        y_simpson2 = np.polyval(np.polyfit([x[i], x[i + 1], x[i + 2]], [y[i], y[i + 1], y[i + 2]], 2), x_simpson2)
        x_simpson.append(x_simpson2)
        y_simpson.append(y_simpson2)

    x_simpson = np.concatenate(x_simpson)
    y_simpson = np.concatenate(y_simpson)

    # Tracer les segments parabolique de Simpson et colorier l'aire
    plt.plot(x_simpson, y_simpson, color='orange')
    plt.fill_between(x_simpson, 0, y_simpson, color='orange', alpha=0.3, label='Approximation de l\'aire')

    # Ajouter des points (ronds rouges) pour bien les voir
    x_segment = x[::2]  # On en prend que un sur deux car un segment est est évalué sur 3 points: a, a+b/2, b
    y_segment = y[::2]  # on ne veut afficher que les points a et b qui délimitent le segment
    plt.scatter(x_segment, y_segment, color='red', s=10)

    # Ajouter des lignes verticales pour délimiter les segments
    plt.vlines(x_segment, 0, y_segment, colors='orange', linewidth=1)

    # Configurer le graphique
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Intégration par la méthode de Simpson (n={n})')
    plt.legend()
    plt.grid(True)
    plt.show()
    return plt
