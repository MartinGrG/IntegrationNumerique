"""
Ce script permet d'évaluer une intégrale en utilisant la méthode de Simpson
"""
import numpy as np
from calculs import *
import scipy as sp


def methode_simpson_python(p, a, b, nbre):
    """ Cette fonction calcule l'intégrale d'un polynôme du 3ème degrés dont les coefficients sont dans p,
     entre a et b, en découpant l'intervalle en n segments. Cette fonction n'utilise pas numpy """
    pas = (b-a)/nbre
    debut = a
    fin = a + pas
    somme = 0
    for i in range(nbre):
        somme += ((fin - debut)/6) * (evaluation(p, debut) + 4 * evaluation(p, (debut + fin)/2) + evaluation(p, fin))
        debut = fin
        fin = debut + pas
    return somme, 0


def methode_simpson_numpy(p, a, b, nbre):
    """ Cette fonction calcule l'intégrale d'un polynôme du 3ème degrés dont les coefficients sont dans p,
     entre a et b, en découpant l'intervalle en n segments. Cette fonction utilise numpy"""
    x = np.linspace(a, b, nbre + 1)
    x0 = x[0: len(x)-1]  # Liste des points de départ du calcul d'intégral
    x1 = x[1: len(x)]  # Liste des points de fin du calcul d'intégral
    integrale_segment = ((x1 - x0)/6) * (evaluation(p, x0) + 4 * evaluation(p, (x0 + x1)/2) + evaluation(p, x1))
    return np.sum(integrale_segment), 0


def methode_simpson_existante(p, a, b, nbre):
    x = np.linspace(a, b, nbre + 1)
    y = evaluation(p, x)
    return sp.integrate.simpson(y,x=x), 0
