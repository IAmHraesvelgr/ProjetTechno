# imports
from termcolor import *
from os import *
import string
import console.utils

# Création de la classe servant de support au programme


class Chiffrer():

    # Constructeur (vide)
    def __init__(self):
        pass

    def run(self):
        """Méthode pour lancer le programme."""
        self.main()

    def main(self):
        """Méthode princiaple du programme"""

        # Affichage de la clé en Unicode et du menu principal
        print(colored("""                                                                  
                                                            ████░░░░░░████      
                                                        ██░░░░░░░░░░██████    
                                                        ██░░░░██████████░░███  
                                                        ██░░░░██      ██░░███  
        ████████████████████████████████████████████████░░░░██          ██░░░░██
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          ██░░░░██
          ██░░░░██░░░░██░░░░████████████████████████████░░░░██          ██░░░░██
            ████  ████  ████                            ██░░░░██      ██░░░░██  
                                                        ██░░░░██████████░░░░██  
                                                        ██░░░░░░░░░░░░░░██    
                                                            ████░░░░░░████      
                                                                ██████          
        """, "yellow"))

        global message

        message = input("Bienvenue dans ce programme de chiffrement de messages.\n\nVeuillez entrez le message à chiffrer : ce message doit uniquement être composé de lettres et ne doit pas contenir d'espaces : \n\n").lower()

        while message == any(char.isdigit() for char in message) or not message.isalpha():

            print(colored("ERREUR : Veuillez renseigner un message à chiffrer uniquement composé de lettres et ne contenant pas d'espaces.", 'red'))
            message = input(
                "\nVeuillez entrez le message à chiffrer: \n\n").lower()

        self.ChoisirChiffrement(message)

    def ROT13(self, messageAChiffrer):
        """Méthode permettant de chiffrer le message fourni en ROT-13"""

        alphabet = string.ascii_lowercase
        messageChiffre = ""

        for char in messageAChiffrer:
            messageChiffre += alphabet[(alphabet.find(char) + 13) % 26]

        return messageChiffre

    def CodeCesar(self, messageAChiffrer, decalage):
        """Méthode permettant de chiffrer le message fourni en César grâce à la clé fournie"""

        decalage = int(decalage)
        alphabet = string.ascii_lowercase
        alphabet_decale = alphabet[decalage:] + alphabet[:decalage]
        messageChiffre = str.maketrans(alphabet, alphabet_decale)
        return messageAChiffrer.translate(messageChiffre)

    def CodeVigenère(self, messageAChiffrer, cle):
        """Méthode permettant de chiffrer le message fourni en Vigenère grâce à la clé fournie"""

        cle = [ord(letter) - 97 for letter in cle]

        messageAChiffrer = str(messageAChiffrer).lower()

        tailleCle = len(cle)
        messageChiffre = ''

        for i in range(len(messageAChiffrer)):
            lettre = messageAChiffrer[i]
            c = cle[i % tailleCle]
            messageChiffre = messageChiffre + \
                chr((ord(lettre) - 97 + c) % 26 + 97)

        return messageChiffre

    def CarreDePolybe(self, messageAChiffrer):
        """Méthode pour chiffrer avec le carré de Polybe (le carré par défaut)
        A B C D E
        F G H I,j K
        L M N O P
        Q R S T U
        V W X Y Z
        """

        messageChiffre = ""

        for char in messageAChiffrer:

            ligne = int((ord(char) - ord('a')) / 5) + 1

            col = ((ord(char) - ord('a')) % 5) + 1

            if char == 'k':

                ligne = ligne - 1
                col = 5 - col + 1

            elif ord(char) >= ord('j'):

                if col == 1:
                    col = 6
                    ligne = ligne - 1

                col = col - 1

            messageChiffre = messageChiffre + str(ligne) + str(col)

        return messageChiffre

    def ChoisirChiffrement(self, messageAChiffrer):
        """Méthode pour choisir le moyen de chiffrement employé"""

        global chiffrement
        chiffrement = input(
            "\nVeuillez choisir une option de chiffrement: \n\n1) ROT13\n2) Code de César\n3) Code de Vigenère\n4) Carré de Polybe\n\n99) Menu Principal\n100) Informations\n\n")

        if chiffrement == "1":

            print("\n", colored("[*]", "blue"), "Le message chiffré est",
                  colored(self.ROT13(messageAChiffrer), "green"))
            menuPrincipal = input("\n99) Menu Principal\n")
            chiffrement = ""

            while True:

                if menuPrincipal == "99":

                    # Nettoyage de la fenêtre
                    console.utils.clear()
                    self.run()

                else:
                    print("\n", colored("[*]", "blue"), "Le message chiffré est",
                          colored(self.ROT13(messageAChiffrer), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")

        if chiffrement == "2":

            cle = input(
                "Veuillez saisir une clé de chiffrement (celle-ci doit être composée d'un nombre entier compris entre 0 et 26):\n\n")

            while cle == "" or not cle.isdigit() or not cle.isdecimal() or int(cle) not in range(0, 26):
                print(colored(
                    "ERREUR : La clé de chiffrement doit être un nombre entier compris entre 0 et 26.\n\n", "red"))
                cle = input("Veuillez saisir une clé de chiffrement :\n\n")

            print("\n", colored("[*]", "blue"), "Le message chiffré est",
                  colored(self.CodeCesar(messageAChiffrer, cle), "green"))
            menuPrincipal = input("\n99) Menu Principal\n")
            chiffrement = ""

            while True:

                if menuPrincipal == "99":

                    # Nettoyage de la fenêtre
                    console.utils.clear()
                    self.run()

                else:
                    print("\n", colored("[*]", "blue"), "Le message chiffré est",
                          colored(self.CodeCesar(messageAChiffrer, cle), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")

        if chiffrement == "3":

            cle = input("Veuillez saisir une clé de chiffrement :\n\n")

            while cle == "" or not cle.isalpha() or any(char.isdigit() for char in cle):
                print(
                    colored("ERREUR : La clé de chiffrement fournie n'est pas valide.\n\n", "red"))
                cle = input("Veuillez saisir une clé de chiffrement :\n\n")

            print("\n", colored("[*]", "blue"), "Le message chiffré est",
                  colored(self.CodeVigenère(messageAChiffrer, cle), "green"))
            menuPrincipal = input("\n99) Menu Principal\n")
            chiffrement = ""

            while True:

                if menuPrincipal == "99":

                    # Nettoyage de la fenêtre
                    console.utils.clear()
                    self.run()

                else:
                    print("\n", colored("[*]", "blue"), "Le message chiffré est",
                          colored(self.CodeVigenère(messageAChiffrer, cle), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")

        if chiffrement == "4":

            print("\n", colored("[*]", "blue"), "Le message chiffré est",
                  colored(self.CarreDePolybe(messageAChiffrer), "green"))
            menuPrincipal = input("\n99) Menu Principal\n")
            chiffrement = ""

            while True:

                if menuPrincipal == "99":

                    # Nettoyage de la fenêtre
                    console.utils.clear()
                    self.run()

                else:
                    print("\n", colored("[*]", "blue"), "Le message chiffré est",
                          colored(self.CarreDePolybe(messageAChiffrer), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")

        if chiffrement == "99":

            chiffrement = ""

            # Nettoyage de la fenêtre
            console.utils.clear()
            self.run()

        if chiffrement == "100":

            chiffrement = ""

            print("\n1) Le chiffrement ROT13 est une méthode de chiffrement dans laquelle chaque lettre à chiffrer est décalée de 13 lettres par rapport à son emplacement initial. Exemple : a = n en ROT13.")
            print("\n2) Le code de César est une méthode de chiffrement dans laquelle chaque lettre à chiifrer est décalée du nombre de lettres correspondant à la clé par rapport à son emplacement initial. Exemple : a = d pour une clé '3' en code de César.")
            print("\n3) Le code Vigenère est une méthode de chiffrement dans laquelle chaque lettre à chiffrer est remplacée par différentes lettres en fonction de la clé fournie. Exemple : a = c pour une clé 'cle' en code de Vigenère.")
            print("\n4) Le carré de Polybe est une méthode de chiffrement dans laquelle chaque lettre de l'alphabet est placée dans un tableau (un cube) de 5 x 5 = 25 cases (par convention, le i et le j sont placés dans la même case à cause du manque de place). Ensuite chaque lettre du message est remplacée par les coordonées de cette lettre dans le carré. Exemple : a = 11 avec le carré de Polybe\n")

            menuPrincipal = input("\n99) Menu Principal\n")

            while True:

                if menuPrincipal == "99":

                    # Nettoyage de la fenêtre
                    console.utils.clear()
                    self.run()

                else:
                    print("\n1) Le chiffrement ROT13 est une méthode de chiffrement dans laquelle chaque lettre à chiffrer est décalée de 13 lettres par rapport à son emplacement initial. Exemple : a = n en ROT13.")
                    print("\n2) Le code de César est une méthode de chiffrement dans laquelle chaque lettre à chiifrer est décalée du nombre de lettres correspondant à la clé par rapport à son emplacement initial. Exemple : a = d pour une clé '3' en code de César.")
                    print("\n3) Le code Vigenère est une méthode de chiffrement dans laquelle chaque lettre à chiffrer est remplacée par différentes lettres en fonction de la clé fournie. Exemple : a = c pour une clé 'cle' en code de Vigenère.")
                    print("\n4) Le carré de Polybe est une méthode de chiffrement dans laquelle chaque lettre de l'alphabet est placée dans un tableau (un cube) de 5 x 5 = 25 cases (par convention, le i et le j sont placés dans la même case à cause du manque de place). Ensuite chaque lettre du message est remplacée par les coordonées de cette lettre dans le carré. Exemple : a = 11 avec le carré de Polybe\n")
                    menuPrincipal = input("\n99) Menu Principal\n")

        else:
            print(colored("ERREUR : Option de chiffrement non-renseignée.", "red"))
            self.ChoisirChiffrement(message)
