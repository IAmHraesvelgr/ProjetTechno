# imports
from termcolor import colored
import os
import codecs

class Program():

    def run(self):
        Program.main(self)

    def main(self):
        
        # Fonction Main
        os.system("mode con cols=85 lines=30")

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
        message = input("Bienvenue dans ce programme de chiffrement de messages.\n\nVeuillez entrez le message à chiffrer: \n")

        while message == "":
            print(colored("ERREUR : Veuillez renseigner un message à chiffrer.", 'red'))
            message = input("\nVeuillez entrez le message à chiffrer: \n")
        
        Program.ChosirChriffrement(message)


    def ROT13(messageAChiffrer):
        messageChiffre = codecs.encode(messageAChiffrer, 'rot_13')
        return messageChiffre

    def CodeCesar(messageAChiffrer, s):
        s = int(s)
        resultat = ""
        for i in range(len(messageAChiffrer)):
            char = messageAChiffrer[i]
            resultat += chr((ord(char) + s - 96) % 26 + 96)
        return resultat

    def CodeVigenère(messageAChiffrer):
        pass

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

            decalage = input("Veuillez saisir une clé de chiffrement :\n")
            while decalage == "" or not decalage.isdigit() or not decalage.isdecimal():
                print(colored("ERREUR : La clé de chiffrement doit être un nombre entier.\n", "red"))
                decalage = input("Veuillez saisir une clé de chiffrement :\n")
            print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.CodeCesar(messageAChiffrer, decalage), "green"))
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
                    print("\n", colored("[*]", "blue"), "Le message chiffré est" , colored(Program.CodeCesar(messageAChiffrer,  decalage), "green"))
                    menuPrincipal = input("\n99) Menu Principal\n")
        
        if chiffrement == "3":
            
            Program.CodeVigenère(messageAChiffrer)
            chiffrement = ""
        
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