#!/usr/bin/env python
# coding: utf-8

# # Theorie des  jeux TP                                               
#    ### Master ACSYON  -------------------------------------------------------------------------------------------------- Université de Limoges
# 
# ## ----------------------------- Rami MECHI & Cleque Marlain MBOULOU -----------------------------------------

# # I-  Introduction
# 
# La théorie des jeux est un domaine des mathématiques qui propose une description formelle d'interactions stratégiques entre agents (appelés « joueurs »). Il existe plusieurs domaine dans lesquels elle est utilisée de divers façon, notament en  Relations internationales, économie, sciences politiques, sciences sociales, bioligie, etc.
# 
# Dans ce projet, nous apportant des solutions des exemples de solutions permettant de résoudre ces problèmes.

# # II-  Exercie 1 , 3 & 4
# 
# Nous avous écrit des programmes qui permettent à l’utilisateur de saisir un jeu à:
# 
# ##### Deux joueurs, deux actions par joueur  pour l'exercice 1;
# 
# ##### Deux joueurs, plusieurs actions par joueur  pour l'exercice 3;
# 
# ##### Plusieurs joueurs, plusieurs actions par joueur  pour l'exercice 4;
# 
#  et faire ce qui suit :
# 
# — Déterminer si le jeu est à somme nulle ou pas;
# 
# — Déterminer les équilibres de Nash purs (et mixtes pour l'exercice 1 uniquement);
# 
# — Déterminer les stratégies (faiblement et strictement) dominées, et, s’il y en a, les stratégies (faiblement et strictement) dominantes

# In[74]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
from sympy import*
from math import*
import copy


# ### A-  Fonction d'affichage
# 
# Dans cette fonction spécifique pour les exercice 1 et 3 (jeux à 2 joueurs) , nous avons voulu afficher les tableaux représentant les strategies de chaque joueurs sous forme normale.
# 
# ##### a-  Exercice 1 et 3
# 
# Dans le cas des exercices 1 et 3, pour des raisons de présentation du jeux sous forme normale, nous avons utilsé des fonctions d'affichage et de saisie du jeux différentes de l'exercice 4.
# 
# $\underline{\text{Affichage du jeux sous forme normale}}$

# In[75]:


# Fonction d'affichage du tableau
def afficher_tab(tab):
    print ('Tableau du jeu sous forme normale : \n')
    for ligne in tab:
        for element in ligne:
            print(element, end=' ')
        print()
M1 = [[[2,1],[0,0]],[[0,0],[1,2]]]
afficher_tab(M1)


# $\underline{\text{Liste}}$
# 
# Dans la fonction liste, nous demandons à l'utilisateur de saisir le gain de chaque joueurs, une fois.

# In[76]:


# Dans cette fonction, nous allons definir une liste va 
def liste(k,j,rep):
    l = []
    if(rep == "non"):
        for i in range(1,3):
                print("Saisir le gain du joueur ",i,"de la ligne",k," composante",j,":")
                gain = int(input())
                l.append(gain)
    else:
        for i in range(1,3):
            gain =float(np.random.randint(-13, 13))
            l.append(gain)
    return np.array(l)


# $\underline{\text{Saisie du jeux}}$
# 
# Dans cette fonction, nous demandons à l'utilisateur de saisir les gains de chaque joueurs ( $nb\_strat\_J1 \times nb\_strat\_J2$)  car dans le cas de ces deux exercices, nous n'avons que deux joueurs, deux strtégies par joueur et le nombre de stratégie au choix pour l'exercice 3

# In[77]:


def saisi_jeux1(L = [2,2]):
    tab = []
    rep = input("voulez vous genérer un jeux aléatoire? oui ou non? \n " )
    while rep != 'non' and rep != 'oui' :
        print('Veuillez repondre par "oui" ou "non" SVP ! \n ')
        rep = input("voulez vous genérer un jeux aléatoire? oui ou non? \n " ) 
    for i in range(1,L[0]+1):
        ligne_i = []
        for j in range(1,L[1]+1):
            strategiei_j = liste(i,j,rep)
            ligne_i.append(strategiei_j)
        tab.append(ligne_i)
    return tab


