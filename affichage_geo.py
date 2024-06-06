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
pas = b-a/n

y_rectangle2 = np.zeros(2*(n+1))
y_rectangle2[0] = 0
x_rectangle = np.zeros(2*(n+1))

m = 0
for l in range(0, 2*(n+1), 2):
    x_rectangle[l] = x[m]
    x_rectangle[l + 1] = x[m]
    m += 1

j = 0
for i in range(0, 2*n, 2):
    y_rectangle2[i+1] = y_rectangle[j]
    y_rectangle2[i+2] = y_rectangle[j]
    j += 1

plt.plot(x_rectangle,y_rectangle2)
plt.show()





