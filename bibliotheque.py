### Développer une application python permettant la gestion d’une bibliothèque contenant des livres et leurs auteurs.

### Contrainte : utiliser au maximum les classes, héritages et méthodes.

class Livre():
    
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

class Bibliotheque():

    def __init__(self):
        #Initialisation d'une mini bibliothèque 
        self.bibliotheque = [Livre("Le Silence de la mer","Vercors"),
                            Livre("La communauté de l'anneau","Tolkien"),
                            Livre("Les deux tours","Tolkien"),
                            Livre("Le retour du roi","Tolkien"),
                            Livre("Le vieil homme et la mer","Hemingway"),]

    def ajouter_livre(self):
        print("Vous avez choisi d'ajouter un livre. Veuillez rentrer son titre puis son auteur!\n")
        titre_livre = input("Titre du livre à ajouter : ")
        auteur_livre = input("Nom de l'auteur du livre à ajouter : ")
        
        self.bibliotheque.append(Livre(titre_livre, auteur_livre))
        
        print("Votre livre a été ajouté à la bibliothèque !")
        
    def rechercher_auteur_de_livre(self):
        print("Vous recherchez l'auteur d'un livre donné. Veuillez tapez le titre du livre en question !")
        titre_livre = input("Titre du livre : ")
        
        for livre in self.bibliotheque:
            if livre.titre == titre_livre:
                print(f"\nL'auteur de '{titre_livre}' est {livre.auteur}.")
    
    def rechercher_livres_par_auteur(self):
        print("Vous recherchez tous les livres d'un auteur. Veuillez tapez le nom de l'auteur !")
        auteur_livre = input("Nom de l'auteur : ")
          
        liste_livres = [livre.titre for livre in self.bibliotheque if livre.auteur == auteur_livre]
        print(f"{auteur_livre} est l'auteur des livres suivants dans votre bibliothèque: {', '.join(liste_livres)}.")


#initialisation de la bibliothèque
macollection = Bibliotheque()

while True:    
    print("\n\nChoisissez ce que vous souhaitez faire : \n \
          1. Ajouter un livre et son auteur\n \
          2. Rechercher l’auteur d’un livre donné \n \
          3. Rechercher les livres d’un auteur donné\n\n \
          \
          \nTapez 'q' pour quitter le programme")

    user_input = input("Faites votre choix [1-3] :  ")

    if user_input == "1":
        macollection.ajouter_livre()
    elif user_input == "2":
        macollection.rechercher_auteur_de_livre()
    elif user_input == "3":
        macollection.rechercher_livres_par_auteur()
    elif user_input == "q":
        print("\nA bientot.")
        break
    else:
        print("Votre choix est invalide. Veuillez recommencer !")
