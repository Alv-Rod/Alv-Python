#Dia de folga, opções:
##ficar em casa e pedir lanche, 3 opções
##ir ao cinema e escolher filme, algoritmo apenas mostra o filme
##estadio ver um jogo, 3 opções de jogo, mostra apenas o jogo
##Alvaro Rodrigues, 2M

def validacao_inteiro(insert):
    while True:
        try:
            value = int(input(insert))
        except ValueError:
            print("Insira um numéro válido")
            continue
        return value

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print("_______________________\nDia de Folga\n_______________________\nOpções:")
print("\n1 - Ficar em casa\n2 - Cinema\n3 - Futebol")

opcaoInicial = validacao_inteiro("\nInsira a opção: ")

match opcaoInicial:
    case 1:
        print("\nFicar em casa\n_______________________")
        lancheQuestao = str(input("\nPedir lanche? (Y/N): "))
        if lancheQuestao == "Y":
            print("\nEscolha o lanche que deseja, opções: \n1 - Hambúrguer\n2 - Pizza\n3 - Bolinho de Bacalhau")

            lancheOpcao = validacao_inteiro("\nInsira a opção: ")

            match lancheOpcao:
                case 1:
                    print("\nPedido Confirmado. tempo de espera aproximadamente 60 minutos :D")
                case 2:
                    print("\nPedido Confirmado. tempo de espera aproximadamente 80 minutos :D")
                case 3:
                    print("\nPedido Confirmado. tempo de espera aproximadamente 40 minutos :D")
                case _:
                    print("Insira uma opção válida")
        elif lancheQuestao == "N":
            print("Boa estadia em sua casa.")
        else:
            print("Insira Y (sim) ou N(não). Finalizando aplicação.")
    case 2:
        print("\nCinema\n_______________________\nEscolha o filme que deseja, opções: \n1 - Sonic 3 o Filme\n2 - Vingadores 76\n3 - Arcane: o Filme")
        cineOpcao = validacao_inteiro("\nInsira a opção: ")
        match  cineOpcao:
            case 1:
                    print("\nIngresso para Sonic 3: o Filme comprado")
            case 2:
                    print("\nIngresso para Vingadores 76 comprado")
            case 3:
                    print("\nIngresso para Arcane: O Filme comprado")
            case _:
                    print("Insira uma opção válida")
    case 3:
        print("\nFutebol\n_______________________\nEscolha o jogo:\nBrasil x Japão\nBrasil x Russia\nBrasil x Brasil")
        futOpcao = validacao_inteiro("\nInsira a opção: ")
        match futOpcao:
            case 1:
                    print("\nIngresso para o jogo do Brasil x Japão comprado")
            case 2:
                    print("\nIngresso para o jogo do Brasil x Rússia comprado")
            case 3:
                    print("\nIngresso para o jogo do Brasil x Brasil comprado")
            case _:
                    print("Insira uma opção válida")
    case _:
        print("\nOpção Invalida, insira um número de 1 à 3.")
        


