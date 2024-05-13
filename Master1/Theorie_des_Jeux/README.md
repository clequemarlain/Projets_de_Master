


# Theorie des  jeux TP                                               
### Master ACSYON  
### Université de Limoges
# 
### Cleque Marlain MBOULOU 

#  I-  Introduction
# 
### La théorie des jeux est un domaine des mathématiques qui propose une description formelle d'interactions stratégiques entre agents (appelés « joueurs »). Il existe plusieurs domaines dans lesquels elle est utilisée de diverses façons, notamment en Relations internationales, économie, sciences politiques, sciences sociales, biologie, etc.
# 
### Dans ce projet, nous apportons des solutions et des exemples permettant de résoudre ces problèmes.

# # II-  Exercices 1, 3 & 4
# 
-  Nous avons écrit des programmes qui permettent à l’utilisateur de saisir un jeu à :
# 
-  Deux joueurs, deux actions par joueur pour l'exercice 1;
# 
-  Deux joueurs, plusieurs actions par joueur pour l'exercice 3;
# 
-  Plusieurs joueurs, plusieurs actions par joueur pour l'exercice 4;

# 
et de faire ce qui suit :
# 
# 
— Déterminer si le jeu est à somme nulle ou pas;
# 
# 
— Déterminer les équilibres de Nash purs (et mixtes pour l'exercice 1 uniquement);
# 
# 
— Déterminer les stratégies (faiblement et strictement) dominées, et, s’il y en a, les stratégies (faiblement et strictement) dominantes.

## Fonctions disponibles

1. **strict_dominer**

   Détermine si une stratégie est strictement dominée par une autre stratégie pour un joueur donné. Utile pour évaluer la domination dans les jeux à somme nulle.

2. **faible_dominer**

   Détermine si une stratégie est faiblement dominée par une autre stratégie pour un joueur donné. Permet d'évaluer la domination faible dans les jeux à somme nulle.

3. **strict_dominant**

   Vérifie si une stratégie est strictement dominante parmi un ensemble de stratégies pour un joueur. Utile pour identifier les stratégies optimales dans les jeux à somme nulle.

4. **compare**

   Compare deux listes élément par élément et retourne True si tous les éléments de la première liste sont supérieurs ou égaux à ceux de la deuxième liste. Utilisée pour évaluer la domination faible dans les jeux à somme nulle.

5. **faible_dominant**

   Détermine si une stratégie est faiblement dominante parmi un ensemble de stratégies pour un joueur. Utile pour identifier les stratégies optimales dans les jeux à somme nulle.

---

Ce fichier README.md fournit une brève vue d'ensemble des fonctions disponibles dans ce code Python. Pour plus de détails sur l'utilisation de chaque fonction, veuillez consulter les commentaires dans le code source.
