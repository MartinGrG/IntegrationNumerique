# -------------------------------------------------------------------------- #
               #SCRIPT REALISANT LES INTEGRATIONS NUMERIQUE
        # AVEC LES METHODES DES TRAPEZES (PYTHON ET NUMPY VERSION)#
# -------------------------------------------------------------------------- #
# MGA-802

# Ce script est composé de deux fonctions. L'une évalue un polynome de 3eme
# degré en une valeur imposée et l'autre calcule l'intégrale entre a et b.


def evaluation(P, value):
    return P[0]+P[1]*value+P[2]*value**2+P[3]*value**3

def integrale_analytique(P, a, b):
    integrale = (P[0]*b+P[1]*(b**2)/2+P[2]*(b**3)/3+P[3]*(b**4)/4)-(P[0]*a+P[1]*(a**2)/2+P[2]*(a**3)/3+P[3]*(a**4)/4)
    return integrale