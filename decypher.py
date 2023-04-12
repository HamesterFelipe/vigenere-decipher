from calculate_length import descobreTamanhoChave
from decypher_key import decifraChave
from decypher_text import decifraTexto

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def write_file(texto):
    with open("data/result.txt", "w") as arquivo:
        arquivo.write(texto)

filename = 'data/cipher.txt'
ciphertext = read_file(filename)
key_length = descobreTamanhoChave(ciphertext)
print("Comprimento da chave:", key_length)
decyphered_key = decifraChave(key_length, ciphertext)
print("Chave:", decyphered_key)
textoDecifrado = decifraTexto(decyphered_key, ciphertext)
print("Texto decifrado: \n", textoDecifrado)
write_file(textoDecifrado)

