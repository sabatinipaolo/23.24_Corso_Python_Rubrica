from oo_rubrica import Rubrica
from oo_rubrica import BrowserRubrica

rubrica = Rubrica()

br = BrowserRubrica(rubrica)

# br.lista()

# print (type (rubrica.listaContatti()) )

while True:
    comando = br.getComando()
    comando.exec()
    if comando.is_exit:
        break
