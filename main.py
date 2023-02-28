# imports
from chiffrer import Chiffrer
import console.utils
from os import *
from curses import *

# Mise en place de la console
console.utils.clear()
terminal_size((150, 35))
console.utils.set_title("Programme de chiffrement")

# Lancement de l'application
app = Chiffrer()
app.run(app)