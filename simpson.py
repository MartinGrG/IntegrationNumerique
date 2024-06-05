"""Ce script permet d'évaluer une intégrale en utilisant la méthode de Simpson"""
import numpy as np


def poly3(p,x):
    """ Cette fonction évalue le polynôme du 3ème degrés dont les coefficients sont dans la liste p, en x"""
    # Entrée : liste p = [p0, p1, p2, p3] les coefficients du polynôme et flottant x la valeur à évaluer
    # Sortie : flottant : la valeur du polynôme en x
    return p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3


def poly4(p,x):
    """ Cette fonction évalue le polynôme du 4ème degrés dont les coefficients sont dans la liste p, en x"""
    # Entrée : liste p = [p0, p1, p2, p3, p4] les coefficients du polynôme et flottant x la valeur à évaluer
    # Sortie : flottant : la valeur du polynôme en x
    return p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3 + p[4] * x**4


def int_poly3(p, a, b):
    """ Cette fonction calcule l'intégrale d'un polynôme du 3ème degrés entre a et b"""
    # Entrée : liste p = [p0, p1, p2, p3] les coefficients du polynôme et entiers : a < b
    # Sortie : flottant : la valeur du polynôme en x
    liste_coef = [0, p[0]/1, p[1]/2, p[2]/3, p[3]/4]
    return poly4(liste_coef, b) - poly4(liste_coef, a)


def methode_simpson_base(p, a, b, n):
    """ Cette fonction calcule l'intégrale d'un polynôme du 3ème degrés dont les coefficients sont dans p,
     entre a et b, en découpant l'intervalle en n segments. Cette fonction n'utilise pas numpy """
    pas = (b-a)/n
    debut = a
    fin = a + pas
    somme = 0
    for i in range(n):
        somme += ((fin - debut)/6) * (poly3(p, debut) + 4 * poly3(p, (debut + fin)/2) + poly3(p, fin))
        debut = fin
        fin = debut + pas
    return somme


def methode_simpson_numpy(p, a, b, n):
    """ Cette fonction calcule l'intégrale d'un polynôme du 3ème degrés dont les coefficients sont dans p,
     entre a et b, en découpant l'intervalle en n segments. Cette fonction utilise numpy"""
    x = np.linspace(a,b,n+1)
    x0 = x[0: len(x)-1]  # Liste des points de départ du calcul d'intégral
    x1 = x[1: len(x)]  # Liste des points de fin du calcul d'intégral
    integrale_segment = ((x1 - x0)/6) * (poly3(p, x0) + 4 * poly3(p, (x0 + x1)/2) + poly3(p, x1))
    return np.sum(integrale_segment)


coef = [1, 2, 3, 4]
debut = 0
fin = 10
nbre_seg = 10

print(f"Valeur calculée simpson de base : {methode_simpson_base(coef, debut, fin, nbre_seg)}")
print(f"Valeur calculée simpson de numpy : {methode_simpson_numpy(coef, debut,fin, nbre_seg)}")
print(f"Valeur réelle : {int_poly3(coef, debut, fin)}")
