from termcolor import colored

def main():
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

if __name__ == '__main__':
    main()