# Projet scolaire et personnel

Projet réalisé en 3 jours dans le cadre de ma reconversion à la Coding Factory.
Par la suite, j'ai retravaillé le code pour finir d'intégrer les différents écrans et la gestion du score.

Cependant, le code souffre de l'absence de l'orientée objet.

## Règles du jeu

Pyjeu mélange réflexe et réflexion dans un jeu de tir à la souris.​


L'objectif est de tirer sur des cibles mouvantes afin de gagner des points, tout en évitant de toucher les leurres et les obstacles.​

Les leurres enlèvent des points, tandis que les obstacles empêchent le joueur de tirer pendant un certain temps, lui faisant perdre de précieuses secondes.​


La partie se termine lorsque le joueur a éliminé toutes les cibles à l'écran mais n'a pas de limite de temps pour le faire.​
​

Les cibles sont des nombres, dont le nombre et le contenu varie selon le niveau de difficulté :​

Facile : Multiples de 2 - (nombre de cible à définir)​

Intermédiaire : Multiples de 7 - (nombre de cible à définir)​

Difficile : Multiple de 3 en hexadécimale - (nombre de cible à définir)​


Le score est calculé en fonction du nombre de cibles détruites, et du temps écoulé avant destruction de l'ensemble des cibles.
