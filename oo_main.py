from oo_rubrica import Comando_stampa_completa, Rubrica
from oo_rubrica import BrowserRubrica

rubrica = Rubrica()

br = BrowserRubrica(rubrica)
#Comando_stampa_completa(rubrica).exec()

while True:
    comando = br.getComando()
    comando.exec()
    if comando.is_exit:
        break
