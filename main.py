# imports
from termcolor import colored
import os
import codecs

# Fonction Main
def main():
    
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

    message = input("Bienvenue dans ce programme de chiffrement de messages.\n\nVeuillez entrez le message à chiffrer: \n")

    while message == "":
        print(colored("ERREUR : Veuillez renseigner un message à chiffrer.", 'red'))
        message = input("\nVeuillez entrez le message à chiffrer: \n")
    
    chiffrement = input("\nVeuillez choisir une option de chiffrement: \n\n1) ROT13\n2) Code de César\n3) Code de Vigenère\n4) Carré de Polybe\n\n99) Menu Principal\n\n")

    if chiffrement == "1":
        
        print("\n" + ROT13(message))
        message = ""
        menuPrincipal = input("\n99) Menu Principal\n")
        while True:
            if menuPrincipal == "99":
                main()
            
    
    if chiffrement == "2":
        
        print("\n" + CodeCesar(message))
        message = ""
        menuPrincipal = input("\n99) Menu Principal\n")
        while True:
            if menuPrincipal == "99":
                main()
    
    if chiffrement == "3":
        
        CodeVigenère(message)
        message = ""
    
    if chiffrement == "4":
        
        CarreDePolybe(message)
        message = ""
    
    if chiffrement == "99":
        message = ""

def ROT13(message):
    messageChiffre = codecs.encode(message, 'rot_13')
    return messageChiffre

def CodeCesar(message):
    pass

def CodeVigenère(message):
    pass

def CarreDePolybe(message):
    pass

# Lancement du Programme
if __name__ == '__main__':
    main()