# ###### b-  Exercice 4
# 
# Dans l'exercice 4, beaucoup plus complexe avec la croissance du nombre de joueurs, qui peut être supérieur à 2, nous avons procédé différemment.
# 
# $\underline{\text{Table de stratégies}}$
# 
# La fonction strategies(n,L) prend en parametre le nombre de joueurs $n$ et et la liste $L$ correspondant à la liste contenant le nombre de stratégies de chaque joueur, retourne une liste de listes vide pour initialiser le tableau du jeux sous sa forme extensive.

# In[78]:


def strategies(n,L):
    if len(L) == n :
        tab = []
        for i in range(n):
            tab.append(([]))
        j=0
        while(j<len(L)):
            for i in range(L[j]):
                l = []
                tab[j].append(l)
            j=j+1
        return tab
    else : 
        print('attention ! incoherence entre le nombre de joueurs et la taille de la liste des stratégies')


# $\underline{\textbf{Construction du procédé de remplissage du tableau}}$
# 
#     Dans cette fonction l'objectif est de construire la liste suivante des indices
#     de stratégies de chaque joueur de telle sorte:
#     
#     Exemple: 3 joueurs 2,3,3 respectivement le nombre de stratégie par joueur
#     la liste initiale est: L = [0,0,0], puis [1,0,0]-->[0,1,0]-->[1,1,0]-->[0,2,0] ... -->[1,2,2]
#     
#     l : liste des indices des strategies précédentes
#     L : liste du nombre de strategies par joueur, elle est fixe

# In[79]:


def next_liste(l,L):
    for i in range(len(l)):
        if((l[i]+1)%L[i]==0):
            for j in range(i+1,len(l)):
                if((l[j]+1)%L[j]==0):
                    continue
                else:
                    l[j] = l[j] + 1
                    for k in range(j):
                        l[k]=0
                    return l
        else:
            l[i] = l[i]+1
            return l


# $\underline{\textbf{Remplissage du tableau}}$
# 
# Dans cette fonction, nous allons remplir le tableau des contenant les listes de strategies de chaque joueurs. 
# 
# La fonction $gain\_joueurs()$ est a appelée dans la fonction $saisi\_stract $ pour le faire.

# In[80]:


def gain_joueurs(nb_joueurs,num_strat_joueurs,tab,reponse):
    tab1 = tab.copy()
    if(reponse == "non" ):
        for i in range(nb_joueurs):
            print(" saisissez le gain du joueur num°",i+1)
            k = float(input())
            tab1[i][num_strat_joueurs[i]].append(k)
    else:
        for i in range(nb_joueurs):
            k = np.random.randint(-13, 13)
            tab1[i][num_strat_joueurs[i]].append(k)
    return tab1

def saisi_stract(n,L):
    
    liste = [0]*n
    tab = strategies(n,L)
    reponse = input('voulez-vous un jeu aléatoires ? "oui" ou "non"')
    while (reponse!="oui" and reponse!="non"):
        print('Veuillez repondre par oui ou non SVP ! (en miniscule) ')  
        reponse = input('voulez-vous un jeu aléatoires ? "oui" ou "non"')
    while(liste!= None) :
        tab = gain_joueurs(n,liste,tab,reponse)
        liste = next_liste(liste,L)
    print('============================================================== \n')
    return tab

# Fonction d'affichage du tableau

def afficher_strat(tab):
    i = 1
    for ligne in tab:
        print("Joueurs", i)
        for element in ligne:
            print(element, end=' ')
        i+=1
        print()


# ### B-  Jeux à somme nulle
# 
# On appelle jeu à somme nulle ou jeu strictement compétitif, les jeux à deux joueurs dans lesquels l'intérêt de l'un des deux joueurs est strictement opposé à l'intérêt de l'autre joueur. Si les préférences des joueurs sont représentées par une fonction de gain ou une fonction d'utilité, alors la somme des deux fonctions est toujours égale à 0.

