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

    message = input("Bienvenue dans ce programme de chiffrement de messages.\n\nVeuillez entrez le message à chiffrer.")

    if message == "":
        message = input("Bienvenue dans ce programme de chiffrement de messages.\n\nVeuillez entrez le message à chiffrer.")

if __name__ == '__main__':
    main()