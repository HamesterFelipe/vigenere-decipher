def descobreTamanhoChave(txt_cifrado):
    distancias_caracteres = [0] * 1000
    tam_palavra = 15
    cont = 0
    for i in range(len(txt_cifrado) - tam_palavra):
        cmp_caracteres = txt_cifrado[i:i+tam_palavra]
        for x in range(i + 1, len(txt_cifrado) - tam_palavra):
            if (cmp_caracteres == txt_cifrado[x:x+tam_palavra]) and (cont < len(distancias_caracteres)):
                distancias_caracteres[cont] = x - i
                cont += 1
    return buscaComMdc(distancias_caracteres)


def buscaComMdc(distancias_caracteres):
    tam_chave = mdc(distancias_caracteres[0], distancias_caracteres[1])
    if len(distancias_caracteres) > 2:
        for i in range(2, len(distancias_caracteres)):
            tam_chave = mdc(tam_chave, distancias_caracteres[i])
    return tam_chave


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)