# $\underline{\textbf{Somme Nulle exercices 1 et 3}}$

# In[81]:


def somme_nulle(tab):
    k = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            k = sum(m for m in tab[i][j])
            if(k==0):
                continue
            else:
                print("Le jeux n'est pas à somme nulle")
                k = -1
                return k
    if (k==0):
        print("Le jeux est à somme nulle")


# $\underline{\textbf{Somme Nulle exercice 4}}$

# In[82]:


def somme_nulle4(n_joueurs,tab,L) :
    l = [0]*len(L)
    t = copy.deepcopy(tab)
    s = 0
    while (s == 0) & (l!= None)  :
        for i in range(n_joueurs) :
            s = s + t[i][l[i]][0]
            del(t[i][l[i]][0])
        l = next_liste(l,L)
    if s!=0 : 
        print("le jeu n'est pas à somme nulle ! " )
    else : 
         print("le jeu est à somme nulle ! " )
        


# ### C- Equilibre de Nash en stratégies Purs

# L'équilibre de Nash est souvent présenté comme une situation où chaque joueur adopte la meilleure répons compte tenu du choix des autres, l'équilibre de Nash est donc tel qu'aucun joueur ne regrette son choix (il n'aurait pas pu faire mieux) au vu du choix des autres, les choix étant, comme toujours en théorie des jeux, simultanés 

# $\underline{\textbf{Equilibre de Nash en stratégies purs exercices 1 et 3}}$

# In[83]:


def gainj(i,j,tab):
    list1 = []
    list2 = []
    for k in range(len(tab)):
        m = tab[k][j][0]
        list1.append(m)
    for k in range(len(tab[0])):
        m = tab[i][k][1]
        list2.append(m)
    return(list1,list2)

                


# In[84]:


def Nash_pure13(tab):
    equ_nash = []
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            list1,list2 = gainj(i,j,tab)
            if([tab[i][j][0],tab[i][j][1]]==[np.max(list1),np.max(list2)] ):
                print(tab[i][j], " est  un équilibre de nash en stratégie pure pour la stratégie ",i+1,"  du joueur 1 et la strategie", j+1," du joueur 2")
                equ_nash.append(tab[i][j])
    if(len(equ_nash)==0):
        print("Ce jeux n'as pas d'équilibre de nash en stratégie pure")
    return equ_nash


# $\underline{\textbf{Equilibre de Nash en stratégies purs exercices 4}}$

# L'idée de cette fonction est de : 
# - parcourir la liste des gains de toutes les stratégies d'un joueur $i$ donnée 
# - comparer chaque element ( gain ) avec tous les autres 
# - donner un point (+1) au plus grand et donc à la (aux) stratégie(s) qui maximise le gain du joueur $i$
# - appliquer le meme processus pour tous les joueurs 
# - compter le nombre de points par profil de stratégie et celui qui a un nombre de points égale aux nombre de joueurs est un equilibre de Nah en stratégies pures. 
# 
# $\underline{\textbf{Explication du dernier point :}}$ Le fait qu'un profil de stratégie $S^{*}$ aie le meme nombre de points que le nombre de joueurs revient à dire que chaque joueur maximise son gain en jouant la stratégie $s^{*}_{i}$ compte tenu des autres stratégies $s^{*} \in S^{*}_{-i}$, autrement dit tous les joueurs n'ont pas intêret à changer leurs stratégies !
# 
# **N.B : plusieurs profils de stratégies peuvent satisfaire la condition autrement dit avoir un nombre de points égale aux nombre de joueurs et donc on peut avoir plusieurs equilibre de Nash ( car nous chercherchons des equilibres de Nash et non pas des equilibres des equilibre de Nash strict )**

# In[85]:


