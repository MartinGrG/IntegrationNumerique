# -------------------------------------------------------------------------- #
#SCRIPT REALISANT L'AFFICHAGE DES DIFFERENTES METHODES
# -------------------------------------------------------------------------- #
# MGA-802


# -------------------------------------------------------------------------- #
#IMPORTATION#
# -------------------------------------------------------------------------- #
import matplotlib.pyplot as plt
import numpy as np
from methode_rectangles import methode_rectangle_numpy
from calculs import evaluation

# -------------------------------------------------------------------------- #
#FONCTIONS#
# -------------------------------------------------------------------------- #
liste = [1, 2, 3, 4]
a = 0
b = 10
n = 4


def affichage_rectangle(liste, a, b, n):  # Affichage de la méthode des rectangles
    x_rectangle1 = np.linspace(a, b, n + 1)

    y_rectangle = methode_rectangle_numpy(liste, a, b, n)[1]
    pas = b - a / n

    y_rectangle2 = np.zeros(2 * (n + 1))
    y_rectangle2[0] = 0
    x_rectangle = np.zeros(2 * (n + 1))

    m = 0
    for l in range(0, 2 * (n + 1), 2):
        x_rectangle[l] = x_rectangle1[m]
        x_rectangle[l + 1] = x_rectangle1[m]
        m += 1

    j = 0
    for i in range(0, 2 * n, 2):
        y_rectangle2[i + 1] = y_rectangle[j]
        y_rectangle2[i + 2] = y_rectangle[j]
        j += 1

    plt.plot(x_rectangle, y_rectangle2, color='orange')
    plt.fill_between(x_rectangle, y_rectangle2, 0, color='orange', alpha=0.3)

    x_segment = x_rectangle[2::]
    y_segment = y_rectangle2[2::]
    plt.vlines(x_segment, 0, y_segment, colors='orange', linewidth=1)

    # Plot fonction analytique
    x = np.linspace(a, b, 1000)
    y_analytique = evaluation(liste, x)
    plt.plot(x, y_analytique)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Intégration par la méthode des rectangles')
    plt.legend()
    plt.grid(True)
    plt.show()

    return 0

def affichage_trapeze(liste, a, b, n):
    x_trapeze = np.linspace(a, b, n + 1)
    y_trapeze = evaluation(liste, x_trapeze)

    plt.plot(x_trapeze, y_trapeze, color='orange')
    plt.fill_between(x_trapeze, y_trapeze, 0, color='orange', alpha=0.3)
    plt.vlines(x_trapeze, 0, y_trapeze, colors='orange', linewidth=1)

    plt.scatter(x_trapeze, y_trapeze, color='red', s=15)

    # Plot fonction analytique
    x_analytique = np.linspace(a, b, 1000)
    y_analytique = evaluation(liste, x_analytique)
    plt.plot(x_analytique, y_analytique)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Intégration par la méthode des Trapèzes')
    plt.legend()
    plt.grid(True)
    plt.show()

    return 0


def affichage_simpson(liste, a, b, n):
    if n % 2 != 0:
        print("Le nombre de sous-intervalles n doit être pair.")
        return 12

    x_simpson = []
    y_simpson = []

    x = np.linspace(a, b, n + 1)
    y = evaluation(liste, x)

    # Points pour la courbe analytique
    x_analytique = np.linspace(a, b, 1000)
    y_analytique = evaluation(liste, x_analytique)

    # Tracer la courbe analytique
    plt.plot(x_analytique, y_analytique, label=f'f(x) = {liste[0]} + {liste[1]}x + {liste[2]}x^2 + {liste[3]}x^3', color= 'blue')

    # Tracer les segments parabolique de Simpson et colorier l'aire
    for i in range(0, n, 2):
        x_simpson2 = np.linspace(x[i], x[i + 2], 10)
        y_simpson2 = np.polyval(np.polyfit([x[i], x[i + 1], x[i + 2]], [y[i], y[i + 1], y[i + 2]], 2), x_simpson2)
        x_simpson.append(x_simpson2)
        y_simpson.append(y_simpson2)

    x_simpson = np.concatenate(x_simpson)
    y_simpson = np.concatenate(y_simpson)

    plt.plot(x_simpson, y_simpson, color='orange')
    plt.fill_between(x_simpson, 0, y_simpson, color='orange', alpha=0.3, label='Approximation de l\'aire' if i == 0 else "")

    # Ajouter des points
    plt.scatter(x, y, color='red', s=15)

    x_segment = x[::2]
    y_segment = y[::2]
    plt.vlines(x_segment, 0, y_segment, colors='orange', linewidth=1)

    # Configurer le graphique
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Intégration par la méthode de Simpson')
    plt.legend()
    plt.grid(True)
    plt.show()
    return 0


