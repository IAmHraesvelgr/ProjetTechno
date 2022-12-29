# imports
from chiffrer import *
from dechiffrer import *
from console.utils import set_title
import os         

# Mise en place de la console
os.system("mode con: cols=130 lines=35")
set_title("Programme de chiffrement")


# Création d'une intance de la classe Programme
chiffrer = Chiffrer()
dechiffrer = Dechiffrer()

# Lancement du Programme
while True:
    while chiffrer.chiffrerLesMessages == True:
        chiffrer.run()

    while chiffrer.chiffrerLesMessages == False:
        dechiffrer.run()