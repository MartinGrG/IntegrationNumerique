from analyse import *
from methode_trapezes import *
from methode_rectangles import *
from methode_simpson import *



resultat_comp = compare(methode_trapezes_python, methode_trapezes_numpy, [1,2,3,4], 0 , 10)

print(resultat_comp[0][:,0])
print(resultat_comp[1][:,1])

