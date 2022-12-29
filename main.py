# imports
from chiffrer import *
from console.utils import set_title
import os         

# Mise en place de la console
os.system("mode con: cols=150 lines=35")
set_title("Programme de chiffrement")


# Création d'une intance de la classe Chiffrer
chiffrer = Chiffrer()

chiffrer.run()