#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:43:13 2021

@author: jc.burnot
Ce programme evalue les case jouables et les utilise dans la saisie protégée
C'est aussi un utilitaire qui permet de donner des indices de cases voulues
"""
#from CCoup import Ccoup
class Cjouable:
    def __init__(self,player,liste):
        self.__player=player
        self.__liste=liste

    #Donne les cases possible pour le joueur(!=jouable)
    def joueur(self):
        if self.__player==1:
            return [1,2,3,4,5,6]
        else:
            return [7,8,9,10,11,12]

    #Donne les cases de l'adversaire
    def adversaire(self):
        if self.__player==1:
            return [7,8,9,10,11,12]
        else:
            return [1,2,3,4,5,6]
    
    #Permet de donner l'indice de la borne inférieure de l'adversaire (dephase compense)
    def borninf(self):
        if self.__player==1:
            return 6
        if self.__player==2:
            return 0
        
    #Permet de donner l'indice de la borne supérieure de l'adversaire (dephasage compense)
    def bornsup(self):
        if self.__player==1:
            return 11
        if self.__player==2:
            return 5
    
    #Permet de connaitre le nombre de graine total dans les case
    def sommeadv(self):
        #Les +1/-1 permettent de régler le déphasage
        return sum(self.__liste[self.adversaire()[0]-1:self.adversaire()[-1]])
        
    #Detecte la famine
    def detecfam(self):
        if self.sommeadv()==0:
            return True
        else:
            return False
    
    #Evalue pour chaque coup si des graines seront seme chez l'adversaire
    #et stocke ces coups (utile en cas de famine)
    def semadv(self):
        lstl=[]
        if self.__player==1:
            #Parcours les indices des cases du joueur 1
            for i in range(1,6+1):
                #le -1 et le 5 permettent de régler le déphasage!
                if self.__liste[i-1]>=7-i:
                    #c'est le num de la case et non de l'indice de la liste
                    lstl.append(i)
            return lstl
        #meme processus mais avec un déphasage différent
        if self.__player==2:
            #Parcours les indices des cases du joueur 2
            for i in range(7,12+1):
                if self.__liste[i-1]>=14-i:
                    lstl.append(i)
            return lstl
      
        #donne une liste de cases jouables comprehensible pour le joueur
        #Ces case jouables sont en cas de famine les cases qui nourissent l'adversaire
        #et s'occupe de la saisie protégée
    def casjfam(self):
        if self.detecfam()==False:
            return self.joueur()
        if self.detecfam()==True:
            print("\033[31mAttention l'adversaire est en famine \nTu dois le nourrir\nTu Peux jouer les cases suivantes:\n"+str(self.semadv())+"\033[37m")
            return self.semadv()
