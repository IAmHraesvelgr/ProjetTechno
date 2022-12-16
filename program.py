# imports
from termcolor import colored
import os
import codecs

class Program():

    def run(self):
        Program.main(self)

    def main(self):

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
        message = input("Bienvenue dans ce programme de chiffrement de messages.\n\nVeuillez entrez le message à chiffrer (ce message doit uniquement être composé de lettres et ne doit pas contenir d'espaces) : \n\n").lower()

        while message == "" or any(char.isdigit() for char in message) or not message.isalpha():
            print(colored("ERREUR : Veuillez renseigner un message à chiffrer uniquement composé de lettres et ne doit pas contenir d'espaces.", 'red'))
            message = input("\nVeuillez entrez le message à chiffrer: \n").lower()
        
        Program.ChosirChriffrement(message)


    def ROT13(messageAChiffrer):
        
        messageChiffre = codecs.encode(messageAChiffrer, 'rot_13')
        return messageChiffre

    def CodeCesar(messageAChiffrer, decalage):
        
        decalage = int(decalage)
        messageChiffre = ""
        for i in range(len(messageAChiffrer)):
            char = messageAChiffrer[i]
            messageChiffre += chr((ord(char) + decalage - 96) % 26 + 96)
        return messageChiffre

    def CodeVigenère(messageAChiffrer, cle):

        cle = [ord(letter) - 97 for letter in cle]
        
        messageAChiffrer = str(messageAChiffrer).lower()

        tailleCle = len(cle)
        messageChiffre = ''

        for i in range(len(messageAChiffrer)):
            lettre = messageAChiffrer[i]
            c = cle[i % tailleCle]
            messageChiffre = messageChiffre + chr ((ord(lettre) - 97 + c ) % 26 + 97)
        
        return messageChiffre


    def CarreDePolybe(messageAChiffrer):
        
        pass

    # Fonction de choix du chiffrement
    def ChosirChriffrement(messageAChiffrer):
        
        global chiffrement
        chiffrement = input("\nVeuillez choisir une option de chiffrement: \n\n1) ROT13\n2) Code de César\n3) Code de Vigenère\n4) Carré de Polybe\n\n99) Menu Principal\n\n")

        if chiffrement == "1":
            
            print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.ROT13(messageAChiffrer), "green"))
            menuPrincipal = input("\n99) Menu Principal\n")
            chiffrement = ""
            while True:
                if menuPrincipal == "99":
                    
                    # Nettoyage de la fenêtre
                    try:
                        os.system("cls")
                    except:
                        os.system("clear")
                    
                    Program.run(Program)

                else:
                    print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.ROT13(messageAChiffrer), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")
                
        
        if chiffrement == "2":

            cle = input("Veuillez saisir une clé de chiffrement (celle-ci doit être composée d'un nombre entier compris entre 0 et 26):\n\n")
            
            while cle == "" or not cle.isdigit() or not cle.isdecimal() or int(cle) not in range(0, 26):
                print(colored("ERREUR : La clé de chiffrement doit être un nombre entier compris entre 0 et 26.\n\n", "red"))
                cle = input("Veuillez saisir une clé de chiffrement :\n\n")
            
            print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.CodeCesar(messageAChiffrer, cle), "green"))
            menuPrincipal = input("\n99) Menu Principal\n")
            chiffrement = ""
            
            while True:
                
                if menuPrincipal == "99":
                    
                    # Nettoyage de la fenêtre
                    try:
                        os.system("cls")
                    except:
                        os.system("clear")
                    
                    Program.run(Program)
                else:
                    print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.CodeCesar(messageAChiffrer,  cle), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")
        
        if chiffrement == "3":
            
            cle = input("Veuillez saisir une clé de chiffrement :\n\n")
            
            while cle == "" or not cle.isalpha() or any(char.isdigit() for char in cle):
                print(colored("ERREUR : La clé de chiffrement fournie n'est pas valide.\n\n", "red"))
                cle = input("Veuillez saisir une clé de chiffrement :\n\n")
            
            print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.CodeVigenère(messageAChiffrer, cle), "green"))
            menuPrincipal = input("\n99) Menu Principal\n")
            chiffrement = ""
            
            while True:
                
                if menuPrincipal == "99":
                    
                    # Nettoyage de la fenêtre
                    try:
                        os.system("cls")
                    except:
                        os.system("clear")
                    
                    Program.run(Program)
                else:
                    print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.CodeVigenère(messageAChiffrer, cle), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")
        
        if chiffrement == "4":
            
            Program.CarreDePolybe(messageAChiffrer)
            chiffrement = ""
        
        if chiffrement == "99":
            
            chiffrement = ""

            # Nettoyage de la fenêtre
            try:
                os.system("cls")
            except:
                os.system("clear")
                
            Program.run()
        
        else:
            print(colored("ERREUR : Option de chiffrement non-renseignée.", "red"))
            Program.ChosirChriffrement(message)