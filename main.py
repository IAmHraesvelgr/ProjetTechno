# imports
from termcolor import colored
import os

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

# Lancement du Programme
if __name__ == '__main__':
    main()