# imports 
from chiffrer import *
from termcolor import colored
import os

# Création de la classe servant de support au programme

class Dechiffrer():
    
    # Méthode __init
    def __init__(self):
        pass

    # Méthode pour lancer le programme
    def run(self):
        self.main()
    
    # Méthode permettant d'initialiser le programme
    def main(self):
        
        # Affichage de la clé en ASCII et du menu principal
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
        """, "green"))
        
        self.ChoisirChiffrement()

    def ChoisirChiffrement(self):
        
        global chiffrement
        while True:
            chiffrement = input("Bienvenue dans ce programme de chiffrement et de déchiffrement de messages.\n\nVeuillez choisir une option de chiffrement: \n\n1) ROT13\n2) Code de César\n3) Code de Vigenère\n4) Carré de Polybe\n\n99) Menu Principal\n100) Informations\n101) Chiffrer\n\n").lower()
            
            if chiffrement == 101:
                chiffrerLesMessages = False
            
            else:
                chiffrement = input("Bienvenue dans ce programme de chiffrement et de déchiffrement de messages.\n\nVeuillez choisir une option de chiffrement: \n\n1) ROT13\n2) Code de César\n3) Code de Vigenère\n4) Carré de Polybe\n\n99) Menu Principal\n100) Informations\n101) Chiffrer\n\n").lower()