def Nash_pure4 (n,tab1,L) :
    tab = copy.deepcopy(tab1)
    Nash = False
    nash = []
    equilibre = []
    for i in range(n) : 
        for j in range (len(tab[i][0])) :
            maxi = 0 
            k = 1
            while  (k<L[i]) :
                if tab[i][maxi][j] < tab[i][k][j] :
                    tab[i][maxi][j] = 0
                    maxi = k
                    k += 1
                else : 
                    tab[i][k][j] = 0
                    k += 1
            tab[i][maxi][j] = 1
            
    l1 = [0]*n
    while l1 != None :
        s = 0
        for i in range(n) :
            s = s + tab[i][l1[i]][0]
            del(tab[i][l1[i]][0])
        nash.append(s)
        equilibre.extend(l1)
        l1 = next_liste(l1,L)

    for i in range (len(nash)) :
            if nash[i] == n :
                Nash = True
                print('la liste des stratégie :',equilibre[i*n : (i+1)*n],' forme un équiibre de Nash en stratégie pure')
                
    if Nash == False :
        print("Ce jeu n'a pas d`èquilibre de Nash en stratégie pure")
    


# ###  D- Equilibre de Nash en stratégie mixtes: Exercice 1
# 
# $\underline{\textbf{Listes des gains par stratégies des joueurs}}$
# 
# La fonction **strat_joueurs()** renvoie deux listes contenant les  gains par stratégies de chaque Joueurs.
# 
# Considérons l'exemple suivant où $A_1$ et $B_1$ sont les strategies du joueur 1, et $A_2$ et $B_2$ sont les strategies du joueur 2. La formale normal du jeux est données par:
# 
# 
# |    |$A_2$ | $B_2$ |
# | :------------ | :----------- |:----------- |
# |$A_1$ |(2,3) | (1,1) |
# |$B_1$ |(4,1) | (4,1) |
# 
# La fonction $strat_joueurs$ renvoiera $L_1,L_2 = ((2,1),(4,4)),((3,1),(1,4))$

# In[86]:


# prend en parametre un une matrice et renvoi les liste de strategies dechaque joueurs

def strat_joueurs(tab):
    liste1 = []
    liste2 = []
    #Joueur 1
    for i in range(len(tab)):
        list1 = []
        for j in range(len(tab[0])):
            list1.append(tab[i][j][0])
        liste1.append((list1))
    # Joueur 2
    for j in range(len(tab[0])):
        list2 = []
        for i in range(len(tab)):
            list2.append(tab[i][j][1])
        liste2.append((list2))
    if(len(liste1)==1):
        liste1=[[liste1[0][1]]]
    return liste1,liste2


# $\underline{\textbf{Equilibre de Nash Mixte}}$
# 
# La fonction $nash\_mixtes$ prend en parametre la matrice du jeux sous sa forme extensive et effectue les étapes suivantes:
# 
# - Extrait  dans deux liste les gains par stratégies de  chaque joueurs par la fonction précédente, puis crée des variables $p_1$ et $p_2$.
# - Calcul la fonction d'utilité de chaque joueur en fonction de $p_1$ et $p_2$. En considérons l'exemple précédent on a:
# 
# $U_1(p_1,p_2) = 2p_1p_2 + p_1(1-p_2) + 4(1-p_1)p_2 + 4(1-p_1)(1-p_2)$ et  $U_2(p_1,p_2) = 3p_1p_2 + p_1(1-p_2) + (1-p_1)p_2 + (1-p_1)(1-p_2)$
# 
# -Puis pour le joueur 1 on essaie de résoudre le système $\frac{\partial U_1(p_1,p_2)}{\partial p1} = 0 $ pour déterminer $p_2$ . Quand ceci n'est pas possible:
# 
# On evalue $\frac{\partial U_1(p_1,p_2)}{\partial p1}$ pour $100$ points de  $p_2\in [0,1]$. si $\frac{\partial U_1(p_1,p_2)}{\partial p1}>0$ pour les $100$ valeurs de $p_2$, $p_2$ vaudra $1$, sinon $p_2$ vaudra $0$
# 
# 
# De memê pour le joueur 2  on essaie de résoudre le système $\frac{\partial U_2(p_1,p_2)}{\partial p2} = 0 $ pour déterminer $p_1$ . Quand ceci n'est pas possible:
# 
# On evalue $\frac{\partial U_2(p_1,p_2)}{\partial p2}$ pour $100$ points de  $p_1\in [0,1]$. si $\frac{\partial U_2(p_1,p_2)}{\partial p2}>0$ pour les $100$ valeurs de $p_1$, $p_1$ vaudra $1$, sinon $p_1$ vaudra $0$
# 
# - Puis renvoie ses valeurs de $p_1$ et $p_2$.

