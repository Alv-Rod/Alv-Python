#Algoritmos
#Alvaro Rodrigues
#____________________________
#algoritmo de aposentadoria
##analise de tempo de contribuição, de idade, deficiencia e possibilidades de aposentadoria
import os, time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("Menu Principal\n____________________________\nEscolha a opção desejada:")


    print("Instituto Nacional do Seguro Social - INSS\n____________________________\nAposentadoria")
    input("Pressione qualquer botão para continuar... ")
    clear()
    print("Insira os dados do contribuinte\n____________________________")
    name = str(input("Insira seu nome: "))

    while True:
        try:
            age = int(input("Insira sua idade: "))
            break
        except ValueError:
            input("Erro... Insira sua idade em números\nPressione qualquer botão...")
            continue

    while True:
        try:
            isInvalidQuestion = int(input("O contribuinte possui alguma deficiencia? (1 - Sim/2 - Não): "))
        except ValueError:
            input("Erro... Resposta precisa ser 1 - Sim ou 2 - Não\nPressione qualquer botão...")
            continue
        if isInvalidQuestion == 1:
            isInvalid = True
            break
        elif isInvalidQuestion > 2:
            input("Erro... Resposta precisa ser 1 - Sim ou 2 - Não\nPressione qualquer botão...")
            continue
        else:
            isInvalid = False
            break

    while True:
        try:
            contribution = int(input("Finalmente, insira seu tempo de contribuição em anos: "))
            break
        except ValueError:
            input("Erro... Insira seu tempo de contribuição em números\nPressione qualquer botão...")
            continue
    clear()
    print("Os dados do contribuinte estão sendo processados, aguarde...")
    time = 0
    while time < 3:
        print("Aguarde...")
        time.sleep(1)
        time += 1

    canRetire = False

    while canRetire == False:
        if isInvalid == True:
            canRetire = True
        elif age >= 85:
            canRetire = True
        elif contribution >= 35:
            canRetire = True
        else:
            input(f"Foi encontrado que o contribuinte {name} não se encontra em situação valida para aposentar.\
                \nPressione qualquer botão para retornar ao menu principal... ")
            
    if canRetire == True:
        input(f"O contribuinte {name} de idade {age} se encontra em situação de aposentadoria.\
            \nPressione qualquer botão para retornar ao menu principal")
    continue
