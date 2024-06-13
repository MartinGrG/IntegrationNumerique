# Objectif du code
Ce code a pour objectif d'implémenter d'une part à la main, avec les éléments de base fournit par python, les méthodes d'intégration numériques suivantes : la méthode des rectangles, la méthode des trapèzes, la méthode de Simpson. Dans un deuxième temps nous les implmenterons à l'aide de numpy, en utilisant les ndarrays. Enfin ce code compare les versions de base et numpy avec les méthodes déjà implémenter dans numpy pour la méthode des trapèzes et dans scipy pour la méthode de Simpson.


# Comment utiliser le code

Pour pouvoir faire fonctionner le code correctement, il faut au préalable installer les package : 
- numpy
- scipy
- matplotlib
- timeit

Ensuite selon les manipulation à faire, il est possible de comparer les fonctions deux à deux, analyser et appeler les fonctions dans le fichier main.py.


# Stratégie adoptée pour la structure du code

Le code est structuré en 7 fichiers : calculs.py, methode_rectangles.py, methode_trapezes.py, methode_simpson.py, affichage.py, analyse.py et main.py.

Dans un premier temps les scripts calculs.py, methode_rectangles.py, methode_trapezes.py et methode_simpson.py ont été implémentées pour calculer les intégrales selon les méthodes proposées. Ensuite nous avons implémenté le script analyse.py afin de récupérer le temps de calcul des méthodes et leur erreur relative et de les comparer sur un graphique pour plusieurs segments.

## calculs.py

Ce script est composé de deus fonctions : 
- evaluation(P, value) : permet de calculer la valeur du polynôme d'ordre 3 dont les coefficient sont indiqué dans P par degrés croissant, en value.
- integrale_analytique(P, a, b) : permet de calculer l'intégrale du polynôme d'ordre 3 dont les coefficient sont indiqué dans P par degrés croissant, entre a et b (a < b).

## methode_rectangles.py

Ce script est composé de deux fonctions : 
- methode_rectangle_python(liste, a, b, n) : permet de calculer l'intégrale du polynôme d'ordre 3 dont les coefficient sont indiqué dans liste par degrés croissant, entre a et b (a < b), en utilisant la méthode des rectangles. Dans ce cas l'intervalle [a, b] est discrétisé en n segemnts et on utilise les éléments de base présents dans python.
- methode_rectangle_numpy(liste, a, b, n) : fait les mêmes calculs que la première fonction mais en utilisant les outils proposés par numpy comme les tableaux.

## methode_trapezes.py

Ce script est composé de trois fonctions : 
- methode_trapezes_python(P, a, b, nbre) : permet de calculer l'intégrale du polynôme d'ordre 3 dont les coefficient sont indiqué dans P par degrés croissant, entre a et b (a < b), en utilisant la méthode des trapèzes. Dans ce cas l'intervalle [a, b] est discrétisé en nbre segemnts et on utilise les éléments de base présents dans python.
- methode_trapezes_numpy(P, a, b, nbre) : fait les mêmes calculs que la première fonction mais en utilisant les outils proposés par numpy comme les tableaux.
- methode_trapezes_existante(P, a, b, nbre) : fait les mêmes calculs que la première fonction mais en utilisant fonction impléémentée dans numpy : trapz.


## methode_simpson.py

Ce script est composé de trois fonctions : 
- methode_simpson_python(P, a, b, nbre) : permet de calculer l'intégrale du polynôme d'ordre 3 dont les coefficient sont indiqué dans P par degrés croissant, entre a et b (a < b), en utilisant la méthode de Simpson. Dans ce cas l'intervalle [a, b] est discrétisé en nbre segemnts et on utilise les éléments de base présents dans python.
- methode_simpson_numpy(P, a, b, nbre) : fait les mêmes calculs que la première fonction mais en utilisant les outils proposés par numpy comme les tableaux.
- methode_simpson_existante(P, a, b, nbre) : fait les mêmes calculs que la première fonction mais en utilisant fonction impléémentée dans numpy : trapz.

## analyse.py




## affichage.py

Ce script permet de tracer les erreurs relatives de chaque méthode de calcul d'intégrale et leur temps de calcul sur deux graphiques différents.

Les fonctions y étant implémentées permettent de tracer les temps d'exécution et les erreurs relatives de chaque méthode de différentes manières. Afficher les temps de calcul seulement, les erreur seulement, pour une méthode, pour toutes les implémentations d'une méthode, pour chaque type d'implémentation...

## affichage_geo.py

Ce script permet de représenter visuelement les méthodes d'approximation d'intégraion:
- affichage_rectangle(liste, a, b, n): renvoi un type plt que l'on peut afficher afin d'observer la méthode des rectangles appliquée au polynôme de coefficients contenu dans la liste "list", sur l'interval [a,b] contenant n intervals.
- affichage_trapeze(liste, a, b, n): renvoi un type plt que l'on peut afficher afin d'observer la méthode des trapezes appliquée au polynôme de coefficients contenu dans la liste "list", sur l'interval [a,b] contenant n intervals.
- affichage_simpson(liste, a, b, n): renvoit un type plt que l'on peut afficher afin d'observer la méthode simpson appliquée au polynôme de coefficients contenu dans la liste "list", sur l'interval [a,b] contenant n intervals.
 
## main_geometrique.py
Ce script permet en le lançant d'afficher 3 graphiques pour chacune des méthodes (rectangle, trapeze et Simpson) selon les paramètres P: contenant les coefficients du polynôme, a: début de l'interval, b: fin de l'interval, n1: nombre de segments pour le premier graphique, n2: nombre de segments pour le second graphique, n3: nombre de segments pour le troisième graphique.

## main.py