# In[87]:


def nash_mixtes(tab):
    
    strat1,strat2 = strat_joueurs(tab)
    p1, p2 = symbols('p1 p2', real=True)
    # Utilité de chaque joueurs :
    equ1 = simplify(strat1[0][0]*p1*p2 + strat1[1][0]*p1*(1-p2) +strat1[0][1]*p2*(1-p1) + strat1[1][1]*(1-p1)*(1-p2))
    equ2 = simplify(strat2[0][0]*p1*p2 + strat2[1][0]*p2*(1-p1) +strat2[0][1]*p1*(1-p2) + strat2[1][1]*(1-p1)*(1-p2))
    # Résoltion des equations de chaque dérivée des utilités :
    x_vals = np.linspace(0, 1, 101)
    sol1, sol2 = 0,0
    
    try:
        sol1 = list(solveset(diff(equ1, p1), p2, domain=sp.Interval(0, 1)))[0]
    except:
        equ11 = lambdify(p2, diff(equ1, p1), 'numpy')
        equ1_vals = equ11(x_vals)
        # Teste si tous les élément sont positif ou négatif
        if np.all(equ1_vals > 0):
            sol1 = 1
        if np.all(equ1_vals < 0):
            sol1 = 0
    try:
        sol2 = list(solveset(diff(equ2, p2), p1, domain=sp.Interval(0, 1)))[0]
    except:
        equ22 = lambdify(p1, diff(equ2, p2), 'numpy')
        equ2_vals = equ22(x_vals)
        # Teste si tous les élément sont positif ou négatif
        if np.all(equ2_vals > 0):
            sol2 = 1
        if np.all(equ2_vals < 0):
            sol2 = 0  
    return sol2,sol1

M1 = [[[1,3],[5,0]],[[3,1],[2,4]]]
M2 = [[[1,1],[1,1]],[[-1,-1],[2,0]]]
afficher_tab(M2)
nash_mixtes(M2)


# ### E- Stratégies faiblement et strictement dominées & dominantes
# 
# 

# $\underline{\textbf{stratégie dominée :}}$
# 
# Une stratégie $s_{i}$ est strictement dominée (resp. faiblement dominée)
# pour un joueur $A$ si et seulement s’il existe une autre stratégie $s^{∗}$ telle
# que, quelles que soient les stratégies adoptées par les autres joueurs,
# cette autre stratégie $s^{∗}$ est toujours strictement meilleure que $s_{i}$ (resp.
# au moins aussi bonne que $s_{i}$ et strictement meilleure dans au moins
# l’une des situations) .
# 
# $\underline{\textbf{stratégie dominante :}}$
# 
# Une stratégie $s_{i}$ est dominante (resp. faiblement dominante) pour un
# joueur $A$ si et seulement si quelles que soient les actions de l’autre
# joueur la stratégie $s_{i}$ apporte{ strictement plus (resp. plus ou égal) de
# gain que les autres stratégies du joueur $A$.
# 

# ### Exercice 1 ,3 et 4

# In[88]:


#  Renvoie True si la stratégie i  du joueur est strictement dominée par  sa stratégie j  et false sinon
def strict_dominer(strategie_i,strategie_j):
    for i in range(len(strategie_i)):
        if(strategie_i[i]>=strategie_j[i]):
            return False
    else:
        return True
#  Renvoie True si la stratégie i  du joueur est faiblement dominée par  sa stratégie j  et false sinon
def faible_dominer(strategie_i,strategie_j):
    k = 0
    for i in range(len(strategie_i)):
        if(strategie_i[i]>strategie_j[i]):
            return False
        if(strategie_i[i]<strategie_j[i]):
            k+=1
    else:
        if(k>=1 and k< len(strategie_i)):
            return True
        else:
            return False
    
