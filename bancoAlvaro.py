#algoritmo de Banco
#Alvaro Rodrigues, 2M

def validacao_inteiro(insert):
    while True:
        try:
            value = int(input(insert))
        except ValueError:
            print("Insira um valor válido")
            continue
        return value

import os
from time import sleep

def clear():
    os.system('cls')
clear()

#começo;banco
print("Banco Central\n______________________")
while True:
    try:
        cartaoPedido = str(input("Seu cartão está inserido? (S/N): "))
    except ValueError:
        print("Use S ou N")
        continue
    if cartaoPedido == "S":
        break
    else:
        ("\nInsira seu cartão para continuar...")
        clear()
        continue
clear()

print("\nQual operação deseja?\n______________________\n1 - Saque\n2 - Depósito\n3 - Saldo\n4 - Pagamento")

menuOperacao = validacao_inteiro("Insira a opção: ")
match menuOperacao:
    case 1:
        print("\nSaque\n______________________\nNotas disponiveis: R$10, R$50, R$100\nValor:\n1 - R$20,00\n2 - R$50,00\n3 - R$100,00\n4 - R$200,00")
        opcaoSaque = validacao_inteiro("Insira a opção: ")
        while True:
            try:
                cpfUsuario = float(input("Insira seu cpf (sem pontos e traços): "))
            except ValueError:
                print("Por favor insira seu cpf usando apenas números...")
                continue
            if cpfUsuario > 99999999999:
                print("CPF ínvalido, tente novamente...")
                continue
            else:
                break
        print("\nSaque aprovado. Aguarde...")
        sleep(3)
        print("\nRetire seu dinheiro. Pressione qualquer botão para terminar a operação.")
        input()
    case 2:
        while True:
            try:
                depositoValor = int(input("Insira o valor a ser depositado: "))
            except ValueError:
                print("Insira um valor valido...")
                continue
            if depositoValor < 50:
                print("Depositos validos apenas apartir de R$50,00...")
                continue
            else:
                break
        print(f"\nDeposito de {depositoValor} validado. Insira o envelope...")
        sleep(1)
        input("Envelope Inserido? Pressione qualquer botão para continuar...")
        sleep(2)
        print("\nOperação completa com exito.")
    case 3:
        saldo = 1024
        while True:
            try:
                cpfUsuario = float(input("Insira seu cpf (sem pontos e traços): "))
            except ValueError:
                print("Por favor insira seu cpf usando apenas números...")
                continue
            if cpfUsuario > 99999999999 or cpfUsuario < 10000000000:
                print("CPF ínvalido, tente novamente...")
                continue
            else:
                break
        print("\nValidando usuario.")
        sleep(1)
        print(f"\nSeu saldo é de R${saldo}.")
        input("Operação concluída. Pressione qualquer botão...")
    case 4:
        #dados das contas
        dictContaAgua = {
            "valor":53,
            "data":"22/11",
            "validade": "22/12"

        }
        dictContaLuz = {
            "valor":144,
            "data":"22/11",
            "validade": "22/12"

        }
        dictContaInternet = {
            "valor":240,
            "data":"22/11",
            "validade": "22/12"

        }
        print("Contas disponiveis:\n1 - Água\n2 - Luz\n3 - Internet")
        opcaoPagamento = validacao_inteiro("Insira a opção desejada: ")
        
        match opcaoPagamento:
            case 1: 
                print(f"\nConta de água:\nReferente à: {dictContaAgua['data']}\nValidade: {dictContaAgua['validade']}\nValor: {dictContaAgua['valor']}")
            case 2:
                print(f"\nConta de luz:\nReferente à: {dictContaLuz['data']}\nValidade: {dictContaLuz['validade']}\nValor: {dictContaLuz['valor']}")
            case 3:
                print(f"\nConta de internet:\nReferente à: {dictContaInternet['data']}\nValidade: {dictContaInternet['validade']}\nValor: {dictContaInternet['valor']}")
            case _:
                print("Insira uma opção válida...")

        while True:
            try:
                pagarConfirmação = str(input("Pagar? (S/N)... "))
            except ValueError:
                print("Use S ou N")
                continue
            if pagarConfirmação == "N":
                input("Operação cancelada. Pressione qualquer botão...")
            else:
                break
        print("\nPagamento em processo...")
        sleep(1)
        input("\nOperação concluida com éxito. Pressione qualquer botão para continuar...")
        exit()
        
        

    
                
                    

