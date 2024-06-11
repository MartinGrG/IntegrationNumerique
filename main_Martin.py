import matplotlib.pyplot as plt
from affichage_geo import *

P = [1,-200,300,4]
a = 0
b = 100
n1 = 10
n2 = 50
n3 = 200

#Méthode rectangle
affichage_rectangle(P,a,b,n1)
plt.show()
affichage_rectangle(P,a,b,n2)
plt.show()
affichage_rectangle(P,a,b,n3)
plt.show()

#Méthode trapeze
affichage_trapeze(P,a,b,n1)
plt.show()
affichage_trapeze(P,a,b,n2)
plt.show()
affichage_trapeze(P,a,b,n3)
plt.show()

#Méthode Simpson
affichage_simpson(P,a,b,n1)
plt.show()
affichage_simpson(P,a,b,n2)
plt.show()
affichage_simpson(P,a,b,n3)
plt.show()


