# imports
from program import Chiffrer
from console.utils import set_title
import os         

# Mise en place de la console
os.system("mode con: cols=130 lines=35")
set_title("Programme de chiffrement")


# Création d'une intance de la classe Programme
app = Chiffrer()

# Lancement du Programme
while True:
    app.run()