from values_en import FREQUENCIAS
from values_en import ALFABETO
def decifraTexto(chave, txtCifrado):
    txtClaro = ""
    offset = 0
    for i in range(len(txtCifrado)):
        offset = ord(txtCifrado[i]) - ord(chave[i % len(chave)])
        if offset < 0:
            offset += len(ALFABETO)
        txtClaro += chr(offset + 97)
    return txtClaro