# Renvoie True si l1 est une strategie dominante parmi l'ensemble de strategies(liste) du joueur
def strict_dominant(strategie,stra_liste):
    liste1 = stra_liste.copy()
    k = liste1.index(strategie)
    del(liste1[k])
    for i in range(len(liste1)):
        for j in range(len(liste1[0])):
            if(strategie[j]<=liste1[i][j]):
                return False
    else:
        return True

def compare(list1,list2):
    all_greater = True

    for i in range(len(list1)):
        if list1[i] < list2[i]:
            all_greater = False
            break
    return all_greater
 
def faible_dominant(strategie,stra_liste):
    liste1 = stra_liste.copy()
    k = liste1.index(strategie)
    del(liste1[k])
    i = 0
    for j in range(len(stra_liste)):
        if(compare(strategie,stra_liste[j] )==True) :
            if(np.all(np.array(strategie) - np.array(stra_liste[j]) == 0) == False):
                  i+=1
    else:
        if(i>=1):
            return True
        else:
            return False


# In[89]:


def strat_dom(nb_joueurs,tab,exo,etape=0,k = 0):
    etape = etape +1
    tab1 = copy.deepcopy(tab)
    liste3 = []
    ligne = []
    
    if(nb_joueurs>2):
        L = copy.deepcopy(tab) # Represenatant directement les listes de strategie de chaque joueurs   
    else:
        L = strat_joueurs(tab) # Extraction des stratégies de chaque joueurs

    for i in range(len(L[k])):
        if(faible_dominant(L[k][i],L[k])==True): # test des stratégies faiblement dominantes
            print("La strategie",i+1,"(",L[k][i], ") du joueur", k+1 ,"est faiblement dominante")
        if(strict_dominant(L[k][i],L[k])==True): # test des stratégies strictementdominantes
            print("La strategie",i+1,"(",L[k][i], ") du joueur", k+1 ,"est strictement dominante")
        for j in range(i+1,len(L[k])):
                if(faible_dominer(L[k][i],L[k][j])==True):
                    print("A l'étape", etape,":\n")
                    print("La strategie",i+1,"(",L[k][i],") du joueur ",k+1," est faiblement dominée par sa strategie", j+1, "(",L[k][j],")")
                    if(strict_dominer(L[k][i],L[k][j])==True):
                        print("La strategie",i+1,"(",L[k][i],") du joueur ",k+1," est strictement dominée par sa strategie", j+1, "(",L[k][j],")")
                        liste3.append(L[k][i])
                        ligne.append(i)
                    break
                    
                elif(faible_dominer(L[k][j],L[k][i])==True):
                    print("A l'étape", etape,":\n")
                    afficher_tab(tab1)
                    print("La strategie",j+1,"(",L[k][j],") du joueur ",k+1," est faiblement dominée par sa strategie", i+1, "(",L[k][i],") ")
                    if(strict_dominer(L[k][j],L[k][i])==True):
                        print("La strategie",j+1,"(",L[k][j],") du joueur",k+1," est strictement dominée par sa strategie", i+1, "(",L[k][i],") ")
                        liste3.append(L[k][j])
                        ligne.append(j)
                    break
    
    if(len(liste3)==0 ):# On s'interesse aux stratégies du joueur suivant s'il n'y a pas de stratégie dominante dans celle du joueur précédent
        print("\n")
        print("A l'étape", etape,":\n")
        print("Le joueur",k+1, " n'a pas de stratégie strictement dominée.\n")
        if(k<nb_joueurs-1):
            k = k+1
            strat_dom(nb_joueurs,tab1,exo,etape=0,k=k%nb_joueurs) # Changement de joueurs
    elif(len(liste3)==1):
        if(nb_joueurs>2):
            L[k].remove(liste3[0])
            try:
                strat_dom4(nb_joueurs,tab1,exo,etape,k)
            except:
                print("Final:\n")

                return tab1
        else:
            if(k==0):
                del(tab1[ligne[0]]) 
                ligne = []
            else:
                for w in range(len(tab1)):
                    del(tab1[w][ligne[0]])
                ligne =[]
            try:
                strat_dom(nb_joueurs,tab1,exo,etape,k=k)
            except:
                print("Final:\n")
                afficher_tab(tab1) 
                return tab1
    else:
        print("AUCUNE STRATEGIE STRICTEMENT DOMINEE")


