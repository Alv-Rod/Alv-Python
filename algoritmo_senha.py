#algoritmo senha
#alvaro
import random
senhaCorreta = random.randint(0, 10)
senhaUsuario = 0
print(senhaCorreta)
while senhaUsuario != senhaCorreta:
    senhaUsuario = int(input("Insira sua senha... "))
    if senhaUsuario != senhaCorreta:
        print("Senha incorreta, tente novamente... ")
print("senha correta.")
print("fim")
