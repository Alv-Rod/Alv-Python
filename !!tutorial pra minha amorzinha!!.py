'''Oii amorr, te amo muiiitoooo!!
Esse programa aqui é pra tentar te ensinar algumas coisas de python q eu aprendi, 
desculpa se n for mto bom ou se n der pra entender direito ;-;
'''

#!primeiro!, pra fazer comentarios vc usa uma hashtag (#) pra linhas unicas

'''ou vc usa
3 apostrofes (')
pra varias linhas'''

#enfim, vamos lá!

print("Te amo muitoo") #print escreve coisas na tela, acho q isso vc ja sabe amorzinho
nomeDeVariavel = "essa variavel chama nomeDeVariavel!" #variaveis no python não levam definições de tipo, isso acontece automaticamente!
'''
--falando um pouco mais sobre--
tipos de variavel

str: string, uma junção de caracteres, formando frases, basicamente, textos

int: integer, números inteiros, até 2 bilhões
float: floating point, números reais
complex: numeros complexos

bool: boolean, tipo logico, de verdadeiro (True) e falso (False)

variaveis podem mudar de tipo durante o codigo, e alguns tipos podem ser convertidos diretamente 
(tipo, mudar uma variavel str representando um numero pra uma variavel int)'''

print(nomeDeVariavel) #voce pode escrever uma variavel

valorMeuAmor = 9999999999999999999 #esse valor é um float por ser maior que 2 bilhões
teAmoMuito = True #essa variavel é um boolean e é verdadeira :3

print(f"meu amor por voce é mais de {valorMeuAmor}") #isso mostra "meu amor por voce é mais de 9999999999999999999"

#juntar diferentes strings chamasse concatenar, em python pra concatenar valores q n são str, vc usa uma f-string
#vc coloca um f antes das aspas, e o valor que voce quer dentro de chaves

if teAmoMuito == True: #se (if) + condicional:
    print("Te amo muito!!")
elif teAmoMuito == False: #(else + if) + condicional:
    print("Isso é impossivel, esse codigo não é executado >:(")
else: #só else: (se não)
    print("Isso tbm é impossivel >:(")

'''loops:
for loop: para cada coisa, executa algo, até acabar (ou voce n querer mais)
while loop: enquanto algo for verdadeiro, executa algo, até não ser mais (ou ate vc n querer mais)
'''

amorzinho = "amorzinho"

for letras in amorzinho: #'for' umNomeLegal 'in' variavel
    print(letras)

#define um nome para as coisas pela qual o loop vai "iterar" ou passar (umNomeLegal), depois diz no que que voce quer passar (variavel)
#para cada iteração sobre aquela variavel, executa o codigo

executando = True

while executando == True:
    print("ta executando amorr!!")
    input("mas não quero mais, pressione algo para parar... ")
    executando = False #quando o codigo chegar aq, o loop para, e o codigo fora do loop continua
    
#uma demostração pratica:

while True:
    try: #'try:' tenta fazer algo; deve ser acompanhada de um except, serve para tentar coisas q podem dar errado, e "pegar" esses erros caso aconteçam 
        queroInteiro = int(input("Insira somente números inteiros grrrr: ")) #int(input()) tenta fazer o que for escrito no input virar um inteiro
        break #break quebra o loop, como nosso loop n tem condicional, oq faz ele parar de loopar é quando o int(input()) funcionar, ai esse break é lido.
    except ValueError: #except é onde os erros vão, ValueError especifica q o caso ocorra um erro desse tipo 
        #(nesse caso, vc inserir algo do Tipo certo, mas de valor inapropriado, ou seja, não inserir um inteiro), o codigo abaixo é executado:
        print("você não inseriu um valor inteiro >:(")
        continue #'continue' manda o loop continuar, dessa forma, ele não é quebrado até que o 'try' seja completo

print("continuação!!!")

'''
o que esse codigo faz é basicamente: 
tentar (try) pegar um valor inteiro > quando o valor for inteiro, o loop é quebrado (break)
caso ocorra uma exceção (except) e o valor não puder ser transformado num inteiro, o loop continua, até dar certo.
quando o loop é quebrado, o resto do codigo é lido
'''

print("TE AMO MINHA COELHINHA!\
    \natrasei minha hora de mimir pra fazer isso pra voce, me desculpa amorr :(\
    \nespero que voce esteja bem hoje, e se n estiver, espero que eu esteja te dando mtos abraços e beijinhos >:( se n vou ter q me bater dps\
    \nse vc estiver bem, tbm espero estar te dando mtos beijinhos e abraçinhos\
    \nte amo meu bem")