# ### F- Organisation des exercices
# 
# 
# $\underline{\textbf{Exercice 1}}$

# In[90]:


def Exercice1():
    print('-------------------------------- Exercice 1 ------------------------------------ \n')
    M = saisi_jeux1() 
    afficher_tab(M)
    print("*************************************************************************")
    print("\n")
    Nash_pure13(M)
    print("*************************************************************************")
    print("\n")
    print("L'équilibre de Nash en stratégies mixtes est:  p* =",nash_mixtes(M))
    print("*************************************************************************")
    print("\n")
    somme_nulle(M)
    print("*************************************************************************")
    print("\n")
    strat_dom(2,M,1)
#essai (facultatif) : 
#Exercice1()


# $\underline{\textbf{Exercice 3}}$

# In[91]:


def Exercice3():
    print('- -------------------------------- Exercice 3 ------------------------------------ \n')
    nb_strat1 = int(input("Combien de stratégies possède le joueur 1?\n "))
    nb_strat2 = int(input("Combien de stratégies possède le joueur 2?\n"))
    
    M = saisi_jeux1([nb_strat1,nb_strat2])
    afficher_tab(M)
    print("*********************************************************************************************************")
    print("\n")
    Nash_pure13(M)
    print("********************************************************************************************************")
    print("\n")
    somme_nulle(M)
    print("*********************************************************************************************************")
    print("\n")
    strat_dom(2,M,3)
#essai (facultatif) :    
#Exercice3()


# $\underline{\textbf{Exercice 4}}$

# In[92]:


def Exercice4():
    print('-------------------------------- Exercice 4 ------------------------------------ \n')
    print("Combien de Joueurs possède le Jeu: ")
    N = int(input())
    L = []
    for i in range(N):
        print("Nombre de strategies du joueur num° ", i+1)
        nb_strat = int(input())
        L.append(nb_strat)
    if N<=2:
        t = saisi_stract(N,L)
        afficher_tab(M)
        print("*************************************************************************")
        print("\n")
        Nash_purs1(M)
        print("*************************************************************************")
        print("\n")
        somme_nulle(M)
        print("*************************************************************************")
        print("\n")
        strat_dom(2,M,3)
    else:
        t = saisi_stract(N,L)
        print('voici le tableau de gain par strat de tous les joueurs : \n')
        afficher_strat(t) 
        print('************************************************************************* \n')
        Nash_pure4(N,t,L)
        print('************************************************************************* \n')
        somme_nulle4(N,t,L)
        print('************************************************************************* \n ')
        strat_dom(N,t,4)
# essai (facultatif) :
#Exercice4()


# # III- Exercice 2

# In[97]:


###### Exercice 2
N=1000

def rand_bernoulli(p):
    x = np.random.random()
    if x <= p: return 1
    else: return 0

def gains(i,j):
    liste = []
    print("Veuillez saisir le gain du joueur 1 si la loi de Bernouilli renvoie (",i,",",j,")")
    gain1 = float(input())
    liste.append(gain1)
    print("Veuillez saisir le gain du joueur 1 si la loi de Bernouilli renvoie (",i,",",j,")")
    gain2 = float(input())
    liste.append(gain2)
    return liste

def saisie_gain(rep):
    
    tab = []
    if rep == 'non' :
        for i in range(2):
            liste = []
            for j in range(2):
                gain = gains(i,j)
                liste.append(gain)
            tab.append(liste)
    else : 
         for i in range(2):
            liste = []
            for j in range(2):
                gain = [np.random.randint(-10,10),np.random.randint(-10,10)]
                liste.append(gain)
            tab.append(liste)
    return tab

