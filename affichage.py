import matplotlib.pyplot as plt
import analyse
import methode_rectangles
import methode_trapezes
import methode_simpson

# Tracé temps de réponse de chaque méthode
a = 0
b = 10
liste_nbre_seg = [i*(b-a) for i in range(1,11)]
rect_base_tps = compare(methode_rectangle_python, a, b)
rect_numpy_tps = compare(methode_rectangle_numpy, a, b)
trap_base_tps = compare(methode_trapeze_python, a, b)
trap_numpy_tps = compare(methode_trapeze_numpy, a, b)
simp_base_tps = compare(methode_simpson_python, a, b)
simp_numpy_tps = compare(methode_simpson_numpy, a, b)

plt.plot(liste_nbre_seg, rect_base_tps, 'r-', label='Méthode des rectangles de base')
plt.plot(liste_nbre_seg, rect_numpy_tps, 'r--', label='Méthode des rectangles Numpy')
plt.plot(liste_nbre_seg, trap_base_tps, 'b-', label='Méthode des trapèzes de base')
plt.plot(liste_nbre_seg, trap_numpy_tps, 'b--', label='Méthode des trapèzes Numpy')
plt.plot(liste_nbre_seg, simp_base_tps, 'g-', label='Méthode Simpson de base')
plt.plot(liste_nbre_seg, simp_numpy_tps, 'g--', label='Méthode Simpson Numpy')

plt.title('Tracé du temps de réponse en fonction du nombre de segments')
plt.xlabel('Nombre de segments')
plt.ylabel('Temps de réponse')
plt.legend()

plt.show()


# Tracé erreur de chaque méthode
a = 0
b = 10
liste_nbre_seg = [i*(b-a) for i in range(1,11)]
rect_base_err = compare(methode_rectangle_python, a, b)
rect_numpy_err = compare(methode_rectangle_numpy, a, b)
trap_base_err = compare(methode_trapeze_python, a, b)
trap_numpy_err = compare(methode_trapeze_numpy, a, b)
simp_base_err = compare(methode_simpson_python, a, b)
simp_numpy_err = compare(methode_simpson_numpy, a, b)

plt.plot(liste_nbre_seg, rect_base_err, 'r-', label='Méthode des rectangles de base')
plt.plot(liste_nbre_seg, rect_nump_err, 'r--', label='Méthode des rectangles Numpy')
plt.plot(liste_nbre_seg, trap_base_err, 'b-', label='Méthode des trapèzes de base')
plt.plot(liste_nbre_seg, trap_numpy_err, 'b--', label='Méthode des trapèzes Numpy')
plt.plot(liste_nbre_seg, simp_base_err, 'g-', label='Méthode Simpson de base')
plt.plot(liste_nbre_seg, simp_numpy_err, 'g--', label='Méthode Simpson Numpy')

plt.title('Tracé des erreurs relatives en fonction du nombre de segments')
plt.xlabel('Nombre de segments')
plt.ylabel('Erreur relative')
plt.legend()

plt.show()


