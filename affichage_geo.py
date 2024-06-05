# -------------------------------------------------------------------------- #
               #SCRIPT REALISANT L'AFFICHAGE DES DIFFERENTES METHODES
# -------------------------------------------------------------------------- #
# MGA-802


# -------------------------------------------------------------------------- #
                              #IMPORTATION#
# -------------------------------------------------------------------------- #
import matplotlib.pyplot as plt
from methode_rectangles import *
from calculs import evaluation

# -------------------------------------------------------------------------- #
                              #FONCTIONS#
# -------------------------------------------------------------------------- #
liste = [1,2,3,4]
a = 0
b = 10
n = 10
x = np.linspace(a, b, n + 1)

#Plot de la focntion analytique
y_analytique = evaluation(liste, x)
plt.plot(x,y_analytique)

#Affichage de la méthode des rectangles

y_rectangle = methode_rectangle_numpy(liste, a, b, n)[1]