def saisi_jeux2(Mat):
    
    equ1 = str(input("Joueur 1, Voulez-vous choisir un équilibre de Nash mixte oui ou non? \n"))
    while equ1 != 'non' and equ1 != 'oui' :
        print("Veuillez repondre par 'oui' ou 'non' SVP !")
        equ1 = str(input("Joueur 1, Voulez-vous choisir un équilibre de Nash mixte? oui ou non? \n"))
    if(equ1=="oui"):
        p1 = nash_mixtes(Mat)[0]
    elif(equ1 == "non"):
        print("Saisir la proba du joueur 1 (Valeur comprise entre 0 et 1)\n")
        p1 = float(input())
        while(p1<0 or p1>1):
            print("Saisir la proba du joueur 1 (Valeur comprise entre 0 et 1)\n")
            p1 = float(input())
            
    equ2 = str(input("Joueur 2, Voulez-vous choisir un équilibre de Nash mixte? oui ou non? \n"))
    while equ2 != 'non' and equ2 != 'oui' :
        print("Veuillez repondre par 'oui' ou 'non' SVP !")
        equ2 = str(input("Joueur 2, Voulez-vous choisir un équilibre de Nash mixte oui ou non? \n"))
    if(equ2 == "oui"):
        p2 = nash_mixtes(Mat)[1]
    elif(equ2 == "non"):
        print("Saisir la proba du joueur 2 (Valeur comprise entre 0 et 1)\n")
        p2 = float(input())
    
        while(p2<0 or p2>1):
            print("Saisir la proba du joueur 2 (Valeur comprise entre 0 et 1)\n")
            p2 = float(input())
    gain1 = 0
    gain2 = 0
    for i in range(N):
        indx1, indx2 = rand_bernoulli(p1), rand_bernoulli(p2)
        gain1 = gain1 + Mat[indx1][indx2][0]
        gain2 = gain2 + Mat[indx1][indx2][1]
    gain1, gain2 = gain1/N, gain2/N
    print("Joueur 1 : Gain moyen ",gain1)
    print("Joueur 2 : Gain moyen ",gain2)
    #return(gain1,gain2)


# $\underline{\textbf{Exemple : dilemme du prisonnier}}$

# In[104]:


M = [[[3,3],[-1,4]],[[4,-1],[0,0]]]
afficher_tab(M)
saisi_jeux2(M)


# $\underline{\textbf{Exercice 2}}$

# In[155]:


def Exercice2():
    print('-------------------------------- Exercice 2 ------------------------------------ \n')
    
    alea = input('Voulez-vous un jeu aléatoire? oui ou non? \n')
    
    while alea != 'oui' and alea != 'non' :
        print('Veuillez repondre par "oui" ou "non" SVP ! \n')
        alea = input('Voulez-vous un jeu aléatoire? oui ou non? \n')
    
    M = saisie_gain(alea)
    afficher_tab(M)
    saisi_jeux2(M)
# essai (facultatif) :
#Exercice2()


# # IV- Mise en place

# In[191]:


def Projet() :
    
    exo = input('Quel exercice voulez-vous simuler ?  \n ')
   
    
    if(exo == '1'):
        Exercice1()
    if(exo == '2'):
        Exercice2()
    if(exo == '3'):
        Exercice3()
    if(exo == '4'):
        Exercice4()
    if exo != "1" and exo != "2" and exo != "3" and exo != "4" : 
        print('veuillez saisir un entier entre 1 et 4 SVP ! \n ' )
        Projet()
        return
    print('========================================================================== \n')
    rep = input("Voulez vous Simuler un autre exercice? 'oui' ou 'non' ? ")
    while(rep != 'oui' and rep != 'non' ):
        print('Veuillez répondre par "oui" ou "non" SVP ! \n')
        rep = input("Voulez vous Simuler un autre exercice? 'oui' ou 'non' ? ")
        
    if(rep == "oui"):
        Projet()
    else :
        print('\n')
        print('Fin du projet ! A BIENTOT :) ')
        


# # C'est parti !!!

# In[185]:


Projet()

