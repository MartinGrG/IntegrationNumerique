"""
Calcul d'intégrale par la méthode des rectangles
Rappel de la méthode des rectangles pour n éléments :
integrale = somme de n éléments de f((x(i)+x(i+1))/2)*(x(i+1)-x(i))
"""

import numpy as np
from calculs import evaluation


def methode_rectangle_python(p, a, b, nbre):
    pas = (b - a) / nbre  # Calcul du pas
    x = [a]  # Initialisation de la liste des abscisses
    y = []
    integrale = 0  # Initialisation de la valeur de l'intégrale
    for i in range(nbre):
        x.append(x[-1] + pas)  # Calcul de la liste des abscisses
        y.append(evaluation(p, (x[-2] + x[-1]) / 2) * (x[-1] - x[-2]))
        integrale = integrale + y[-1]  # Calcul de l'intégrale avec la méthode des rectangles
    return integrale, y


def methode_rectangle_numpy(p, a, b, nbre):
    x = np.linspace(a, b, nbre + 1)  # Création d'une liste de a à b avec n +1 éléments
    x1 = np.array([x[0:len(x) - 1], x[1:len(x)]])  # Création d'un tableau 1ere ligne: x sauf le dernier élément,
    # 2ème ligne: x sauf le premier élément
    x2 = np.array((x1[0, :] + x1[1, :]) / 2)  # Calcul de l'abscisse pour lequel on va évaluer chaque segment
    y = evaluation(p, x2)  # Evaluation du polynôme
    integrale = np.sum(y * (x1[1, :] - x1[0, :]))  # Calcul de l'intégrale par la méthode des rectangles
    return integrale, y



