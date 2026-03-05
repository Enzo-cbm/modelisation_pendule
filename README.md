README — Spring Pendulum Simulation (Python)

Description
-----------
Ce projet simule la dynamique d’un pendule à ressort (spring pendulum) en utilisant
une intégration numérique avec la fonction solve_ivp de SciPy.

Le système est un pendule dont la longueur peut varier grâce à un ressort.
Le mouvement est décrit par :
- la longueur du ressort l
- l’angle θ

Le programme calcule l’évolution temporelle, la trajectoire (x,y), les énergies,
et peut générer une animation si le module animation.py est présent.

Dépendances
-----------
- numpy
- scipy
- matplotlib
- (optionnel) un module local animation.py fournissant generate_animation

Exécution
---------
pip install numpy scipy matplotlib
python spring_pendulum.py

Animation (optionnel)
---------------------
Si un fichier animation.py est présent dans le même dossier (ou importable),
le script appelle :
generate_animation(sol.y[1], sol.y[0], dt=0.01)

Sorties
-------
- x(t), y(t)
- trajectoire dans le plan
- énergies + erreur de conservation
- histogramme 2D pour un ensemble de conditions initiales
- animation (si disponible)
