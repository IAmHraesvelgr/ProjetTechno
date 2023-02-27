# imports
from chiffrer import Chiffrer
from console.utils import set_title
from os import *

# Mise en place de la console
Chiffrer.clear()

if name == "nt":
    _ = system("mode con: cols=150 lines=35")
else:
    system("resize -s 35 150")

set_title("Programme de chiffrement")

# Lancement de l'application
Chiffrer.run()