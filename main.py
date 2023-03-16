# imports
from chiffrer import Chiffrer
import console.utils
from os import *

# Mise en place de la console
console.utils.clear()
console.utils.set_title("Programme de chiffrement")

# Lancement de l'application
app = Chiffrer()
app.run()