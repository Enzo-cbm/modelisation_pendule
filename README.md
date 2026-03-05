README — Spring Pendulum Simulation (Python)

Description
-----------
Ce projet simule la dynamique d’un pendule à ressort (spring pendulum) en utilisant
une intégration numérique avec la fonction solve_ivp de SciPy.

Le système est un pendule dont la longueur peut varier grâce à un ressort de
constante k. Le mouvement est donc décrit par deux coordonnées :
- la longueur du ressort l
- l’angle θ du pendule

Le programme calcule l’évolution temporelle du système, la trajectoire dans
le plan (x,y), ainsi que les différentes énergies du système.

Modèle physique
---------------
Le système est gouverné par deux équations différentielles couplées :

d²θ/dt² = -(1/l)(g sin(θ) + 2 dl/dt dθ/dt)

d²l/dt² = (1/m)(m l (dθ/dt)² − k(l − l0) + m g cos(θ))

Paramètres du modèle
--------------------
g  : accélération gravitationnelle
m  : masse
k  : constante du ressort
l0 : longueur naturelle du ressort

Conditions initiales
--------------------
[l, θ, dl/dt, dθ/dt]

Le système est ensuite intégré numériquement avec solve_ivp.

Fonctionnalités
---------------
- simulation du mouvement du pendule à ressort
- visualisation des positions x(t) et y(t)
- affichage de la trajectoire dans le plan
- calcul des énergies :
    énergie potentielle
    énergie cinétique
    énergie totale
- vérification de la conservation de l’énergie
- simulation de nombreuses conditions initiales
- histogramme 2D des positions explorées

Exécution
---------
Installer les dépendances :

pip install numpy scipy matplotlib

Puis exécuter le script :

python spring_pendulum.py

Sorties
-------
Le script génère plusieurs figures :

- évolution temporelle de x(t) et y(t)
- trajectoire du pendule
- évolution des énergies
- histogramme 2D des positions

Remarques
---------
La simulation utilise une intégration numérique explicite et peut être
utilisée pour explorer la dynamique non linéaire du système.

Améliorations possibles
-----------------------
- animation du mouvement du pendule
- étude de la stabilité du système
- ajout de conditions initiales paramétrables
- optimisation du calcul pour un grand nombre de simulations
