#Desenvolvedores: Fernando Ferrarin e Lucas Blatt

from Funcoes import limpaLinha, novaPalavra, desenho, finalContador, criaLog

contadorFinal = 0
def jogo():
    limpaLinha(1)
    while True:
        desafiante = input("Insira o nome do Desafiante: ")
        competidor = input("Insira o nome do Competidor: ")
        if not desafiante or not competidor:
            limpaLinha(1)
            print("Estes dados não podem ficar em branco")
        else:
            break    

    limpaLinha(1)
    print("Desafiante", desafiante, "\nInsira algumas algumas informações: \n")

    while True:
        palavraChave = input("Insira a Palavra Chave: ")
        dica1 = input("\nInsira a Primeira Dica: ")
        dica2 = input("\nInsira a Segunda Dica: ")
        dica3 = input("\nInsira a Última Dica: ")
        if not palavraChave or not dica1 or not dica2 or not dica3:
            limpaLinha(1)
            print("Estes dados não podem ficar em branco")
        else:
            break    
    
    limpaLinha(1)
    novaPalavraChave = novaPalavra(palavraChave) 
    print("Sua Palavra Chave: ", ("*" * len(novaPalavraChave)))

    #-------------------------------------------->   Menus e Jogo
    contador = 0
    podePedirDica = True
    while True:
        print("\n(0) Jogar\n")
        print("\n(1) Sair\n")
        resposta = input()
        limpaLinha(1)

        if int(resposta) == 0:
            tentativas = 5
            listaDeAsteriscos = novaPalavra("*" * len(novaPalavraChave))
            print("Sua Palavra Chave: ", ("*" * len(novaPalavraChave)))
            limpaLinha(1)
            if tentativas > 0:
                    while True:    
                        print("\nSua Palavra Chave: ", listaDeAsteriscos)
                        print("\nVocê ainda têm:", tentativas, "Tentativas")
                        desenho(tentativas)
                        if contador < 3:
                            questionamento = input("\nQuer uma Dica? s Ou n? ")
                        else:
                            questionamento = "n"
                            
                        if questionamento == "n":
                            respostaDoJogo = input("\nChute uma letra: ")
                            if respostaDoJogo not in novaPalavraChave:
                                podePedirDica = True
                                if respostaDoJogo in listaDeAsteriscos:
                                    tentativas -= 1
                                else:
                                    limpaLinha(1)
                                    print("Errou!")
                                    tentativas -= 1
                                    
                                if tentativas <= 0: 
                                    break    
                            elif respostaDoJogo in novaPalavraChave:
                                podePedirDica = True
                                limpaLinha(1)
                                print("Acertou!")     
                                for letra in novaPalavraChave:
                                    for i in range (0, len(novaPalavraChave)):
                                        if respostaDoJogo == novaPalavraChave[i]:
                                            listaDeAsteriscos[i] = respostaDoJogo             
                        elif questionamento == "s":
                            limpaLinha(1)
                            if podePedirDica == True and contador == 0:
                                print("\nSua dica é: ", dica1)
                                contador += 1
                                podePedirDica = False
                            elif podePedirDica == True and contador == 1:
                                print("\nSua dica é: ", dica2)
                                contador += 1
                                podePedirDica = False
                            elif podePedirDica == True and contador == 2:
                                print("\nSua dica é: ", dica3)
                                contador += 1  
                                podePedirDica = False
                            else:
                                print("\nVocê não pode pedir mais Dicas ;-;")
                        else:
                            limpaLinha(1)
                            print("Caractere inserido inválido")
                            
                        if "*" not in listaDeAsteriscos:
                            break 
            elif tentativas <= 0:
                print(competidor, "Suas tentativas acabaram ;-;")
        elif int(resposta) == 1:
            quit()
        else:
            print("Dígito Inválido!") 
            quit()

        if "*" not in listaDeAsteriscos:
            break
        elif tentativas <= 0:
            break       
    contador = 0        
    if "*" not in listaDeAsteriscos:
        limpaLinha(1)
        criaLog(palavraChave, competidor, desafiante, listaDeAsteriscos, tentativas)
        print("Parabéns! O Competidor", competidor ,"venceu! :)")
        print("\nO Desafiante", desafiante, "perdeu ;-;")
        print("\nA Palavra Chave era:", palavraChave)
        print("\nVocê ainda tinha:", tentativas, "Tentativas")
        desenho(tentativas)    
    elif tentativas <= 0: 
        limpaLinha(1)
        criaLog(palavraChave, competidor, desafiante, listaDeAsteriscos, tentativas)
        print("Que Pena! O Competidor", competidor, "perdeu ;-;")
        print("\nO Desafiante", desafiante ,"venceu! :)!")
        print("\nA Palavra Chave era:", palavraChave)
        desenho(tentativas)

jogo()

while True:
    print("Você jogou", finalContador(contadorFinal), "partida(s)")
    print("\n(0) Jogar Novamente\n")
    print("(1) Sair\n")
    respostaFinal = input()
    
    if respostaFinal == "0":
        contadorFinal += 1
        jogo()
    elif respostaFinal == "1":
        limpaLinha(1)
        break
    else:
        limpaLinha(1)
        print("Valor inserido inválido\n")       