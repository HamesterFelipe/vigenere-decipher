from values_en import FREQUENCIAS
from values_en import ALFABETO


def decifraChave(tamChave, txt):
    mtzTextCifrado = organizaTxt(tamChave, txt)
    chave = ""

    for i in range(tamChave):
        colunaTxt = ""
        for j in range(len(mtzTextCifrado) - 1):
            colunaTxt += mtzTextCifrado[j][i]
        chave += encontraCharChave(colunaTxt)

    return chave

def organizaTxt(tamChave, cifrado):
    qtdLinhas = len(cifrado) // tamChave
    index = 0
    mtr = {}
    for i in range(qtdLinhas):
        mtr[i] = []
        for j in range(tamChave):
            if index < len(cifrado):
                mtr[i].append(cifrado[index])
                index += 1
    return mtr

def encontraCharChave(colunaTxt):
    colunaAux = colunaTxt
    quiQuadrado = {}

    for i in range(1, len(ALFABETO)):
        freqLetras = calculaFrequenciaLetra(colunaAux)
        qui = 0
        for j in range(len(ALFABETO)):
            freqEsperada = FREQUENCIAS[j] * len(colunaAux)
            qui += ((freqLetras[ALFABETO[j]] - freqEsperada) ** 2) / freqEsperada

        quiQuadrado[ALFABETO[i - 1]] = qui
        colunaAux = deslocaLetras(ALFABETO[i], colunaTxt)

    # a letra de menor valor encontrada é a resposta.
    return encontraLetraChave(quiQuadrado)

def calculaFrequenciaLetra(col):
    freqLetras = {}
    
    for letra in ALFABETO:
        freqLetras[letra] = 0
    
    for letra in col:
        freqLetras[letra] = freqLetras.get(letra, 0) + 1
    
    return freqLetras

def deslocaLetras(letra, colunaTxt):
    print(letra + "-" + colunaTxt)
    
    resultado = ""
    
    # elabora coluna da tabela de vigenere apartir do caractere
    colunaVig = montaColunaTabelaVigenere(letra)
    
    for i in range(len(colunaTxt)):
        for j in range(len(colunaVig)):
            if colunaVig[j] == colunaTxt[i]:
                index = j
                break
        
        resultado += ALFABETO[index]
    
    print("RESULTADO: " + resultado)
    
    return resultado

def montaColunaTabelaVigenere(c):
    ac = []
    k = ord(c)
    
    for i in range(len(ALFABETO)):
        ac.append(chr(k))
        
        if k == 122:
            k = 97
        else:
            k += 1
    
    return ac

def encontraLetraChave(quiQuadrado):
    minimo = float("inf")
    letra = None
    
    for k in quiQuadrado.keys():
        if quiQuadrado[k] < minimo:
            letra = k
            minimo = quiQuadrado[k]
    
    return letra