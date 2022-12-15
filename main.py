# imports
from program import Program
from console.utils import set_title
import os         

os.system("mode con: cols=130 lines=35")
set_title("Programme de chiffrement")

app = Program()

# Lancement du Programme
while True:
    app.run()