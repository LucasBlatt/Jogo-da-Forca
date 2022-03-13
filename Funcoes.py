import os

def limpaLinha(x):
    x * os.system("cls")

def novaPalavra(palavraChave):
    newPalavraChave = []
    for i in range(0, len(palavraChave)):
        newPalavraChave.append(palavraChave[i])
        i += 1
    return newPalavraChave

def desenho(tentativas):
    if tentativas == 5:
        print('+-----+   ')
        print('|     |   ')
        print('|         ')
        print('|         ')
        print('|         ')
        print('|         ')
        print('|_________')
    elif tentativas == 4:
        print('+-----+   ')
        print('|     |   ')
        print('|     O   ')
        print('|         ')
        print('|         ')
        print('|         ')
        print('|_________')
    elif tentativas == 3:
        print('+-----+   ')
        print('|     |   ')
        print('|     O   ')
        print('|     |   ')
        print('|         ')
        print('|         ')
        print('|_________')
    elif tentativas == 2:
        print('+-----+   ')
        print('|     |   ')
        print('|     O   ')
        print('|    /|   ')
        print('|         ')
        print('|         ')
        print('|_________')
    elif tentativas == 1:
        print('+-----+   ')
        print('|     |   ')
        print('|     O   ')
        print('|    /|   ')
        print('|     |   ')
        print('|    /    ')
        print('|_________')
    elif tentativas == 0:
        print('+-----+   ')
        print('|     |   ')
        print('|     O   ')
        print('|    /|\\ ')
        print('|     |   ')
        print('|    / \\ ')
        print('|_________')  

def finalContador(contadorFinal):
    contadorFinal += 1
    return contadorFinal 

def criaLog(palavraChave, competidor, desafiante, listaDeAsteriscos, tentativas):
    arquivo = open("LogJogoDaForca.txt", "w")
    arquivo.write("Palavra: ")
    arquivo.write(palavraChave)
    if "*" not in listaDeAsteriscos:
        arquivo.write("\nVencedor: ")
        arquivo.write(competidor)
        arquivo.write("\nPerdedor: ")
        arquivo.write(desafiante)
    elif tentativas <= 0:
        arquivo.write("\nVencedor: ")
        arquivo.write(desafiante)
        arquivo.write("\nPerdedor: ")
        arquivo.write(competidor)
    arquivo.close()