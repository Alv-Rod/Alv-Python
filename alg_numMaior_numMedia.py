#algoritmo, numero maior, finaliza no 0

print("Numero maior.")
a = int(input("Digite 5 números inteiros positivos:\na: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))

if a or b or c or d or e == 0: quit

if a > b and c and d and e:
    maior = a
elif b > a and b > c and b > d and b > e:
    maior = b
elif c > a and c > b and c > d and c > e:
    maior = c
elif d > a and d > b and d > c and d > e:
    maior = d
else:
    maior = e


print("numero maior:", maior)

#algoritmo que calcule a media de varios inteiros lidos, finaliza num numero negativo

print("Média Aritmética")
a = int(input("Insira 5 números inteiros positivos:\na: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))

if a or b or c or d or e < 0: quit

media = (a + b + c + d + e)/ 5

print("A média dos valores é:", media)