# Jeu de Morpion:
# 2 joueurs jouent l'un contre l'autre
# Les choix de placement sont basés sur le pavé numérique

import random
import IPython

def rejouer(reponse):
    if reponse == "O":
        print("Ok c'est reparti pour un tour !\n")
        return True
    elif reponse == "N":
        print("Merci d'avoir joué !\n")
        return False

def verif_gagnant(tab_jeu):
    #vérifie s'il y a un gagnant sur les lignes
    if tab_jeu[0:3] == 3*["X"] or tab_jeu[0:3] == 3*["O"]:
        return True
    elif tab_jeu[3:6] == 3*["X"] or tab_jeu[3:6] == 3*["O"]:
        return True
    elif tab_jeu[6:9] == 3*["X"] or tab_jeu[6:9] == 3*["O"]:
        return True
    
    #vérifie s'il y a un gagnant sur les colonnes
    elif tab_jeu[0:9:3] == 3*["X"] or tab_jeu[0:9:3] == 3*["O"]:
        return True
    elif tab_jeu[1:9:3] == 3*["X"] or tab_jeu[1:9:3] == 3*["O"]:
        return True
    elif tab_jeu[2:9:3] == 3*["X"] or tab_jeu[2:9:3] == 3*["O"]:
        return True
    
    #vérifie s'il y a un gagnant sur les diagonales
    elif [tab_jeu[0], tab_jeu[4], tab_jeu[8]] == 3*["X"] or [tab_jeu[0], tab_jeu[4], tab_jeu[8]] == 3*["O"]:
        return True
    elif [tab_jeu[2], tab_jeu[4], tab_jeu[6]] == 3*["X"] or [tab_jeu[2], tab_jeu[4], tab_jeu[6]] == 3*["O"]:
        return True
    #si aucun cas n'est vrai, alors il n'y a pas encore de gagnant
    else:
        return False
    
    
jeu_continue = True #inutile à ce stade
nbjoueur = 2 #inutile à ce stade
joueur_actif = "" #détermine quel joueur est actif pour savoir s'il faut mettre X ou O
choix_position = "" #correspond au choix de position à remplacer
choix_ok = False #booléen vérifiant si choix_position est un nombre compris entre 1 et 9 qui n'a pas déjà été joué

joueur1 = input("Quel est le nom du joueur 1 représenté par X ? ")
joueur2 = input("Quel est le nom du joueur 2 représenté par O ? ")

while jeu_continue == True:
    # Obtention du nom des joueurs

    tableau_choix = list(range(1,10))
    tableau_jeu = 9*[" "]

    # Sélection du premier joueur à jouer
    joueur_actif = random.choice([joueur1, joueur2])
    while " " in tableau_jeu:
        choix_ok = False
        choix_position = ""

        print(f"\nC'est à {joueur_actif} de jouer !")

        #afficher le tableau de jeu et la position des choix
        print("\nPour rappel, voici les différentes positions du tableau de jeu:\n")
        print("", tableau_choix[0:3], "\n",  tableau_choix[3:6], "\n", tableau_choix[6:9], "\n")

        print("Voici le tableau de jeu actuel :")
        print("", tableau_jeu[0:3], "\n", tableau_jeu[3:6],"\n", tableau_jeu[6:9], "\n")

        #demander au joueur où il veut jouer et vérifier le choix 
        while choix_ok == False:
            choix_position = input("Quelle position voulez-vous remplacer ? ")

            if choix_position.isdigit() == False:
                print("La position indiquée n'est pas un chiffre. Veuillez saisir un chiffre compris entre 1 et 9\n")

            elif int(choix_position) not in range(1, 10):
                print("Cette position n'est pas valide. Veuillez saisir un chiffre compris entre 1 et 9\n")

            elif tableau_jeu[int(choix_position) - 1] != " ":
                print("Cette position a déjà été jouée. Veuillez faire un autre choix !\n")

            else:
                choix_ok = True
        #Modifie la position avec le bon signe en fonction du joueur
        if joueur_actif == joueur1:
            tableau_jeu[int(choix_position) - 1] = "X"
        elif joueur_actif == joueur2:
            tableau_jeu[int(choix_position) - 1] = "O"  

        #vérifie s'il y a un gagnant et arrête la partie le cas échéant
        if verif_gagnant(tableau_jeu) == True:
            print(f"C'est fini et c'est {joueur_actif} qui l'emporte !")
            break
            

        #nettoie l'écran
        IPython.display.clear_output()

        # change de joueur
        if joueur_actif == joueur1:
            joueur_actif = joueur2
        elif joueur_actif == joueur2:
            joueur_actif = joueur1

    print("", tableau_jeu[0:3], "\n", tableau_jeu[3:6],"\n", tableau_jeu[6:9], "\n")
    if verif_gagnant(tableau_jeu) == False:
        print("\n La partie est finie ! Il n'y a pas eu de vainqueur !")
    
    choix_rejouer = input("Voulez-vous rejouer : O/N ?\n")
    jeu_continue = rejouer(choix_rejouer)
    
    


    
